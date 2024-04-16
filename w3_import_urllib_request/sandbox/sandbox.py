import urllib.request as request
import json
import csv

src1 = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1"
src2 = 'https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-2'

with request.urlopen(src1) as response:
    data1 = json.load(response)
with request.urlopen(src2) as response:
    data2 = json.load(response)

# print(len(data1["data"]["results"]))
station = [n['MRT'] for n in data2["data"]]
for n in station:
    if station.count(n)!=1:
        station.remove(n)  # >>>  處理station list串中重複出現
name_to_mrt={k["MRT"]:k["address"] for k in data2["data"]}  # >>>  處理data2中站名是values的問題，並且組成[{站明：地址}}


# with open('RaphaFang.github.io/w3_import_urllib_request/spot.csv', 'w', newline='') as file:
#     writer = csv.writer(file)

#     for n in range(len(data1["data"]["results"])):
#         SpotTitle = data1["data"]["results"][n]["stitle"]
#         for s in station:
#             if s+"站" in data1["data"]["results"][n]["info"]:
#                 District = name_to_mrt[s][5:7]+"區"
#                 break
#         Longitude = data1["data"]["results"][n]["longitude"]
#         Latitude = data1["data"]["results"][n]["latitude"]
#         if data1["data"]["results"][n]["filelist"].find(".jpg")==-1:
#             jpg = data1["data"]["results"][n]["filelist"].find(".JPG")
#         else:
#             jpg = data1["data"]["results"][n]["filelist"].find(".jpg" or ".JPG")
#         ImageURL = data1["data"]["results"][n]["filelist"][0:jpg+4]

#         writer.writerow([SpotTitle,District,Longitude,Latitude,ImageURL])

        

# with open('RaphaFang.github.io/w3_import_urllib_request/mrt.csv', 'w', newline='') as file:
#     writer = csv.writer(file)

mrt_dict = {n:[] for n in station}
for s in station:
    for n in range(len(data1["data"]["results"])):
        if s+"站" in data1["data"]["results"][n]["info"]:
            mrt_dict[s].append(data1["data"]["results"][n]["stitle"])

# print(mrt_dict)

# for n in mrt_dict:
#     StationName = n
#     AttractionTitle= ', '.join(mrt_dict[n])
#     print(StationName,AttractionTitle)
            
find_all