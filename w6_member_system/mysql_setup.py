import mysql.connector
import os
sql_password = os.getenv('SQL_PASSWORD')
sql_username = os.getenv('SQL_USER')

mydb = mysql.connector.connect(
  host="localhost",
  user=sql_username,
  password=sql_password,
  database="website" )

# 創建新的表
# cursor = mydb.cursor()
# sql = """
# CREATE TABLE login_data (
#     id BIGINT AUTO_INCREMENT PRIMARY KEY,
#     signup_username VARCHAR(255) NOT NULL,
#     signup_user_id VARCHAR(255) NOT NULL,
#     signup_password VARCHAR(255) NOT NULL
# )
# """
# cursor.execute(sql)


# cursor.execute("USE website")
# cursor.execute("SELECT * FROM login_data")
# result = cursor.fetchall()
# for x in result:
#     print(x)