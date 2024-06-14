import os
import mysql.connector.pooling

sql_password = os.getenv('SQL_PASSWORD')
sql_username = os.getenv('SQL_USER')

pool_config = {
    'pool_name': 'day_trip_pool',
    'pool_size': 10,
    'host': '52.4.229.207',
    'user': sql_username,
    'password': sql_password,
    'database': 'basic_db',
    'port':3306

}
mydb_pool = mysql.connector.pooling.MySQLConnectionPool(**pool_config)


# db_config = {
#     'host': '52.4.229.207',
#     'user': sql_username,
#     'password': sql_password,
#     'database': 'basic_db',

#     'port':3306
# }

def create_db_pool(db):
    dbconfig = {
        "database": db,
        "user": "root",
        "password": os.environ['MYSQL_PASSWORD']
    }
    return mysql.connector.pooling.MySQLConnectionPool(pool_name="mypool", pool_size=10, **dbconfig)