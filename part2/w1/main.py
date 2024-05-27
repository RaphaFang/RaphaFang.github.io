# import mysql.connector
# import os
# sql_password = os.getenv('SQL_PASSWORD')
# sql_username = os.getenv('SQL_USER')
# mydb = mysql.connector.connect(
#   host="localhost",
#   user=sql_username,
#   password=sql_password,
#   database="Day_Trip")
# cursor = mydb.cursor()

# 1. read the json file
import json
url = '/Users/fangsiyu/Desktop/wehelp/RaphaFang.github.io/part2/w1/taipei-attractions.json'
with open(url, 'r') as file:
    data = json.load(file)

# 2. convert the data into specific formate
# the format request

# {
#   "nextPage": 1,
#   "data": [
#     {
#       "id": 10,
#       "name": "平安鐘",
#       "category": "公共藝術",
#       "description": "平安鐘祈求大家的平安，這是為了紀念 921 地震週年的設計",
#       "address": "臺北市大安區忠孝東路 4 段 1 號",
#       "transport": "公車：204、212、212直",
#       "mrt": "忠孝復興",
#       "lat": 25.04181,
#       "lng": 121.544814,
#       "images": [
#         "http://140.112.3.4/images/92-0.jpg"
#       ]
#     }
#   ]
# }

id = data['result']['results'][1]['_id']
print(id)

name = data['result']['results'][0]['name']
category = data['result']['results'][0]['CAT']
description = data['result']['results'][0]['description']
address = data['result']['results'][0]['address']
transport = data['result']['results'][0]['direction']
mrt = data['result']['results'][0]['MRT']
lat = data['result']['results'][0]['latitude']
lng = data['result']['results'][0]['longitude']
images_str = data['result']['results'][0]['file']
cut_list = ["https://"+n for n in images_str.split("https://") if n and (n[-3:].upper()=='JPG' or n[-3:].upper()=='PNG')]
json_format_str = json.dumps(cut_list)

# aaa = 'abcde'
# print(aaa[-3:].upper())