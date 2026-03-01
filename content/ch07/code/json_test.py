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

b=json.dumps(json_data)
print(b,type(b))
c=json.loads(b)
print(c,type(c))
