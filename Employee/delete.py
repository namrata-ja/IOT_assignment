
import mysql.connector

connection = mysql.connector.connect(
    host = "localhost",
    port = 3306,
    user = "root",
    password = "password",
    database = "iotdb"
)

uid = 6

query = f"delete from persons where uid = {uid};"

cursor = connection.cursor()

cursor.execute(query)

connection.commit()

cursor.close()

connection.close()