# your code here, maybe
def book(consultants, hour, duration, criteria):
    pass
consultants=[
{"name":"John", "rate":4.5, "price":1000},
{"name":"Bob", "rate":3, "price":1200},
{"name":"Jenny", "rate":3.8, "price":800}
]



# book(consultants, 15, 1, "price") # Jenny
# book(consultants, 11, 2, "price") # Jenny
# book(consultants, 10, 2, "price") # John
# book(consultants, 20, 2, "rate") # John
# book(consultants, 11, 1, "rate") # Bob
# book(consultants, 11, 2, "rate") # No Service
# book(consultants, 14, 3, "price") # John


# 順位上：諮詢者敲定的時間、諮詢者時長、諮詢者評分or價格偏好
# 先設定三個字典