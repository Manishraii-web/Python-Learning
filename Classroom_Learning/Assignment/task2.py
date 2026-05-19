balance=5000
w_amount=2000
check1 = w_amount > 0 and w_amount<=balance
newbal= balance-w_amount
if check1:
    print (f"New Balance: {newbal}")
else:
    print("Insufficient balance")

if w_amount%100==0:
    print("atm only gives multiples of 100")
else:
    print("Not in 100")