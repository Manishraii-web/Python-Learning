price =500
qty = 3
budget = 1800

total = price * qty  #arithmetic
can_affort = total <= budget  #comparision
has_stock =qty> 0    #comparision

can_buy= can_affort and has_stock  #logical

print("total cost", total)
print("affortable", can_affort)
print("has stock ", has_stock)
print("can buy ", can_buy)
