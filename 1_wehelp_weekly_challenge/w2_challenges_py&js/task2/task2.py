def get_price(element):
    return element["price"]
def get_rate(ele):
    return ele["rate"]

# def book(consultants, hour, duration, criteria):
#     Jenny_dict=[]
#     Bob_dict=[]
#     Jenny_dict=[]

    # price_order = 
    
        

consultants=[
{"name":"John", "rate":4.5, "price":1000},
{"name":"Bob", "rate":3, "price":1200},
{"name":"Jenny", "rate":3.8, "price":800}
]
# price_order_dict ={p["name"]:p["price"] for p in consultants}
# rate_order_dict ={r["name"]:r["rate"] for r in consultants}
# price_order = [p for p in price_order_dict.sort(key=get_price)]


consultants.sort(key=get_price)
print(consultants)

# book(consultants, 15, 1, "price") # Jenny
# book(consultants, 11, 2, "price") # Jenny
# book(consultants, 10, 2, "price") # John
# book(consultants, 20, 2, "rate") # John
# book(consultants, 11, 1, "rate") # Bob
# book(consultants, 11, 2, "rate") # No Service
# book(consultants, 14, 3, "price") # John



# 條件順序：諮詢者名單順位、price/rate作為順序機制檢查空餘時間
# Ｏ解決：先設定三個list，以人名為key
# 將price/rate 各自建立list
# 注意，如果直接print(consultants.sort(key=get_price))，會得出none