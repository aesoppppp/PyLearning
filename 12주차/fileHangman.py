import random

guesses = ''
turns = 10

f = open("words.txt", "r", encoding='UTF-8')
lines = f.readlines()
word = random.choice(lines)

while turns > 10:
    failed = 0
    for char in guesses:
        if char in guesses:
            print(char, end=)
