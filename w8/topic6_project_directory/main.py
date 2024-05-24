import mysql.connector
from mysql.connector import pooling

import os
sql_password = os.getenv('SQL_PASSWORD')
sql_username = os.getenv('SQL_USER')

pool_config = {
    'pool_name': 'my_pool',
    'pool_size': 1,
    'user': sql_username,
    'password': sql_password,
    'host': "localhost",
    'database': 'website'
}
mydb_pool = mysql.connector.pooling.MySQLConnectionPool(**pool_config)


def execute_query(query, params=None):
    try:
        mydb_pool_connection = mydb_pool.get_connection()   # Get a connection from the pool
        cursor = mydb_pool_connection.cursor()
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        
        if query.strip().lower().startswith(('insert', 'update', 'delete')):  # strip() -> Remove Whitespace
            mydb_pool_connection.commit()
            if cursor.rowcount == 0: 
                return ({"error": True},f'the output of cursor.rowcount is {cursor.rowcount}')
            return {"ok": True}
        
        if query.strip().lower().startswith('select'):
            results = cursor.fetchall()
            return results
        
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        mydb_pool_connection.close()


# by doing the code below, can't test the size of the pool
# select_query = "SELECT * FROM member WHERE id = %s"

# params = (1,)
# results = execute_query(select_query, params)
# for row in results:
#     print(row)

# params_2 = (2,)
# results = execute_query(select_query, params_2)
# for row in results:
#     print(row)
        

# instead, do this
        
def run_query(query, params):
    results = execute_query(query, params)
    if isinstance(results, list):
        for row in results:
            print(row)
    else:
        print(results)

import threading
import time
select_query = "SELECT * FROM member WHERE id = %s"
params_1 = (1,)
params_2 = (2,)

# Create threads for concurrent execution
thread1 = threading.Thread(target=run_query, args=(select_query, params_1))
thread2 = threading.Thread(target=run_query, args=(select_query, params_2))

# Start threads
thread1.start()
thread2.start()

# Wait for both threads to finish
thread1.join()
thread2.join()