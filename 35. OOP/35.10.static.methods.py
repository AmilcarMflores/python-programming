class Stringutil:
  @staticmethod
  def is_palindrome(s, case_insensitive=True):
    # Solo permitimos letras y números
    s = ''.join(c for c in s if c.isalnum())
    # Para una comparación que no distingue entre mayúsculas y minúsculas, escribimos s con minúscula.
    if case_insensitive:
      s = s.lower()
    for c in range(len(s) // 2):
      if s[c] != s[-c - 1]:
        return False
    return True
  @staticmethod
  def get_unique_words(sentence):
    return set(sentence.split())

print(
  Stringutil.is_palindrome('Radar', case_insensitive=False) 
) # False
print(Stringutil.is_palindrome("A nut for a jar of tuna")) # True
print(Stringutil.is_palindrome("Never odd, Or Even!")) # True
print(
  Stringutil.get_unique_words("I love palindromes. I really really love them!")
) # {'them!', 'love', 'really', 'I', 'palindromes.'}