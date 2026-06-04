def analyze_text(text):
    #analyxe a given text and return some statistics

     clean = text.strip().lower()
     words = clean.split()
     chars = [ c for c in clean if c.isalpha()]
     vowels = [c for c in chars if c in 'aeiou']
     sentences = text.split('.')

# word frequency
     freq = (w: words.count(w) for w in set(words))
     top3 = sorted(freq, key= lambda w: freq[w], reverse=True)[:3]

     return {
          "total_chars" :len(text),
          "total_words" : len(words),
          "unique_words" :len(set(words)),
          "total_sentencs" : len([s for s in sentences if s.string()]),
          "vowels" : len(vowels),
          "top3_words" : top3,
          "is_all_lowe" : text == text.lower()
     }