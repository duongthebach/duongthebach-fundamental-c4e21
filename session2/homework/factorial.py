n = int(input("enter number:"))
factorial = 1
for i in range(1,n+1):
    factorial *= i
print(str(n) + "! =", factorial)