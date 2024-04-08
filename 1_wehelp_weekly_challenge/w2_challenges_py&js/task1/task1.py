def find_and_print(messages, current_station):
    rebuild_messages_dict = {}
    list=[]
    for k in messages.values():
        for i in stations.keys():
            if i in k:
                list.append(stations[i])
    rebuild_messages_dict = dict(zip(messages.keys(), list))

    sta_num = stations[current_station]
    for n in rebuild_messages_dict:
        rebuild_messages_dict[n]

    print(rebuild_messages)


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
# Ｏ解決：處理捷運綠線，注意有分岔出去的小碧潭站
#       把小碧潭編列成3.2


# 合併成一個大檔案提供老師
# 可選擇，上現在網頁或是不