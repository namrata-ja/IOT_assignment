
import mysql.connector

connection = mysql.connector.connect(
    host = "localhost",
    port = 3306,
    user = "root",
    password = "password",
    database = "iotdb"
)

empid = 6
name = "namrata"
department = "marketing"
email = "namratajadhavgmail.com"
salary ="10000"
Doj = "18 "


query = f"insert into persons(empid,name,department,email,salary,doj) values('{empid}', {name}, {department}, {email}, '{salary}' '{Doj}');"

cursor = connection.cursor()

cursor.execute(query)

connection.commit()

cursor.close()

connection.close()