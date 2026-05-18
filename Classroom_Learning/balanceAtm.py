bank_blc= 52158
withdrawl = 2000

if(bank_blc>=withdrawl):
    print("you can withdrwal")
    withdrawing = bank_blc-withdrawl
    print("after withdrawing", withdrawing)
elif(bank_blc %100 == 0):
    print("atm only give multiple of hundred")
else:
    print("you cant invalid invalid")
