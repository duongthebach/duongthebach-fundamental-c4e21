menu_items = ['Pho ga', 'Com rang', 'My xao', 'Bun bo']
for index, item in enumerate(menu_items):
    print(index + 1, ".", item)
n = int(input("Favorite position you want to get rid of?"))
menu_items.pop(n -1)
for index, item in enumerate(menu_items):
    print(index + 1, ".", item)