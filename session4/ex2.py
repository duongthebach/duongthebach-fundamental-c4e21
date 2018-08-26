from collections import OrderedDict

r1 = {
    "#": "1",
    "name": "A",
    "level": 222,
    "hour": 2,
}
r2 = {
    "#": "2",
    "name": "B",
    "level": 222,
    "hour": 2,
}
r3 = {
    "#": "3",
    "name": "C",
    "level": 222,
    "hour": 2,
}
salary_list = [r1, r2, r3]
total_wage = 0
wage_list = []
for salary in salary_list:
    name = salary["name"]
    hour = salary["hour"]
    level = salary["level"]
    wage = hour * level
    wage_info = OrderedDict({
        "name": name,
        "wage": wage,
    }) 
    wage_list.append(wage_info)
    total_wage += wage
    print(name, "'s wage:", wage)
print("Total name:", total_wage)
print(wage_list)
import pyexcel    
pyexcel.save_as(records=wage_list, dest_file_name="wage.xlsx")
