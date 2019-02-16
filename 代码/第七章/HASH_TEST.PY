#导入哈希算法库
import hashlib

#MD5加密
md5_1 = hashlib.md5()
md5_1.update(b'using md5 in python')
print(md5_1.hexdigest())

#如果数据量很大，可以分块多次调用update()，最后计算的结果是一样的
md5_2 = hashlib.md5()
md5_2.update(b'using md5')
md5_2.update(b' in python')
print(md5_2.hexdigest())

#SHA1加密
sha1 = hashlib.sha1()
sha1.update(b'using sha1 in python')
print(sha1.hexdigest())
