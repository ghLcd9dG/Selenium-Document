import csv
file=open('city.csv','r',  encoding='utf-8',errors='ignore')
csv_file = csv.reader(file)
for i in csv_file:
    print(i)

