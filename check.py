# Example usage: python check.py < DELFI_LOD1.xml
import sys

# The following attributes are excluded because they are derived/calculated: 3080, 3125, 3126 3127, 3131, 3132
attributes=[3010,3020,3021,3030,3031,3050,3051,3060,3061,3070,3090,3100,3101,3110,3111,3112,3113,3120,3121,3122,3123,3124,3130,3133,3140]

file=sys.stdin.read()

missing=[attr for attr in attributes if str(attr) not in file]
if not missing:
    print('All DELFI attributes are present.')
else:
    print(f'DELFI attributes {', '.join(map(str, missing))} are missing.')
