person ={
    "name": "Bach",
    "age": 21,
    "city": "Ha noi",
}
# print(person)
while True:
    key = input("Your person:")
    if key in person:
        print(person[key])
    else:
        print("not found")
        update_key = input("your update?")
        update_value = input("expain:")
        person[update_key] = update_value
        print(person)