from xml.etree.ElementTree import tostring
from xml.etree.ElementTree import Element

dict = { "name":"zhang_san", "gender":"female", "phone_number":"01234567890","note":"none"}
def convert(tag_name,dict):
    #建立一个XML
    elem = Element(tag_name)

    #双值循环取出字典中的key和value
    for key,value in dict.items():

        #打印
        print(key,":",value)

        #相当于为key建一个标签
        xml_elem=Element(key)
        #将key的值赋给这个标签的值
        xml_elem.text=str(value)

        #添加进XML文件
        elem.append(xml_elem)

    return elem

#字典转换
dict_convert = convert("test", dict)
print("-------------------------------------------")
print(dict_convert)

#这是转换为标准的XML
print(tostring(dict_convert))
#设置最外层标签属性
dict_convert.set('id_number','01234567890')
#再次输出
print(tostring(dict_convert))

'''
text=tostring(e)
print(text)
'''