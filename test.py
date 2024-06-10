# import mysql.connector
# import os
# sql_password = os.getenv('SQL_PASSWORD')
# sql_username = os.getenv('SQL_USER')
# db_config = {
#     'host': 'localhost',
#     'user': sql_username,
#     'password': sql_password,
#     'database': 'basic_db',
# }

# mydb = mysql.connector.connect(**db_config)
# cursor = mydb.cursor()


# keyword = "%北%"
# cursor.execute("select * from processed_data where mrt = %s or name like %s;", (keyword, keyword)) 
# attract_data = cursor.fetchall()
# print(len(attract_data))

def create_counter():
    count = 0

    def increment():
        # nonlocal count
        count += 1
        print(count)
    
    return increment

counter1 = create_counter()
counter1()  # 1
counter1()  # 2

counter2 = create_counter()
counter2()  # 1
counter2()  # 2