# Used to automatically update and enrich the doc files.
# Requires lxml (mostly because it offers file line information)
# This script is optimized for readability and extensibility at the expense of performance
# Arguments:
# 1. Affected directory
# 2. NeTEx branch
# Example: python add_netex_xsd_links.py ../docs/src/ next
import os
import sys
import fileinput
import urllib.request
import re
from zipfile import ZipFile
from pathlib import Path
from lxml import etree

'''
Expects a zip file of the NeTEx repo.
Returns an iterator over all NeTEx XSD files.
The iterator produces tuples containing an XML Tree and the file path.
'''
def iterZipXSDFiles(zipFile):
  for member in zipFile.infolist():
    # filter for files
    if not member.is_dir():
      filePathParts = Path(member.filename).parts
      # filter for files inside the xsd directory
      if len(filePathParts) > 1 and filePathParts[1] == 'xsd':
        with zipFile.open(member) as file:
          yield etree.parse(file), Path(*filePathParts[1:]).as_posix()


'''
Inserts/updates enum values based on headings formatted like #### Values (`ENUM_NAME_HERE`):
'''
class EnumValuesLineReplacer:
  def __init__(self, zipFile):
    self.zipFile = zipFile
    self.valueListFound = False

  '''
  Expects a line of the currently processed file.
  Returns True if this replacer took effect otherwise False.
  '''
  def run(self, line):
    if self.valueListFound:
      if len(line.strip()) == 0:
        # ignore empty lines
        sys.stdout.write(line)
        return True
      elif line.startswith('- '):
        # remove existing list values
        return True
      else:
        self.valueListFound = False
    else:
      match = re.search(r'(?<=(# Values \(`)).*(?=(`\):))', line)
      if match:
        elements = self.findEnumElementsByName(match.group(0))
        if elements:
          sys.stdout.write(line)
          sys.stdout.write(self.enumValuesAsMarkdown(elements))
          self.valueListFound = True
          return True
    return False

  def findEnumElementsByName(self, name):
    pattern = f'.//xsd:simpleType[@name="{name}"]//xsd:enumeration'
    for tree, path in iterZipXSDFiles(self.zipFile):
      if tree.find(pattern, {'xsd': 'http://www.w3.org/2001/XMLSchema'}) is not None:
        return tree.iterfind(pattern, {'xsd': 'http://www.w3.org/2001/XMLSchema'})

  def enumValuesAsMarkdown(self, elements):
    output = ''
    for element in elements:
      output += f'- {element.get('value')}{os.linesep}'
    return output


'''
Inserts/updates XSD references for the main elements based on the title (# XXX) name.
'''
class XSDGithubRefLineReplacer:
  def __init__(self, zipFile, branch):
    self.zipFile = zipFile
    self.branch = branch
    self.refIsPresent = False
    self.element = None
    self.filePath = None

  '''
  Expects a line of the currently processed file.
  Returns True if this replacer took effect otherwise False.
  '''
  def run(self, line):
    match = re.search(r'(?<=(^#)\s).*', line)
    if match:
      self.element, self.filePath = self.findElementByName(match.group(0).strip())
    elif self.element is not None and not self.refIsPresent:
      if line.startswith('**XSD:**'):
        # found existing ref, update it
        sys.stdout.write(self.xsdGithubRefAsMarkdown(self.filePath, self.element.sourceline))
        self.refIsPresent = True
        return True
      elif line.startswith('##'):
        # found next heading section, insert ref
        sys.stdout.write(self.xsdGithubRefAsMarkdown(self.filePath, self.element.sourceline))
        sys.stdout.write(os.linesep)
        sys.stdout.write(line)
        self.refIsPresent = True
        return True
    return False

  def findElementByName(self, name):
    pattern = f'.//xsd:element[@name="{name}"]'
    for tree, filePath in iterZipXSDFiles(self.zipFile):
      result = tree.find(pattern, {'xsd': 'http://www.w3.org/2001/XMLSchema'})
      if result is not None:
        return result, filePath
    return None, None

  def xsdGithubRefAsMarkdown(self, filePath, lineNumber):
    url = f'https://github.com/NeTEx-CEN/NeTEx/blob/{self.branch}/{filePath}#L{lineNumber}'
    return f'**XSD:** [`{filePath}`]({url}){os.linesep}'


################ Main ################

directory = sys.argv[1]
branch = sys.argv[2]
zipFilePath = 'netex.zip'
# download NeTEx as zip
urllib.request.urlretrieve(f'https://github.com/NeTEx-CEN/NeTEx/archive/refs/heads/{branch}.zip', zipFilePath)

with ZipFile(zipFilePath) as zipFile:
  # loop through all given files
  for (dirpath, dirnames, filenames) in os.walk(directory):
    for filename in filenames:
      filePath = os.path.join(dirpath, filename)
      # NOTE: this redirects all prints/std:outs to the file
      with fileinput.input(filePath, inplace=True) as file:
        replacers = (
          XSDGithubRefLineReplacer(zipFile, branch),
          EnumValuesLineReplacer(zipFile),
        )
        # rewrite file
        for line in file:
          if not any(map(lambda r: r.run(line), replacers)):
            sys.stdout.write(line)

  os.remove(zipFilePath)
