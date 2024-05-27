import mysql.connector
import os
sql_password = os.getenv('SQL_PASSWORD')
sql_username = os.getenv('SQL_USER')
mydb = mysql.connector.connect(
  host="localhost",
  user=sql_username,
  password=sql_password,
  database="basic_db")
cursor = mydb.cursor()

# 1. read the json file
import json
url = '/Users/fangsiyu/Desktop/wehelp/RaphaFang.github.io/part2/w1/taipei-attractions.json'
with open(url, 'r') as file:
    data = json.load(file)

# 2. convert the data into specific formate, and inser in SQL
# the format request
# processed_data
# INSERT INTO processed_data (id, name, category, description, address, transport, mrt, lat, lng, json_format_str)
# VALUES ('test', 'test', 'test');
    
for j in range(0, len(data['result']['results'])):
    id = int(data['result']['results'][j]['_id'])
    name = data['result']['results'][j]['name']
    category = data['result']['results'][j]['CAT']
    description = data['result']['results'][j]['description']
    address = data['result']['results'][j]['address']
    transport = data['result']['results'][j]['direction']
    mrt = data['result']['results'][j]['MRT']
    lat = float(data['result']['results'][j]['latitude'])
    lng = float(data['result']['results'][j]['longitude'])
    
    images_str = data['result']['results'][j]['file']
    cut_list = ["https://"+n for n in images_str.split("https://") if n and (n[-3:].upper()=='JPG' or n[-3:].upper()=='PNG')]
    json_format_str = json.dumps(cut_list)

    cursor.execute("INSERT INTO processed_data (id, name, category, description, address, transport, mrt, lat, lng, images) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);",(id, name, category, description, address, transport, mrt, lat, lng, json_format_str))
    mydb.commit()

print('process finished')




# aaa = 'abcde'
# print(aaa[-3:].upper())