menu_drinks = ["Coca", "Fanta", "Beer"]
menu_size = len(menu_drinks)
for i in range(menu_size):
    print(i+1,".", menu_drinks[i], sep="")
n = int(input("posion you want to update?"))
your_fav = input("Your replacing favorite?")
menu_drinks[n] = your_fav
for index, item in enumerate(menu_drinks):
    print(index + 1, ".", item)

