import xml.etree.ElementTree as ET

tree = ET.parse('book1.xml')
root = tree.getroot()

first_book_title = root[0][0].text
print("Title of the first book:", first_book_title)

second_book_author = root[1][0].text
print("Author of the second book:", second_book_author)
