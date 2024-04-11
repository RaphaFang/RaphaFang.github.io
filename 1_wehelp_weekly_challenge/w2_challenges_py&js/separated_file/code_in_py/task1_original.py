def find_and_print(messages, current_station):  # >>> given current_station = "Wanlong"
    rebuild_messages_dict = {}
    message_loc_list=[]
    for k in messages.values():
        for i in stations.keys():
            if i in k:
                message_loc_list.append(stations[i])

    
    rebuild_messages_dict = dict(zip(messages.keys(), message_loc_list))  # >>> {'Leslie': 3.1, 'Bob': 12, 'Mary': 5, 'Copper': 17, 'Vivian': 1}
    # it contain a list and a dict, dict comprehension won't work

    relative_position_dict = {}
    current_station_num = stations[current_station]   # >>> 6
    position_list = [abs(current_station_num - rebuild_messages_dict[n]) for n in rebuild_messages_dict]
    #  >>>[2.9, 6, 1, 11, 5]
    
    relative_position_dict = dict(zip(position_list, messages.keys()))   
    # print(relative_position_dict)  # >>> {2.9: 'Leslie', 6: 'Bob', 1: 'Mary', 11: 'Copper', 5: 'Vivian'}

    min = position_list[0]
    for _ in position_list:
        if  _ < min:
            min = _
    print(relative_position_dict[min])

messages={
"Leslie":"I'm at home near Xiaobitan station.",
"Bob":"I'm at Ximen MRT station.",
"Mary":"I have a drink near Jingmei MRT station.",
"Copper":"I just saw a concert at Taipei Arena.",
"Vivian":"I'm at Xindian station waiting for you."
}
stations={"Songshan":19,"Nanjing Sanmin":18,"Taipei Arena":17,"Nanjing Fuxing":16,"Songjiang Nanjing":15,"Zhongshan":14,"Beimen":13,"Ximen":12,"Xiaonanmen":11,"Chiang Kai-Shek Memorial Hall":10,"Guting":9,"Taipower Building":8,"Gongguan":7,"Wanlong":6,"Jingmei":5,"Dapinglin":4,"Xiaobitan":3.1,"Qizhang":3,"Xindian City Hall":2,"Xindian":1
}

find_and_print(messages, "Wanlong") # print Mary
find_and_print(messages, "Songshan") # print Copper
find_and_print(messages, "Qizhang") # print Leslie
find_and_print(messages, "Ximen") # print Bob
find_and_print(messages, "Xindian City Hall") # print Vivian



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
# Ｏ解決：處理捷運綠線，注意有分岔出去的小碧潭站
#       把小碧潭編列成3.1

# terminal:--------------------------------------------------------------------
# Mary
# Copper
# Leslie
# Bob
# Vivian