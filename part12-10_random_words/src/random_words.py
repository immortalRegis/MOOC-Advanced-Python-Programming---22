# Write your solution here:
import random
def word_generator(characters: str, length: int, amount: int):
    for i in range(amount):
        word = ''
        j = 0
        while(j < length):
            word += random.choice(characters)
            j += 1
        yield word
