
import random
# library that we use in order to choose
# on random words from a list of words
 
name = input("What is your name? ")
 
# Here the user is asked to enter the name first
 
print("Good Luck ! ", name)
 
words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

word = random.choice(words)

k = -1
rights = ['*']*len(word)
guessed = ""
while rights.count('*')!= 0 and  k != 11:
    for i in guessed:
        if i in word:
            rights[word.index(i)] = i
    print("".join(rights))
    k += 1
    guess = input("input a character: ")
    while len(guess) != 1:
        guess = input("enter only one letter: ")
    guessed += guess
if k == 11:
    print("you lose")
    print ("the corresct word is " + word)
else:
    print("you win")
    
    