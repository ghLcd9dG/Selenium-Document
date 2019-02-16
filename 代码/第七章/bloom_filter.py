import os
from pybloom_live import BloomFilter

#你完全可以避免下载庞大的vc运行库，在https://www.lfd.uci.edu/~gohlke/pythonlibs/下载whl文件
'''
animals = ['dog', 'cat', 'giraffe', 'fly', 'mosquito', 'horse', 'eagle',
           'bird', 'bison', 'boar', 'butterfly', 'ant', 'anaconda', 'bear',
           'chicken', 'dolphin', 'donkey', 'crow', 'crocodile','testadd']
'''
is_exist = os.path.exists('test.blm')
#判断是否存在bloom文件
#判断存在就读取
if is_exist:
    bf = BloomFilter.fromfile(open('test.blm', 'rb'))
   #没有该文件则创建bf对象 最后的时候保存文件
else:
    bf = BloomFilter(20000, 0.001)


for i in range(10):
    if i in bf:
        print('pass')
        pass
    else:
        print('add %s' %i)
        bf.add(i)
        n=open('test.blm','wb')
        bf.tofile(n)
        n.close()
for i in range(20):
    if i in bf:
        print("written")
    else:
        print("unwritten")
