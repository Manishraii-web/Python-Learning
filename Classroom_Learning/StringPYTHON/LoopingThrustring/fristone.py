text = "Hello, World!"
# for loop
for ch in text:
    print(ch, end=' ')

#enum
for i , ch in enumerate(text):
    print(f"{i}: {ch}", end=' ')

#comprehension
vowels = [ch for ch in text if ch in 'aeiouAEIOU']
print("\nVowels in the text:", vowels)