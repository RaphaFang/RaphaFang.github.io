import urllib.request as request
import json

src1 = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1"
src2 = 'https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-2'

with request.urlopen(src1) as response:
    data1 = json.load(response)

with request.urlopen(src2) as response:
    data2 = json.load(response)

# def 
    


# print(data1["data"]["results"][0]["stitle"])
station = [n['MRT'] for n in data2["data"]]
# station = [n for n in station if n]
for n in station:
    if station.count(n)!=1:
        station.remove(n)
for n in station:
    if n+"站" in data1["data"]["results"][0]["info"]:
        data2["data"]["results"][0]["info"]
        print(n)
        break
print(data1["data"]["results"][0]["info"])
print(data1["data"]["results"][1]["info"])
print(data1["data"]["results"][0]["longitude"])
print(data1["data"]["results"][0]["latitude"])
jpg = data1["data"]["results"][0]["filelist"].find(".jpg")
print(data1["data"]["results"][0]["filelist"][0:jpg+4])
print(station)
print(1+1)

# ["latitude"]

# 解決ssl讀取阻擋：透過 Install Certificates.command
#       https://support.chainstack.com/hc/en-us/articles/9117198436249-Common-SSL-Issues-on-Python-and-How-to-Fix-it
# 解決地區明＼XX區＼經緯度＼第一張照片