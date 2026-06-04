# lambda for string transformation

upper = lambda s: s.upper()
print(upper('manish sammaaaaaaa'))

#sorting strings by length
words = ['apple','banana','ciwi','dickhead']
words.sort(key=lambda w: len(w))
print(words)

#using map() with  lambda to transform a list of strings
names = ['Alice', 'Bob', 'Charlie']
titled = list(map(lambda n: n.title(), names))
print(titled)

# filter words longer than 5 characters
long_words = list(filter(lambda w: len(w) > 5, words))
print(long_words)

