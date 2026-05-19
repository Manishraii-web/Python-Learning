name = input("Enter name: ")
weight = float(input("Enter weight: "))
height = float(input("Enter Height: "))
BMI = weight/(height*height)

if BMI<18.5:
   category = print("Underweight")
elif BMI>=18.5 and BMI <=24.9:
    category =print("Normal")
elif BMI>=25 and BMI <=29.9:
    category =print("OverWeight")
else:
    category =print("Obese")

print(f"Hi {name}! BMI :{BMI} Category: {category}")