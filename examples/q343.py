import xml.etree.ElementTree as ET

# Create the root element
root = ET.Element('bookstore')

# Add sub-elements using SubElement
book1 = ET.SubElement(root, 'book')
book2 = ET.SubElement(root, 'book')

# Add attributes and text content
book1.attrib['genre'] = 'Science Fiction'
book1.text = 'Title of Book 1'

book2.attrib['genre'] = 'Fantasy'
book2.text = 'Title of Book 2'

# Create an ElementTree object
tree = ET.ElementTree(root)

# Write the XML document to a file
tree.write('books.xml')
