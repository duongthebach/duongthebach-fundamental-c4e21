
print("a* x**2 + b * x + c = 0")
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

if a != 0:
    delta = b**2 - 4*a*c
    if delta > 0:
            print("phuong trinh co 2 nghiem")
            x1 = (-b + delta**0.5)/(2*a)
            x2 = (-b - delta**0.5)/(2*a)
            print("x1=", x1)
            print("x2=", x2)

    elif delta == 0:
            print("phuong trinh co 1 nghiem duy nhat")
            x = -b/(2*a)
            print("x=", x)
    else:
            print("phuong trinh vo nghiem")
else:
    print("phuong trinh co nghiem")
    x = -c/b
    print("x=", x) 

