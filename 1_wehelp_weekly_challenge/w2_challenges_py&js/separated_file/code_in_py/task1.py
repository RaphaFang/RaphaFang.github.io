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

print("========task1 end========")

def find(spaces, stat, n):   # >>> given find([3, 1, 5, 4, 3, 2], [0, 1, 0, 1, 1, 1], 2) # print 5
    available = [spaces[i] if stat[i]>0 and spaces[i]>0 else 0 for i in range(len(spaces))]
    # print(available)   # >>> [0, 1, 0, 4, 3, 2]

    ava_minus_passenger_list = [k-n for k in available]
    # print(ava_minus_passenger_list)  # >>> [-2, -1, -2, 2, 1, 0]
        
    fit = None
    for n in range(len(ava_minus_passenger_list)):
        for i in ava_minus_passenger_list:
            if ava_minus_passenger_list[n] >= 0 and ava_minus_passenger_list[n] < i:
                fit = n
    # print(fit)   # >>> 5 / None / 2
    
    if str(fit).isnumeric():
        print(fit)
    else:
        print(-1)

find([3, 1, 5, 4, 3, 2], [0, 1, 0, 1, 1, 1], 2) # print 5  [0, 1, 0, 4, 3, 2]
find([1, 0, 5, 1, 3], [0, 1, 0, 1, 1], 4) # print -1  [0, 0, 0, 1, 3]
find([4, 6, 5, 8], [0, 1, 1, 1], 4) # print 2 [0, 6, 5, 8]



# Ｏ解決：處理兩個list合併問題
#       注意range 的計算是從 0 開始到 n-1
#       處理兩個list合併的 comprehension， if else
#       https://www.geeksforgeeks.org/python-list-comprehension-using-if-else/
# Ｘ錯誤：寫一個dict，處理index對應數值
#       沒必要這麼複雜，因為只是指數，透過list更快
        # index_dict={n:ava_minus_passenger_list[n] for n in range(len(ava_minus_passenger_list))}
# Ｏ解決：須滿足條件：>=0 and >=0數值裡最小的
# Ｏ解決：透過字典呼叫指數的index?或是list？
#       發現用list可以更快的比大小，可以略過max/min功能，但情況是"keys"只是指數，若是第3題的字，則須要透過dict
# Ｏ解決：解決是否為數字？
#       https://www.toppr.com/guides/python-guide/references/methods-and-functions/methods/string/isnumeric/python-string-isnumeric/


# terminal:--------------------------------------------------------------------
# 5
# -1
# 2

print("========task5 end========")