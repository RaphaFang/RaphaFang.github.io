Jenny=[]
Bob=[]
Jenny=[]



def get_price(ele):
    return ele["price"]
def get_rate(ele):
    return ele["rate"]
def return_list(ele):
    consultants.sort(key=ele)
    return  [p['name'] for p in consultants]

def book(consultants, hour, duration, criteria):
    available_time_dict = {}
    price_order_list = return_list(get_price)
    rate_order_list = return_list(get_rate)[::-1]

    if criteria=="price":
        pass
        for n in price_order_list:
            print(type(n))
            # if str(hour) not in n:
            #     n.append(hour)
            #     print(n)
            #     return
    else:
        pass




    
        

consultants=[
{"name":"John", "rate":4.5, "price":1000},
{"name":"Bob", "rate":3, "price":1200},
{"name":"Jenny", "rate":3.8, "price":800}
]



# print(consultants)

book(consultants, 15, 1, "price") # Jenny
# book(consultants, 11, 2, "price") # Jenny
# book(consultants, 10, 2, "price") # John
# book(consultants, 20, 2, "rate") # John
# book(consultants, 11, 1, "rate") # Bob
# book(consultants, 11, 2, "rate") # No Service
# book(consultants, 14, 3, "price") # John



# 條件順序：諮詢者名單順位、price/rate作為順序機制檢查空餘時間
# Ｘ錯誤：無法叫出這些list，且要考慮到func內部的資料在下次叫出時，可能不會存處
    # Ｏ解決：先設定三個list，以人名為key
    # Ｏ解決：將price/rate 各自建立list，透過dict.sort(key=['x'])，key是『函數』
    #       https://www.freecodecamp.org/chinese/news/python-sort-how-to-sort-a-list-in-python/
    #       注意，如果直接print(consultants.sort(key=get_price))，會得出none
    # Ｏ解決：反轉列印出rate list。Slicing Operator
    #       https://www.programiz.com/python-programming/methods/list/reverse