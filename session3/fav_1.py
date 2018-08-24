favs = ['netflix', 'teaching', 'rebull']
for i, item in enumerate(favs):
    print(i, item)
command = input("What you want (C, R, U, D)?")
while True:
    command = input("What you want (C, R, U, D)?").upper()
    if command == "C":
        you_fav = input("your favorite?")
        favs.append(you_fav)
        for i, item in enumerate(favs):
            print(i+1, "." ,item, sep="")   
    elif command == "R":
        for i, item in enumerate(favs):
            print(i +1, ".", item, sep="")
    elif command == "U":
        n = int(input("position you want update?"))
        you_update = input("you want update?")
        favs[n] = you_update
        for i, item in enumerate(favs):
            print(i +1, "." ,item, sep="")
    elif command == "D":
        you_delete = input("You want delete?")
        favs.remove(you_delete)
        for i, item in enumerate(favs):
            print(i +1, "." ,item, sep="")
    else:
        print("nah")



