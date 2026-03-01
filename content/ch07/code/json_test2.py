import json
#json库提供四个方法，json.dump(),json.dumps(),json.load(),json.load()
#dumps是将dict转化成str格式，loads是将str转化成dict格式。
#文件输出也略有差异
#
json_data={
  "results": [
    {
      "location": {
        "id": "WX4FBXXFKE4F",
        "name": "北京",
        "country": "CN",
        "path": "北京,北京",
        "timezone": "Asia/Shanghai",
        "timezone_offset": "+08:00"
      }

    }
  ]
}
f = open('test.txt', 'w')
print(type(json_data))
json.dump(json_data, f)
#必须先关闭，然后才会写入
f.close()

#注，不能同时使用
#f.read()和json.load(f)
#read()调用后，load()方法就会什么都获取不到
#笔者就在这里纠结了好久
#报错json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
#其实根本没有获取到文件
f=open('test.txt', 'r')
print(f.read())
f.close()

#读取test.txt内容
f=open('test.txt', 'r')
#load方法
print(json.load(f))
f.close()

