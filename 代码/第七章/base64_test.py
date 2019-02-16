# -*- coding: utf-8 -*-
# @Author: name
# @Date:   2018-07-31 20:56:26
# @Last Modified by:   name
# @Last Modified time: 2018-07-31 21:04:17
import base64
string=b"admin"
encoded=base64.b64encode(string)
decoded=base64.b64decode(encoded)
print(encoded)
print(decoded)