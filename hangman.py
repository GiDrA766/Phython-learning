import random
from collections import Counter

print("starting game of Hangman")
fruits = ["mango", "papaya", "dragonfruit", "starfruit", "acai berry", "kiwano", "rambutan", "durian", "lychee", "feijoa", "pineapple", "coconut", "avocado", "banana", "pomegranate", "peach", "grapefruit", "grape", "kiwi", "mandarin orange", "lemon", "lime", "orange", "pear", "strawberry", "blueberry", "raspberry", "blackberry", "cherry", "pomelo", "watermelon"]
word = random.choice(fruits)
guessedletters = ""
count = len(word) *1.5
trueans = ['*']*len(word)
while trueans.count('*') != 0 and count > 0:
    guess = input("write a letter: ")
    while len(guess) != 1 or not(guess.isalpha())  or (guess in guessedletters):
        guess = input("write only one letter in alphabetic that doesnt entered previously")
    guessedletters += guess
    for char  in range(len(word)):
        if word[char] in guessedletters:
            trueans[char] = word[char]
    print("".join(trueans))
    count -= 1

if count == 0:
    print("you losed") 
    print("correct answer was " + word)
else:
    print("you won")
    print("word is " + word)
    