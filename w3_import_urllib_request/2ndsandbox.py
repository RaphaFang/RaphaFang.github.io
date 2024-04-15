# from itertools import groupby
# import urllib.request as request
# import json

# src1 = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1"
# src2 = 'https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-2'

# with request.urlopen(src1) as response:
#     data1 = json.load(response)
# with request.urlopen(src2) as response:
#     data2 = json.load(response)

# # Your original list
# station = [n['MRT'] for n in data2["data"]]
# print(station)
# print(len(station))

# list = station
# # Using groupby to remove consecutive duplicates
# result = [key for key, group in groupby(list)]
# print(result)
# print(len(result) )# Output: [1, 2, 3]

# for n in station:
#     if station.count(n)!=1:
#         station.remove(n)  # >>>  處理station list串中重複出現
# print(station)
# print(len(station))

from collections import Counter

list1 = ['文德', '中正紀念堂', '關渡', '西門', '松山', '關渡', '北投', '葫洲', '臺大醫院', '劍潭', '木柵', '忠孝新生', '市政府', '圓山', '芝山', '劍潭', '龍山寺', '公館', '新北投', '雙連', '士林', '士林', '新北投', '圓山', '大湖公園', '大直', '關渡', '劍潭', '石牌', '中山', '中山', '圓山', '忠義', '動物園', '松江南京', '雙連', '新北投', '中山', '國父紀念館', '士林', '動物園', '劍潭', '唭哩岸', '大安森林公園', '新北投', '象山', '龍山寺', '行天宮', '新北投', '中正紀念堂', '市政府', '動物園', '新北投', '關渡', '忠孝新生', '臺大醫院', '台北101／世貿', '龍山寺']
list2= ['文德', '西門', '松山', '北投', '葫洲', '木柵', '芝山', '公館', '大湖公園', '大直', '關渡', '劍潭', '石牌', '圓山', '忠義', '松江南京', '雙連', '中山', '國父紀念館', '士林', '動物園', '劍潭', '唭哩岸', '大安森林公園', '象山', '行天宮', '中正紀念堂', '市政府', '動物園', '新北投', '關渡', '忠孝新生', '臺大醫院', '台北101／世貿', '龍山寺']
# Count occurrences of each item in the list
occurrences = Counter(list2)

# Print the occurrences
for item, count in occurrences.items():
    print(f"{item}: {count}")