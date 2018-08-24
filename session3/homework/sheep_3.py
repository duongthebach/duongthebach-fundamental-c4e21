sizes = [5, 7, 300, 90, 24, 50, 75]

print("Hello, my name is bach and these are my ship sizes: ")
print(sizes)

bigsize = max(sizes)

print("Now my biggest sheep has size", bigsize, "let's shear it")

default_sizes = sizes.index(bigsize)

sizes[default_sizes] = 8
print("After shearing, here is my flock")
print(sizes)
