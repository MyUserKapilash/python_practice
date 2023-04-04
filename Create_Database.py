#DB1.py
#Create Database

import pymysql
try:
    con = pymysql.connect(host="localhost",user="root",password="12345")
    cursor = con.cursor()
    cursor.excute("CREATE DATABASE demo_bd")
    print("Database created succesfully")
    con.commit()
except pymysql.DatabaseError as e:
    if con:
        con.rollback()
        print("There is a problem with date:",e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
    

