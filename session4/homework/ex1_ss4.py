inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}
inventory['pocket'] = ['seashell', 'strange berry', 'lint']
print(inventory)
print()
lists = inventory['backpack']
lists.remove('dagger')
print(lists)
print()
inventory['gold'] += 50
print(inventory)


