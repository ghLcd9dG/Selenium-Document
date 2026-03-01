#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
import csv
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

csv_file=open('city.csv','r',encoding="utf8")
reader=csv.reader(csv_file)
for item in reader:
    print(item)
    '''
import csv

# 文件头，一般就是数据名
header=["name","gender","score"]
file_1=["zhang_san","male","100"]
file_2=["Li_si","male","80"]

# 创建
# 如果不加,newline=''会多一行空行
csvFile = open("writer.csv","w",newline='')
writer = csv.writer(csvFile)

# 写入的内容都是以列表的形式传入函数
writer.writerow(header)
writer.writerow(file_1)
writer.writerow(file_2)

#关闭
csvFile.close()