import mysql.connector
from commands import *
from db.loadcsv import *


conn=mysql.connector.connect(host='localhost',database='sensormanangement',user='root',password='2147483647')
if conn.is_connected(): print("success")
cursor =conn.cursor()


for path in list_path("C:\Downloads",csv):
    x=csv_filter(path)
    for row in x:
        row.insert(0,'1')
        cursor.execute(insert_data, tuple(row))
        conn.commit()
print(cursor.rowcount, "record inserted.")




