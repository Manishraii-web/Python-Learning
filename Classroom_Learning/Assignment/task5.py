totalBill = 3750.00
num_people = 5
paid_extra = True
discount_Percent = 10
your_name = "Sachin"

discount = totalBill * (discount_Percent/100)

eachPersonShare = discount / num_people

print (f"After Discount : {discount}\nEachShare : {eachPersonShare}")
print(type(discount))
print(type(eachPersonShare))