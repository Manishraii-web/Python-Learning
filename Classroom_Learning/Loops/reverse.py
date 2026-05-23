#Take a sentense as input. Reverse each word individually, keep word order the same
sentence = input("Enter sentence: ")
words = sentence.split()
result = []

for word in words:
    rev = " "
    for char in range(len(word)-1, -1,-1):
        rev+=word[char]
        result.append(rev)

print(" ".join(result))