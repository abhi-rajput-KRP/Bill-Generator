import mysql.connector
conn = mysql.connector.connect(host='localhost',user='root',database='bill',passwd='krpabhi9876')
cur = conn.cursor()

vend_li = [("Dhanpat Rai",4000),("S-Chand",2000),("Oxford",5000),("Cambridge",6000)]

for i in vend_li:
    query = 'insert into vendor values(%s,%s)'
    val = (i[0],i[1])
    cur.execute(query,val)
    conn.commit()