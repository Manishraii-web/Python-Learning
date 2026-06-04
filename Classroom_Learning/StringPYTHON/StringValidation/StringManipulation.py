text = "Manish , Sama"

# 1 Clean and m=normalize

clean = text.strip().lower()
print(clean)  # Output: "manish , sama"     

# 2 Replace and split
replaced = clean.replace(",", "").split()
print(replaced)  # Output: "manish  sama"

#3.Reversed
reversed_text = clean[::-1]
print(reversed_text)  # Output: "amas , hsinaM"

