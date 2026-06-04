import re
#NLP preprocessing pipeline
text = 'Hello, VIlLIain SAMA'

#step 1 normalize
text = text.lower().strip()

#steop2 remove punctuation
text = re.sub(r'[^\w\s]', '', text)
 
 #step 3 tokenization
tokens = text.split()

#step 4 : remove stop words
stop_words = set(['the', 'is', 'in', 'and', 'to', 'a'])
filtered_tokens = [t for t in tokens if t not in stop_words]

print(filtered_tokens)
