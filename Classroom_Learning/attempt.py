pin = "1234"
attempt = 3

while attempt > 0:
    user_inp = input("Enter PIN: ")

    if user_inp == pin:
        print("Welcome sama")
        break
    else:
        attempt -= 1
        print("Enter again")

if attempt == 0:
    print("Too many incorrect attempts. Access denied.")