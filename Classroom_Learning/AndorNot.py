# age = 25
# salary= 35000 
has_id = True

salary = int(input("Enter your Salary Monthly basis: "))
age = int(input("enter your age: too"))

eligible = (age>= 18) and (salary >= 25000) and has_id

if eligible:
    print("loaan is grnsted")
else:
    print("not elgibile for loan taking")

#why rejected
if not has_id:
    print("-> missing id document")
if salary < 25000:
   print("Gareeeb Salaaa")