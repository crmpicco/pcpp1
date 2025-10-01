# XML file

"""

<?xml version="1.0" encoding="UTF-8"?>
<library>
    <book>
        <title>Python Programming</title>
        <author>John Doe</author>
        <isbn>978-1234567890</isbn>
    </book>
    <book>
        <title>Java Basics</title>
        <author>Jane Smith</author>
        <isbn>978-9876543210</isbn>
    </book>
    <book>
        <title>C++ Fundamentals</title>
        <author>Robert Johnson</author>
        <isbn>978-5432109876</isbn>
    </book>
</library>

"""

import xml.etree.ElementTree as ET

tree = ET.parse('new 1.xml')
root = tree.getroot()
print(root.tag)
