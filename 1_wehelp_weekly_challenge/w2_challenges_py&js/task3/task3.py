def func(*data):
    name_dict={}
    for n in data:   # >>> given func("郭宣雅", "夏曼藍波安", "郭宣恆") # print 夏曼藍波安
        if len(n) >= 4:
            name_dict[n] = list(n)[2]
        if len(n) == 3 or len(n) == 2:
            name_dict[n] = list(n)[1]   
    # print(name_dict)   # >>> {'郭宣雅': '宣', '夏曼藍波安': '藍', '郭宣恆': '宣'}

    counting_dict={}
    counting_list = [n for n in name_dict.values()]  # >>> ['宣', '藍', '宣']
    for n in counting_list:
       counting_dict[n]= counting_list.count(n)  # >>> {'宣': 2, '藍': 1}

    the_one_dict={}
    for n in counting_dict:
        min = counting_dict[n]
        for i in counting_dict:
            if counting_dict[i] < min:
                min = counting_dict[i]
                the_one_dict[i]= min
    # print(the_one_dict)    # >>> {'藍': 1}

    reverse_name_dict={y:x for (x,y) in name_dict.items()}  # >>> {'宣': '郭宣恆', '藍': '夏曼藍波安'}，重複的key會被洗掉，但是不影響我們只要抓出最unique的全名
    # print(the_one_dict.items())

    for keys, value in the_one_dict.items():
        the_key = keys      # >>> 藍

    try:
        print(reverse_name_dict[the_key])
    except UnboundLocalError:
        print("沒有")



# func("彭大牆", "陳王明雅", "吳明") # print 彭大牆
# func("郭靜雅", "王立強", "郭林靜宜", "郭立恆", "林花花") # print 林花花
# func("郭宣雅", "林靜宜", "郭宣恆", "林靜花") # print 沒有
func("郭宣雅", "夏曼藍波安", "郭宣恆") # print 夏曼藍波安



# Ｏ解決：找出中間字，建立全名與中間字的dict
# Ｏ解決：計算數字，用count
#       https://www.programiz.com/python-programming/methods/list/count
# Ｏ解決：建立中間字為key的dict，values是字數
# Ｏ解決：找出最少的字，獨自給一個dict
# Ｏ解決：反轉name_dict，因為要透過keys，叫出原先全名
# Ｏ解決：只叫出keys,沒有外加的括號
#       https://www.tutorialspoint.com/How-to-print-all-the-keys-of-a-dictionary-in-Python