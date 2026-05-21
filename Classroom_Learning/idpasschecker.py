username="Manish"
password="1123"
un = input("Enter Username: ")
pw = input("Enter Password: ")

if un == username and pw == password:
    print("Successfull login")
elif un == username and pw != password:
    print("Incorrect Password")
else:
    print("User not found")