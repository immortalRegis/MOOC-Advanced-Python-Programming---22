# WRITE YOUR SOLUTION HERE:
def begin_with_vowel(words: list):
    return [word for word in words if word[0] in "aeiou" or word[0] in 'AEIOU']