# Cracking the Coding Interview: 16.12
# Written by Josh Humphrey
import xml.etree.ElementTree as ET
hashmap = {"family":1,"person":2,"firstName":3,"lastName":4,"state":5}

def get_xml_root(file_name):
    tree = ET.parse(file_name)
    root = tree.getroot()
    return root

def encode_xml(xml_root):
    for child in xml_root:
        print("Tag: " + str(child.tag))
        print("Attribute: " + str(child.attrib))
        print("Element: " + str(xml_root))

xml_root = get_xml_root("data.xml")
encode_xml(xml_root)
