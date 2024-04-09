def find(spaces, stat, n):   # >>> given find([3, 1, 5, 4, 3, 2], [0, 1, 0, 1, 1, 1], 2) # print 5
    available = [spaces[i] if stat[i]>0 and spaces[i]>0 else 0 for i in range(len(spaces))]
    # print(available)   # >>> [0, 1, 0, 4, 3, 2]

    ava_minus_passenger_list=[]
    for k in available:
        ava_minus_passenger_list.append(k-n) 
    # print(ava_minus_passenger_list)  # >>> [-2, -1, -2, 2, 1, 0]
    
    fit = None
    for n in range(len(ava_minus_passenger_list)):
        for i in ava_minus_passenger_list:
            if ava_minus_passenger_list[n] >= 0 and ava_minus_passenger_list[n] < i:
                fit = n
    
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