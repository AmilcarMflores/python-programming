word = "Hello"
letters1 = {c for c in word}
letters2 = set(c for c in word)
print(letters1) # {'o', 'H', 'e', 'l'}
print(letters1 == letters2) # True