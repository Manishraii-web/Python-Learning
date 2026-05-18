# saved_password= "python123"
# entered_pwd = "python123"

# if entered_pwd == saved_password:
#     print("Access granted")
# else:
#     print("Wrong")

saved_password = "password123"
user_input = input("Enter your password: ")

if user_input == saved_password:
    print("Access granted.")
else:   
    print("Access denied. Incorrect password.") 
pin = 1234
attempts = 3
while attempts > 0:
    user_pin = int(input("Enter your PIN: "))
    if user_pin == pin:
        print("PIN accepted. Access granted.")
        break
    else:
        attempts -= 1
        print(f"Incorrect PIN. You have {attempts} attempts left.")
if attempts == 0:
    print("Too many incorrect attempts. Access denied.")