def find(spaces, stat, n):   # >>> given find([3, 1, 5, 4, 3, 2], [0, 1, 0, 1, 1, 1], 2) # print 5
    available = [spaces[i] if stat[i]>0 and spaces[i]>0 else 0 for i in range(len(spaces))]
    # print(available)   # >>> [0, 1, 0, 4, 3, 2]

    index_list=[]
    for k in available:
        index_list.append(k-n) 
    # print(index_list)  # >>> [-2, -1, -2, 2, 1, 0]
    
    index_dict={n:index_list[n] for n in range(len(index_list))}
    print(index_dict)   # >>> {0: -2, 1: -1, 2: -2, 3: 2, 4: 1, 5: 0;}

    the_one_dict={}
    for n in index_dict:
        most_fitted = index_dict[n]
        for i in index_dict:
            if index_dict[i] >=0 and index_dict[i] < most_fitted:
                most_fitted = index_dict[i]
    print(most_fitted)

    # print(the_one_dict)

    # 嘗試sand box的方式


find([3, 1, 5, 4, 3, 2], [0, 1, 0, 1, 1, 1], 2) # print 5  [0, 1, 0, 4, 3, 2]
find([1, 0, 5, 1, 3], [0, 1, 0, 1, 1], 4) # print -1  [0, 0, 0, 1, 3]
find([4, 6, 5, 8], [0, 1, 1, 1], 4) # print 2 [0, 6, 5, 8]



# Ｏ解決：處理兩個list合併問題
#       注意range 的計算是從 0 開始到 n-1
# 寫一個dict，處理index對應數值
# 須滿足條件：>=0 and >=0數值裡最小的