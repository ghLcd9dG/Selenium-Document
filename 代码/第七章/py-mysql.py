#导入库
import pymysql

#创建数据库
conn=pymysql.connect(host='localhost',port=3306,db='test',user='root',passwd='password',charset='utf8')
cur=conn.cursor()

#查询原数据------------------------------------------------
select="SELECT * FROM user_info"
cur.execute(select)
all_data=cur.fetchall()
print(all_data)
print("*****====================================*****")

#插入数据
insert="INSERT INTO user_info VALUES('li_liu',2,123456789);"
count=cur.execute(insert)

#输出插入后
select="SELECT * FROM user_info;"
cur.execute(select)
all_data=cur.fetchall()
print(all_data)
print("*****====================================*****")

#删除数据
delete='DELETE FROM user_info WHERE log_in="wang_wu";'
count=cur.execute(delete)

#输出删除后
select="SELECT * FROM user_info;"
cur.execute(select)
all_data=cur.fetchall()
print(all_data)
print("*****====================================*****")

#更改
update='UPDATE user_info SET log_in="im changed" WHERE id=0;'
count=cur.execute(update)

#输出更改后
select="SELECT * FROM user_info;"
cur.execute(select)
all_data=cur.fetchall()
print(all_data)
print("*****====================================*****")


conn.commit()
#关闭
cur.close()
# 关闭数据库连接
conn.close()
