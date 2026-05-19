name = input("Enter your name: ")
age = int(input("Enter your age: "))
citizen = input("Are you a citizen? (yes/no): ")

if age >= 18 and citizen.lower() == "yes":
    print("Eligible to vote")
elif age >= 18 and citizen.lower() == "no":
    print("Not Eligible to vote (Not a citizen)")
else:
    print("Too Young to vote")