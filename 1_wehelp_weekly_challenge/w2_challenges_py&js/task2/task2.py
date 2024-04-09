def get_price(ele):
    return ele["price"]
def get_rate(ele):
    return ele["rate"]
def book(consultants, hour, duration, criteria):
    try:
        bool(consultants[0]["time"])
    except KeyError:
        for n in consultants:
            n["time"] = []    # >>> [{'name': 'John', 'rate': 4.5, 'price': 1000, 'time': []}, {'name': 'Bob', 'rate': 3, 'price': 1200, 'time': []}, {'name': 'Jenny', 'rate': 3.8, 'price': 800, 'time': []}]
        
    if criteria=="price":
        consultants.sort(key=get_price)
        # print(consultants)
        count = 0
        for n in consultants:
            if hour and hour+duration-1 not in n["time"]:
                for t in range(duration):
                    n["time"].append(hour+t)
                n["time"].sort()
                break
            else:
                count+=1
        # print(count)
        if count ==3:
            print("No Service")

    elif criteria=="rate":
        consultants.sort(key=get_rate)
        print(consultants)
        # print(consultants)
        count = 0
        for n in consultants[::-1]:
            for l in [k for k in range(hour, hour+duration)]:
                if l not in n["time"]:
                    for t in range(duration):
                        n["time"].append(hour+t)
                    n["time"].sort()
                    break
                else:
                    count+=1
        print(count)
        if count ==3:
            print("No Service")

consultants=[
{"name":"John", "rate":4.5, "price":1000,},
{"name":"Bob", "rate":3, "price":1200},
{"name":"Jenny", "rate":3.8, "price":800}
]


# Jenny 11 12 15
# John 10 11 14 15 16 20 21
# Bob  11
book(consultants, 15, 1, "price") # Jenny
book(consultants, 11, 2, "price") # Jenny
book(consultants, 10, 2, "price") # John
book(consultants, 20, 2, "rate") # John
book(consultants, 11, 1, "rate") # Bob
book(consultants, 11, 2, "rate") # No Service
# book(consultants, 14, 3, "price") # John

print(consultants)


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
# 一小時持續時間的，編寫進入字典會有問題