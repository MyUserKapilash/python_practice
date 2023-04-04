#Getting_Data_from_the_Table
import pymysql
try:
    con = pymysql.connect(host="localhost",
                          database="demo_db",
                          user="root",password="Kapilash@123")
    cursor = con.cursor()
    sql_query("insert into employees valie(100,'Durga',1000,'Hyd'):")
    cursor.execute(sql_query)
    print("Data inserted successfully")
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
