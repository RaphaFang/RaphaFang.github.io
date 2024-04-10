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