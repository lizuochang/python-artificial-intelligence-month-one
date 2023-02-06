import pymysql
import re

f = open('dict.txt')
# db = pymysql.connect('localhost', 'root','lzc50090', 'dict')
db = pymysql.connect(host='localhost', user='root', password='123456', db='dict')
cur = db.cursor()
sql = 'insert into words (word,mean) \
values(%s,%s)'
for line in f:
    tup_temp = re.findall(r'(\w+)\s+(.*)', line)[0]
    try:
        cur.execute(sql, tup_temp)
        db.commit()
    except Exception:
        db.rollback()
f.close()
cur.close()
db.close()

# print(sql)
