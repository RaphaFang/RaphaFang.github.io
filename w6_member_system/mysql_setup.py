import mysql.connector
import os
sql_password = os.getenv('SQL_PASSWORD')
sql_username = os.getenv('SQL_USER')

mydb = mysql.connector.connect(
  host="localhost",
  user=sql_username,
  password=sql_password)

cursor = mydb.cursor()

cursor.execute("CREATE TABLE login (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), position VARCHAR(255))")


# cursor.execute("USE website")
# cursor.execute("SELECT * FROM member")
# result = cursor.fetchall()
# for x in result:
#     print(x)