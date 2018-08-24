menu_items = ['Pho ga', 'Com rang', 'My xao', 'Bun bo']
for index, item in enumerate(menu_items):
    print(index + 1, ".", item)

delete_item = input("delete item:")
if delete_item in menu_items:
    menu_items.remove(delete_item)
else:
    print("nah")
menu_items.remove(delete_item)
for index, item in enumerate(menu_items):
    print(index + 1, ".", item)