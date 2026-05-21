income = float(input("Enter monthly income: "))
credit_score = int(input("Enter credit score: "))
debt = float(input("Enter existing debt: "))

if income > 100000 and credit_score > 750 and debt < 50000:
    print("Eligible for Premium Loan ")

elif income > 70000 and credit_score > 700 and debt < 100000:
    print("Eligible for Standard Loan ")

elif income > 40000 and credit_score > 650:
    print("Eligible for Basic Loan ")

else:
    print("Not Eligible for Loan ")