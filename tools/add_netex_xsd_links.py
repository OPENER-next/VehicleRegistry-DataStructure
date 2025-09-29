# Used to automatically find and set XSD references to markdown files.
# Arguments:
# 1. Affected directory
# 2. NeTEx branch
# Example: python add_netex_xsd_links.py ../docs/src/ next
import os
import sys
import fileinput
from zipfile import ZipFile
from pathlib import Path
import urllib.request

'''
Searches through the NeTEx XSD files.
Requires the NeTEx repo given as a zip and a list of element names to search for.
Returns an iterable of matches for the given element names.
The order of the returned iterable depends on which element was found first.
'''
def findXSDMatchesByName(netexZipPath, elementNames):
  remainingElementNames = set(elementNames)

  with ZipFile(netexZipPath) as zipFile:
    for member in zipFile.infolist():
      # filter for files
      if not member.is_dir():
        filePathParts = Path(member.filename).parts
        # filter for files inside the xsd directory
        if len(filePathParts) > 1 and filePathParts[1] == 'xsd':
          with zipFile.open(member) as file:
            for lineNumber, line in enumerate(file, 1):
              lineText = line.decode("utf-8")
              # get first matching element from set
              # https://stackoverflow.com/a/37401376/3771196
              match = next(
                (x for x in remainingElementNames if f'name="{x}"' in lineText),
                False
              )
              if match:
                yield {
                  'item': match,
                  # strip leading directory from path
                  'filePath': Path(*filePathParts[1:]).as_posix(),
                  'lineText': lineText,
                  'lineNumber': lineNumber,
                }
                remainingElementNames.remove(match)
                if len(remainingElementNames) == 0: return


'''
Construct a GitHub URL pointing to the NeTEx repo based on branch, file path and line number.
'''
def makeGithubURLToFile(branch, filePath, lineNumber):
  return f'https://github.com/NeTEx-CEN/NeTEx/blob/{branch}/{filePath}#L{lineNumber}'


'''
Finds the first markdown title (# Title) for each file in the given directory.
Returns an iterable of tuples containing the file path mapped to their respective markdown title.
'''
def findFileTitles(directory):
  for (dirpath, dirnames, filenames) in os.walk(directory):
    for filename in filenames:
      path = f'{dirpath}/{filename}'
      with open(path,'r') as file:
        for line in file:
          if line.strip().startswith('# '):
            yield path, line.split("# ",1)[1].strip()
            break


'''
Updates all given markdown files with an XSD ref.
Expects a dictionary with markdown file paths mapped to XSD matches (produced by findXSDMatchesByName).
'''
def setXSDReferencesOnFiles(matches, branch):
  for filePath, match in matches.items():
    with fileinput.input(filePath, inplace=True) as file:
      refIsPresent = False
      # rewrite file
      for line in file:
        if not refIsPresent:
          if line.startswith('**XSD:**'):
            # found existing ref, update it
            url = makeGithubURLToFile(branch, match['filePath'], match['lineNumber'])
            line = f'**XSD:** [`{match['filePath']}`]({url})' + os.linesep
            refIsPresent = True
          elif line.startswith('##'):
            # found next heading section, insert ref
            url = makeGithubURLToFile('next', match['filePath'], match['lineNumber'])
            ref = f'**XSD:** [`{match['filePath']}`]({url})'
            line = ref + os.linesep + os.linesep + line
            refIsPresent = True
        sys.stdout.write(line)



directory = sys.argv[1]
branch = sys.argv[2]
zipName = 'netex.zip'

urllib.request.urlretrieve(f'https://github.com/NeTEx-CEN/NeTEx/archive/refs/heads/{branch}.zip', zipName)

filePathToTitleMapping = tuple(findFileTitles(directory))

# rematch files ot matches
mapping = {}
for match in findXSDMatchesByName(zipName, map(lambda x: x[1], filePathToTitleMapping)):
  for path, title in filePathToTitleMapping:
    if title == match['item']:
      mapping[path] = match

setXSDReferencesOnFiles(mapping, branch)

os.remove(zipName)
