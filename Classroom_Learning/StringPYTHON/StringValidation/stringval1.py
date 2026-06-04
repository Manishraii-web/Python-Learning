text = 'Hello World'

print(text.isalpha())  # False, because of space
print(text.isdigit())  # False, because it contains letters and space print(text.isalnum())  # False, because of space
print(text.islower())  # False, because of uppercase letters
print(text.isupper())  # False, because of lowercase letters
print(text.isspace())  # False, because it contains letters and space
print(text.startswith('Hello'))  # True
print(text.endswith('World'))  # True