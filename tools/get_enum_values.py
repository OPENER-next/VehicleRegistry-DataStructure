import xml.etree.ElementTree as ElementTree
from urllib.request import urlopen


def list_enum_values(url, name):
  with urlopen(url) as f:
      elements = ElementTree.parse(f).findall(
          f'.//xsd:simpleType[@name="{name}"]//xsd:enumeration',
          {'xsd': 'http://www.w3.org/2001/XMLSchema'}
      )
      for e in elements: print(f'- {e.get('value')}')

# Example: https://raw.githubusercontent.com/NeTEx-CEN/NeTEx/refs/heads/next/xsd/netex_framework/netex_reusableComponents/netex_facility_support.xsd
url = input("Enter the full URL to the XSD file: ")
# Example: PassengerInformationFacilityEnumeration
name = input("Enter the enumeration name: ")
list_enum_values(url, name)
