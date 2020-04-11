import xml.etree.ElementTree as ET
from xml.dom import minidom


def create_xml_tree(root, dict_tree):
    # Node : recursively create tree nodes
    if type(dict_tree) == dict:
        for k, v in dict_tree.items():
            create_xml_tree(ET.SubElement(root, k), v)
        return root
    # Leaf : just set the value of the current node
    else:
        root.text = str(dict_tree)


def prettify(elem):
    """Return a pretty-printed XML string for the Element
    """
    rough_string = ET.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="".join([' '] * 4))


def output(tree):
    """
    Takes tree generated and creates an xml file in the root
    directory.
    """
    with open('estimate.xml', 'w') as output:
        output.write(prettify(tree))
