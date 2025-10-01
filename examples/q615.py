import xml.etree.ElementTree as ET
tree = ET.parse('books.xml')
root = tree.getroot()
new_root = ET.Element('bookstore')
for book in root:
    new_root.append(book)
tree._setroot(new_root)
tree.write('MODIFIED_BOOK.xml')
