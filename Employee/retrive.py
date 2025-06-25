
import mysql.connector

connection = mysql.connector.connect(
    host = "localhost",
    port = 3306,
    user = "root",
    password = "password",
    database = "iotdb"
)

query = "select * from persons;"

cursor = connection.cursor()

cursor.execute(query)

persons = cursor.fetchall()         

for p in persons:
    print(p)

cursor.close()

connection.close()