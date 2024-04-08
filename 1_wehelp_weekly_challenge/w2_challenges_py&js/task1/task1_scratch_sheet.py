# messages={
# "Leslie":"I'm at home near Xiaobitan station.",
# "Bob":"I'm at Ximen MRT station.",
# "Mary":"I have a drink near Jingmei MRT station.",
# "Copper":"I just saw a concert at Taipei Arena.",
# "Vivian":"I'm at Xindian station waiting for you."
# }


# for n in messages:
#     print(n)

# weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
# weather_f = {days:(f* 9/5) + 32 for (days, f) in weather_c.items()}

# print(weather_f)

# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# x = car.items()

# print(x)

# dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# # Put all keys of `dict1` in a list and returns the list
# print(dict1.keys())
# print(dict1.values())

# str = "I'm at Xindian station waiting for you."

# if str.startswith("I'm")== True:
#     print("Xindian")
# else:
#     print("nofound")


messages={
"Leslie":"I'm at home near Xiaobitan station.",
"Bob":"I'm at Ximen MRT station.",
"Mary":"I have a drink near Jingmei MRT station.",
"Copper":"I just saw a concert at Taipei Arena.",
"Vivian":"I'm at Xindian station waiting for you."
}
stations={"Songshan":19,"Nanjing Sanmin":18,"Taipei Arena":17,"Nanjing Fuxing":16,"Songjiang Nanjing":15,"Zhongshan":14,"Beimen":13,"Ximen":12,"Xiaonanmen":11,"Chiang Kai-Shek Memorial Hall":10,"Guting":9,"Taipower Building":8,"Gongguan":7,"Wanlong":6,"Jingmei":5,"Dapinglin":4,"Xiaobitan":3.1,"Qizhang":3,"Xindian City Hall":2,"Xindian":1}

rebuild_messages = {}
list=[]
for k in messages.values():
    for i in stations.keys():
        if i in k:
            list.append(stations[i])

# 0. 最初使用的方式，無法成功
# rebuild_messages = {}
# for k in messages.values():
#     for i in stations.keys():
#         if i in k:
#             rebuild_messages[messages.keys()]=stations[i]
#             print(stations[i])

# 1. dictionary comprehension   行不通，無法合併list & dict
# 出現問題：{'Leslie': 1, 'Bob': 1, 'Mary': 1, 'Copper': 1, 'Vivian': 1}
# for n in list:
#     for j in messages.keys():
        # rebuild_messages[j] = n
            # rebuild_messages={x: for (x,y) in messages.items()}
            # rebuild_messages[k]=stations[i]
            # print(stations[i])
# rebuild_messages = {x:a for (x,y) in messages.items() for a in list}


# 2. enumerate loop   行不通無法合併list & dict
# 出現問題：{'Leslie': 1, 'Bob': 1, 'Mary': 1, 'Copper': 1, 'Vivian': 1}
# for index, element1 in enumerate(list):
#     for index, element2 in enumerate(messages.keys()):
#         rebuild_messages[index] = element1

# 3. enumerate loop + comprehension  行不通無法合併list & dict
# 出現問題：{'Leslie': 1, 'Bob': 1, 'Mary': 1, 'Copper': 1, 'Vivian': 1}
# rebuild_messages = {index: element for index, element in enumerate(list)}
# for n in list:
#     for j in messages.keys():
        # rebuild_messages[j] = n
            
# 4. zip 大成功！！
rebuild_messages = dict(zip(messages.keys(), list))

# print(list)
# print(rebuild_messages)
for n in rebuild_messages:
    print(rebuild_messages[n])