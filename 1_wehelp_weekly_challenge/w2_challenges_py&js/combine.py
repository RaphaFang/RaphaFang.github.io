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

def get_price(ele):
    return ele["price"]

def get_rate(ele):
    return ele["rate"]

def book_hour_list(hour,duration):
    hour_list = []
    for b in range(hour,hour+duration):
        hour_list.append(b)
    return hour_list

def time_occupied_or_not_list(n, hour_list):
    occupied_list=[]
    for k in hour_list:
        if k in n["time"]:
            occupied_list.append(True)
        else:
            occupied_list.append(False)
    return any(occupied_list)

def print_name_and_break(n, hour, duration):
    for t in range(duration):
        n["time"].append(hour+t)
    n["time"].sort()
    print(n["name"])
    
def book(consultants, hour, duration, criteria):
    try:
        bool(consultants[0]["time"])
    except KeyError:
        for n in consultants:
            n["time"] = []    # >>> [{'name': 'John', 'rate': 4.5, 'price': 1000, 'time': []}, {'name': 'Bob', 'rate': 3, 'price': 1200, 'time': []}, {'name': 'Jenny', 'rate': 3.8, 'price': 800, 'time': []}]
    
    if criteria=="price":
        consultants.sort(key=get_price)
        count = 0
        for n in consultants:
            if time_occupied_or_not_list(n,book_hour_list(hour,duration)):
                count+=1
            else:
                print_name_and_break(n, hour, duration)
                break
        if count ==3:
            print("No Service")

    elif criteria=="rate":
        consultants.sort(key=get_rate)
        count = 0
        for n in consultants[::-1]:
            if time_occupied_or_not_list(n,book_hour_list(hour,duration)):
                count+=1
            else:
                print_name_and_break(n, hour, duration)
                break
        if count ==3:
            print("No Service")

consultants=[
{"name":"John", "rate":4.5, "price":1000,},
{"name":"Bob", "rate":3, "price":1200},
{"name":"Jenny", "rate":3.8, "price":800}
]


book(consultants, 15, 1, "price") # Jenny
book(consultants, 11, 2, "price") # Jenny
book(consultants, 10, 2, "price") # John
book(consultants, 20, 2, "rate") # John
book(consultants, 11, 1, "rate") # Bob
book(consultants, 11, 2, "rate") # No Service
book(consultants, 14, 3, "price") # John

# Jenny 11 12 15
# John 10 11 14 15 16 20 21
# Bob  11
# print(consultants)


# 條件順序：諮詢者名單順位、price/rate作為順序機制檢查空餘時間
# Ｘ錯誤：無法叫出這些list，且要考慮到func內部的資料在下次叫出時，可能不會存處
    # Ｏ解決：先設定三個list，以人名為key
    # Ｏ解決：將price/rate 各自建立list，透過dict.sort(key=['x'])，key是『函數』
    #       https://www.freecodecamp.org/chinese/news/python-sort-how-to-sort-a-list-in-python/
    #       注意，如果直接print(consultants.sort(key=get_price))，會得出none
    # Ｏ解決：反轉列印出rate list。Slicing Operator
    #       https://www.programiz.com/python-programming/methods/list/reverse
# Ｘ錯誤：還是需要透過外部txt
#       try:重新寫資料進去consultants dict內
# Ｏ解決：一小時持續時間的 or 2小時頭部沒重複但尾部重複，檢查條件是否滿足時，會有問題
#       透過any()解決
#       https://www.geeksforgeeks.org/python-any-function/
# Ｏ解決：斷開，滿足一次就離開（break、continue、pass）
#       https://medium.com/@chiayinchen/1-%E5%88%86%E9%90%98%E6%90%9E%E6%87%82-python-%E8%BF%B4%E5%9C%88%E6%8E%A7%E5%88%B6-break-continue-pass-be290cd1f9d8


# terminal:--------------------------------------------------------------------
# Jenny
# Jenny
# John
# John
# Bob
# No Service
# John

print("========task2 end========")

def func(*data):
    name_dict={}
    for n in data:   # >>> given func("郭宣雅", "夏曼藍波安", "郭宣恆") # print 夏曼藍波安
        if len(n) >= 4:
            name_dict[n] = list(n)[2]
        if len(n) <= 3:
            name_dict[n] = list(n)[1]   
    # print(name_dict)   # >>> {'郭宣雅': '宣', '夏曼藍波安': '藍', '郭宣恆': '宣'}

    counting_list = [n for n in name_dict.values()]  # >>> ['宣', '藍', '宣']
    counting_dict={k:counting_list.count(k) for k in counting_list }   # >>> {'宣': 2, '藍': 1}

    min_name = min(counting_dict.values())
    check_min_list =  [k for k in counting_dict if counting_dict.get(k) == min_name]   # >>> ['藍'] 若出現兩個最小，在下方會剔除

    reverse_name_dict={y:x for (x,y) in name_dict.items()}  # >>> {'宣': '郭宣恆', '藍': '夏曼藍波安'}，重複的key會被洗掉，但是不影響我們只要抓出最unique的全名
    if len(check_min_list) == 1:
        print(reverse_name_dict[check_min_list[0]])
    else:
        print("沒有")



func("彭大牆", "陳王明雅", "吳明") # print 彭大牆
func("郭靜雅", "王立強", "郭林靜宜", "郭立恆", "林花花") # print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花") # print 沒有
func("郭宣雅", "夏曼藍波安", "郭宣恆") # print 夏曼藍波安



# Ｏ解決：找出中間字，建立全名與中間字的dict
# Ｏ解決：計算數字，用count
#       https://www.programiz.com/python-programming/methods/list/count
# Ｏ解決：建立中間字為key的dict，values是字數
# 
# X錯誤：不能成功寫進一個最小value的字，先前成功是巧合
#       Ｏ解決：找出最少的字，獨自給一個dict
#       Ｏ解決：反轉name_dict，因為要透過keys，叫出原先全名
#       Ｏ解決：只叫出keys,沒有外加的括號
#           https://www.tutorialspoint.com/How-to-print-all-the-keys-of-a-dictionary-in-Python
# Ｏ解決：透過dict找最大最小值
#       https://zhuanlan.zhihu.com/p/440585003
# Ｏ解決：找到最小值，但是存在多個的情況？？
#       https://stackoverflow.com/questions/23967702/finding-max-value-in-a-dictionary-if-two-or-more-keys-have-same-values
# Ｏ解決：反轉name_dict，check_min_list為list，不需要解決叫出dict key的問題


# terminal:--------------------------------------------------------------------
# 彭大牆
# 林花花
# 沒有
# 夏曼藍波安

print("========task3 end========")

def get_number(index):
    tuple = divmod(index,3)
    print(tuple[0]*7 + tuple[1]*4)


get_number(1) # print 4
get_number(5) # print 15
get_number(10) # print 25
get_number(30) # print 70


# Ｏ解決：了解py除法如何運作
#       https://zoejoyuliao.medium.com/%E6%AF%94%E8%BC%83-python-%E7%9A%84-%E8%88%87-divmod-9f71786c0d33


# terminal:--------------------------------------------------------------------
# 4
# 15
# 25
# 70

print("========task4 end========")

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