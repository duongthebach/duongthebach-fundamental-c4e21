sizes = [5, 7, 300, 90, 24, 50, 75]

print("Hello, my name is bach and these are my ship sizes: ")
print(sizes)

month = 4 

for i in range(month):
    print("Month", i+1, ":")
    print("One month has passed, now here is my flock")
    sizes =[size + 50 for size in sizes]
    print(sizes)
    big_size = max(sizes)
    print("Now my biggest sheep has size", big_size, "let's shear it ")
    default_sizes = sizes.index(big_size)

    sizes[default_sizes] = 8
    print("After shearing, here is my flock")
    print(sizes)
    print()
total = sum(sizes)
A = total * 2
print("My flock has size in total:", total)
print("I would get", total, "*", 2,"$", "=", A, "$", end ="" )