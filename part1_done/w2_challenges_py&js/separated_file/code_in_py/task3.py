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