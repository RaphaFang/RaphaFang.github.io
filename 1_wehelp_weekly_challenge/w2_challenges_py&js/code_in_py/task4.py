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