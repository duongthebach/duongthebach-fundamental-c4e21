items = ['T-Shirt', 'Sweater']
for i, item in enumerate(items):
    print(i+1, ".", item)
# command = input("Welcome to our shopwhat you want (C, R, U, D)?")
loop = True
while loop:
    command = input("Welcome to our shop,what you want (C, R, U, D)?").upper()
    if command == "C":
        new_item = input("Enter your item:")
        items.append(new_item)
        for i, item in enumerate(items):
            print(i+1, "." ,item, sep="")   
    elif command == "R":
        for i, item in enumerate(items):
            print(i +1, ".", item, sep="")
    elif command == "U":
        n = int(input("update posision?"))
        update = input("new item?")
        items[n] = update
        for i, item in enumerate(items):
            print(i +1, "." ,item, sep="")
    elif command == "D":
        delete = input("delete posision?")
        items.remove(delete)
        for i, item in enumerate(items):
            print(i +1, "." , item, sep="")
    else:
        print("No item")
        loop = False