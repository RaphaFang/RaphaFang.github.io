from itertools import groupby
import urllib.request as request
import json

src1 = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1"
src2 = 'https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-2'

with request.urlopen(src1) as response:
    data1 = json.load(response)
with request.urlopen(src2) as response:
    data2 = json.load(response)

# Your original list
station = [n['MRT'] for n in data2["data"]]
print(station)
print(len(station))

list = station
# Using groupby to remove consecutive duplicates
result = [key for key, group in groupby(list)]
print(result)
print(len(result) )# Output: [1, 2, 3]

for n in station:
    if station.count(n)!=1:
        station.remove(n)  # >>>  處理station list串中重複出現
print(station)
print(len(station))