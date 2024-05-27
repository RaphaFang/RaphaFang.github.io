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

# print(sql_username)



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
# 0
# rate : 5
# direction : "新北投站下車，沿中山路直走即可到達公車：216、218、223、230、266、602、小6、小7、小9、、小22、小25、小26至新北投站下車"
# name : "新北投溫泉區"
# date : "2016/07/07"
# longitude : "121.508447"
# REF_WP : "10"
# avBegin : "2010/02/14"
# langinfo : "10"
# MRT : "新北投"
# SERIAL_NO : "2011051800000061"
# RowNumber : "1"
# CAT : "養生溫泉"
# MEMO_TIME : "各業者不同，依據現場公告"
# POI : "Y"
# file : "https://www.travel.taipei/d_upload_ttn/sceneadmin/pic/11000848.jpghttps://www.travel.taipei/d_upload_ttn/sceneadmin/pic/11002891.jpghttps://www.travel.taipei/d_upload_ttn/sceneadmin/image/A0/B0/C0/D315/E70/F65/1e0951fb-069f-4b13-b5ca-2d09df1d3d90.JPGhttps://www.travel.taipei/d_upload_ttn/sceneadmin/image/A0/B0/C0/D260/E538/F274/e7d482ba-e3c0-40c3-87ef-3f2a1c93edfa.JPGhttps://www.travel.taipei/d_upload_ttn/sceneadmin/image/A0/B0/C0/D919/E767/F581/9ddde70e-55c2-4cf0-bd3d-7a8450582e55.jpghttps://www.travel.taipei/d_upload_ttn/sceneadmin/image/A0/B0/C1/D28/E891/F188/77a58890-7711-4ca2-aebe-4aa379726575.JPG"
# idpt : "臺北旅遊網"
# latitude : "25.137077"
# description : "北投溫泉從日據時代便有盛名，深受喜愛泡湯的日人自然不會錯過，瀧乃湯、星乃湯、鐵乃湯就是日本人依照溫泉的特性與療效給予的名稱，據說對皮膚病、神經過敏、氣喘、風濕等具有很好的療效，也因此成為了北部最著名的泡湯景點之一。新北投溫泉的泉源為大磺嘴溫泉，泉質屬硫酸鹽泉，PH值約為3~4之間，水質呈黃白色半透明，泉水溫度約為50-90℃，帶有些許的硫磺味 。目前北投的溫泉旅館、飯店、會館大部分集中於中山路、光明路沿線以及北投公園地熱谷附近，總計約有44家，每一家都各有其特色，多樣的溫泉水療以及遊憩設施，提供遊客泡湯養生，而鄰近的景點也是非常值得造訪，例如被列為三級古蹟的三寶吟松閣、星乃湯、瀧乃湯以及北投第一家溫泉旅館「天狗庵」，都有著深遠的歷史背景，而北投公園、北投溫泉博物館、北投文物館、地熱谷等，更是遊客必遊的景點，來到北投除了可以讓溫泉洗滌身心疲憊，也可以順便了解到北投溫泉豐富的人文歷史。"
# _id : 1
# avEnd : "2016/07/07"
# address : "臺北市 北投區中山路、光明路沿線"
    
# print(len(data['result']['results']))


# id = data['result']['results'][0]['_id']
# name = data['result']['results'][0]['name']
# category = data['result']['results'][0]['CAT']
# description = data['result']['results'][0]['description']
# address = data['result']['results'][0]['address']
# transport = data['result']['results'][0]['direction']
# mrt = data['result']['results'][0]['MRT']
# lat = data['result']['results'][0]['latitude']
# lng = data['result']['results'][0]['longitude']
# images_str = data['result']['results'][0]['file']
# images_list

images_str = data['result']['results'][0]['file']
# for n in cut_list:
cut_list = ["https://"+n for n in images_str.split("https://") if n]
print(cut_list)


