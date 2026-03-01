from xml.etree import ElementTree as et

xml_string=b'<test><name>zhang_san</name><gender>female</gender><phone_number>01234567890</phone_number><note>none</note></test>'

root=et.fromstring(xml_string)


print("*****====================================*****")
#列表形式输出的内存地址
for i in list(root):
    print(i.tag,i.text)

print("*****====================================*****")
test_person=root.getiterator("test")
#用来输出内容
for i in test_person:
    for j in i:
        print(j.tag,j.text)

print("*****====================================*****")
#返回的是一个列表
find_node2=root.findall("name")
print(find_node2[0],find_node2[0].tag,find_node2[0].text)

print("*****====================================*****")
#查找获得的第一个
find_node=root.find("name")
print(find_node,find_node.tag,find_node.text)




'''
IDLE:
>>> from xml.etree import ElementTree as et
>>> xml_string=b'<test><name>zhang_san</name><gender note="transsexuals">male</gender><phone_number>01234567890</phone_number><note>none</note></test>'
>>> root=et.fromstring(xml_string)
>>> root.tag
'test'
>>> root.attrib
{}
>>> for i in root:
    print(i.tag,i.attrib)

name {}
gender {'note': 'transsexuals'}
phone_number {}
note {}

#元素，返回值
>>> for i in root:
    print(i)

<Element 'name' at 0x000000541846F9F8>
<Element 'gender' at 0x000000541846FAE8>
<Element 'phone_number' at 0x000000541846FBD8>
<Element 'note' at 0x000000541846FB88>
>>> for i in root:
    print(i.text)

zhang_san
male
01234567890
none
'''