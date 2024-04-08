def find_and_print(messages, current_station):
    rebuild_messages_dict = {}
    message_loc_list=[]
    for k in messages.values():
        for i in stations.keys():
            if i in k:
                message_loc_list.append(stations[i])
    rebuild_messages_dict = dict(zip(messages.keys(), message_loc_list))  # >>> {'Leslie': 3.1, 'Bob': 12, 'Mary': 5, 'Copper': 17, 'Vivian': 1}

    relative_position_dict = {}
    position_list=[]
    current_station_num = stations[current_station]   # >>> 6
    for n in rebuild_messages_dict:
        position_list.append(abs(current_station_num - rebuild_messages_dict[n]))  # >>>[2.9, 6, 1, 11, 5]
    relative_position_dict = dict(zip(messages.keys(), position_list))   # >>> {'Leslie': 2.9, 'Bob': 6, 'Mary': 1, 'Copper': 11, 'Vivian': 5}
        
    
def findMax(nums):
    max = nums[0]
    for _ in nums:
        if  _ > max:
            max = _
    return max
        
nums = [0]
# nums = []
findMax(nums)


messages={
"Leslie":"I'm at home near Xiaobitan station.",
"Bob":"I'm at Ximen MRT station.",
"Mary":"I have a drink near Jingmei MRT station.",
"Copper":"I just saw a concert at Taipei Arena.",
"Vivian":"I'm at Xindian station waiting for you."
}
stations={"Songshan":19,"Nanjing Sanmin":18,"Taipei Arena":17,"Nanjing Fuxing":16,"Songjiang Nanjing":15,"Zhongshan":14,"Beimen":13,"Ximen":12,"Xiaonanmen":11,"Chiang Kai-Shek Memorial Hall":10,"Guting":9,"Taipower Building":8,"Gongguan":7,"Wanlong":6,"Jingmei":5,"Dapinglin":4,"Xiaobitan":3.1,"Qizhang":3,"Xindian City Hall":2,"Xindian":1
}



find_and_print(messages, "Wanlong") 

print("====Task1 in py====")



# 找到我車站的數值(dict, 站名:數值)、檢查messages中（編譯dict, 數值:人名）、

# Ｏ解決：讀取json。實際上是dict了
# Ｏ解決：處理捷運站序列，綠線
#       key, para 要寫正確順序
# Ｏ解決：處理給定站名，回報順序
# Ｏ解決：處理messages找字串的功能。
#       不是用 find 而是用 in
#       dict comprehensive :
#       https://ithelp.ithome.com.tw/articles/10203788
#       https://www.udemy.com/course/100-days-of-code/learn/lecture/20763744#overview
#       https://www.datacamp.com/tutorial/python-dictionary-comprehension
# Ｏ解決：處理讀字典的功能，並且重新編寫
#       透過map功能解決
#       https://www.atatus.com/blog/python-converting-lsts-to-dictionaries/
# 處理捷運斬「尋找」功能
#       絕對值：
#       https://runoob.com/python/func-number-abs.html
# Ｏ解決：處理捷運綠線，注意有分岔出去的小碧潭站
#       把小碧潭編列成3.2


# 合併成一個大檔案提供老師
# 可選擇，上現在網頁或是不