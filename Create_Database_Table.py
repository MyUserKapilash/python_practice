#Create Table Using MySQL
import pymysql
try:
    con = pymysql.connect(host="localhost",database="demo_db",user="root",password="12345")
    cursor = con.cursor()
    Sql_query = "create table employees(eno int(5) primary key,\
    ename varchar(10),esal double(10,2),\
    eaddr varchar(10));"
    cursor.execute(sql_query)
    print("Table created successfully")
    con.commit()
except pymysql.DatabaseError as e:
    if con:
        con.rollback()
        print("There is a problem with database:",e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
          
