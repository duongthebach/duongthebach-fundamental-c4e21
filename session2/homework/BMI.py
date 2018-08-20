height = int(input("your height(cm): "))
weight = int(input("your weight(kg): "))

BMI = weight/(height **2 /10000)
if BMI < 16:
    print("Severely underweight")
elif BMI <= 18.5:
    print("Underweight")
elif BMI <= 25:
    print("Norma")
elif BMI <=30:
    print("Overweight")
else:
    print("Obese")