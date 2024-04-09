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
       counting_dict[n]= counting_list.count(n)  
    print(counting_dict)   # >>> {'宣': 2, '藍': 1}

    # 問題檢討：(1.)start_________________________________________________________________________
    # 這裏能找出最小值只是巧合，因為最小值在第一個n出現，後面較大值因此不會寫入dict。
    # 但是如果是呈現降序出現最小值，字典中會紀錄每一次最小值
    the_one_dict={}
    for n in counting_dict:
        min = counting_dict[n]
        for i in counting_dict:
            if counting_dict[i] < min:
                min = counting_dict[i]
                the_one_dict[i]= min # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!這裡有大問題
    print(the_one_dict)    # >>> {'藍': 1}
    # 問題檢討：(1.)end_________________________________________________________________________

    aaa = min(counting_dict,key=counting_dict.get)
    print(aaa)
    reverse_name_dict={y:x for (x,y) in name_dict.items()}  # >>> {'宣': '郭宣恆', '藍': '夏曼藍波安'}，重複的key會被洗掉，但是不影響我們只要抓出最unique的全名
    # print(the_one_dict.items())


    # 問題檢討：(2.) start_________________________________________________________________________
    # 上方問題一導致應該只有一個最小值的字典，出現多個值。
    # 但是這邊巧合的，最小值是最後一個 for loop中的元素，因此答案恰巧是正確的
    for keys, value in the_one_dict.items():
        print(keys)         # >>> !!!!!!!!!!!!!!!!!!!!!!!!!!!! 這裡可以有正確答案，是因為運氣好，key這變數被洗掉
        the_key = keys      # >>> 藍
    # 問題檢討：(2.)end_________________________________________________________________________

    try:
        print(reverse_name_dict[the_key])
    except UnboundLocalError:
        print("沒有")



# func("彭大牆", "陳王明雅", "吳明") # print 彭大牆
# func("郭靜雅", "王立強", "郭林靜宜", "郭立恆", "林花花") # print 林花花
func("大宣雅","一一一","郭宣雅", "林靜宜", "郭宣恆", "林靜花") # print 沒有
# func("郭宣雅", "夏曼藍波安", "郭宣恆") # print 夏曼藍波安