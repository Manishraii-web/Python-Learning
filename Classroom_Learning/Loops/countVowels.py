#COunt the total number if vowels(a,e,i,o,u) in a user entered text
sentence = input("Enter ssentence")
count = 0
vowels = "aeiou"
for char in  sentence:
    if char in  vowels:
        count += 1
print("Vowels: ", count)