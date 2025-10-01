import xml.etree.ElementTree as ET


root = ET.Element('students')


student1 = ET.SubElement(root, 'student')
student2 = ET.SubElement(root, 'student')


student1.attrib['id'] = '101'
name1 = ET.SubElement(student1, 'name')
name1.text = 'Alice'
age1 = ET.SubElement(student1, 'age')
age1.text = '20'

student2.attrib['id'] = '102'
name2 = ET.SubElement(student2, 'name')
name2.text = 'Bob'
age2 = ET.SubElement(student2, 'age')
age2.text = '22'

tree = ET.ElementTree(root)

tree.write('students.xml')
