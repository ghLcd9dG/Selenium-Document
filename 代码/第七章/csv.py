import csv

Headers=['name','gender','phone_number','note']
file_1=['张三','男','1234567890','无']
file_2=['李四','男','1234567890','无']
file_3=['王五','男','1234567890','有']
file_4=['郭六','女','1234567890','无']

with open('test.csv','a') as f:
    writer=csv.writer(f)
    writer.writerow(Headers)
    writer.writerow(file_1)
    writer.writerow(file_2)
    writer.writerow(file_3)
    writer.writerow(file_4)

