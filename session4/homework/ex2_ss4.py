prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3,
}
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15,
}

total_money = 0
for key in prices:
    print(key)
    a = prices[key]
    b = stock[key]
    print("price", ":", a)
    print("stock", ":", b)
    total = a * b
    print(total)
    total_money += total
    print()  
print("total: ", total_money)