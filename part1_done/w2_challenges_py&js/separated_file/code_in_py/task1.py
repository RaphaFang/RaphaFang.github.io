def find_and_print(messages, current_station):  # >>> given current_station = "Wanlong"
    stations=["Songshan","Nanjing Sanmin","Taipei Arena","Nanjing Fuxing","Songjiang Nanjing","Zhongshan","Beimen","Ximen","Xiaonanmen","Chiang Kai-Shek Memorial Hall","Guting","Taipower Building","Gongguan","Wanlong","Jingmei","Dapinglin","Xiaobitan","Qizhang","Xindian City Hall","Xindian"]

    message_sta_list=[]
    for k in messages.values():
        for i in stations:
            if i in k:
                message_sta_list.append(i)  # >>> ['Xiaobitan', 'Ximen', 'Jingmei', 'Taipei Arena', 'Xindian']
    message_sta_dict = dict(zip(messages.keys(), message_sta_list))  # >>> {'Leslie': 'Xiaobitan', 'Bob': 'Ximen', 'Mary': 'Jingmei', 'Copper': 'Taipei Arena', 'Vivian': 'Xindian'}

    stations_without_Xiaobitan=["Songshan","Nanjing Sanmin","Taipei Arena","Nanjing Fuxing","Songjiang Nanjing","Zhongshan","Beimen","Ximen","Xiaonanmen","Chiang Kai-Shek Memorial Hall","Guting","Taipower Building","Gongguan","Wanlong","Jingmei","Dapinglin","Qizhang","Xindian City Hall","Xindian"]

    if current_station != 'Xiaobitan':
        fix = stations_without_Xiaobitan.index(current_station)
        message_sta_index_dict = {}
        for n in message_sta_dict:
            if message_sta_dict[n]=="Xiaobitan":
                message_sta_index_dict[n]= abs(fix-stations_without_Xiaobitan.index("Qizhang"))+1
            else:
                absolute_loc = stations_without_Xiaobitan.index(message_sta_dict[n])
                relative_loc = abs(fix-absolute_loc)
                message_sta_index_dict[n]=relative_loc
    else:
        fix = stations_without_Xiaobitan.index("Qizhang")
        message_sta_index_dict = {}
        for n in message_sta_dict:
            if message_sta_dict[n]=="Xiaobitan":
                message_sta_index_dict[n]= 0
            else:
                absolute_loc = stations_without_Xiaobitan.index(message_sta_dict[n])
                relative_loc = abs(fix-absolute_loc) +1
                message_sta_index_dict[n]=relative_loc
    # print(message_sta_index_dict)     # >>>{'Leslie': 4, 'Bob': 6, 'Mary': 1, 'Copper': 11, 'Vivian': 5}

    person = min(message_sta_index_dict, key=message_sta_index_dict.get)
    print(person)

messages={
"Leslie":"I'm at home near Xiaobitan station.",
"Bob":"I'm at Ximen MRT station.",
"Mary":"I have a drink near Jingmei MRT station.",
"Copper":"I just saw a concert at Taipei Arena.",
"Vivian":"I'm at Xindian station waiting for you."
}

find_and_print(messages, "Wanlong") # print Mary
find_and_print(messages, "Songshan") # print Copper
find_and_print(messages, "Qizhang") # print Leslie
find_and_print(messages, "Ximen") # print Bob
find_and_print(messages, "Xindian City Hall") # print Vivian

find_and_print(messages, "Dapinglin")  # print Mary 


# 找到我車站的數值(dict, 站名:數值)、檢查messages中（編譯dict, 數值:人名）、
# Ｏ解決：讀取json。實際上是dict了
# Ｏ解決：處理捷運站序列，綠線，存粹打字處理
# Ｏ解決：處理給定站名，回報順序
#       key, para 要寫正確順序
# Ｏ解決：處理messages找字串的功能。
#       不是用 find 而是用 in
#       dict comprehensive :
#       https://ithelp.ithome.com.tw/articles/10203788
#       https://www.udemy.com/course/100-days-of-code/learn/lecture/20763744#overview
#       https://www.datacamp.com/tutorial/python-dictionary-comprehension
# Ｏ解決：處理讀字典的功能，並且重新編寫
#       透過map、zip功能解決
#       https://www.atatus.com/blog/python-converting-lsts-to-dictionaries/
# Ｏ解決：處理捷運站距離比較功能
#       絕對值：
#       https://runoob.com/python/func-number-abs.html
#       最大最小：
#       透過先前wehelp code的紀錄
# Ｘ錯誤：處理捷運綠線，注意有分岔出去的小碧潭站
#       把小碧潭編列成3.1

# terminal:--------------------------------------------------------------------
# Mary
# Copper
# Leslie
# Bob
# Vivian
# Mary 

print("========task1 end========")