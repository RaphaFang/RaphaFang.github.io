import mysql.connector
import os
sql_password = os.getenv('SQL_PASSWORD')
sql_username = os.getenv('SQL_USER')
db_config = {
    'host': 'localhost',
    'user': sql_username,
    'password': sql_password,
    'database': 'basic_db',
}

mydb = mysql.connector.connect(**db_config)
cursor = mydb.cursor()


keyword = "%北%"
cursor.execute("select * from processed_data where mrt = %s or name like %s;", (keyword, keyword)) 
attract_data = cursor.fetchall()
print(len(attract_data))