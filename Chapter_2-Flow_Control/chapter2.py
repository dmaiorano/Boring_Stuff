# Comparison Operators
# Numeric things
42 == 42 # True

42 == 99 # False

2 != 3 # True

2 != 2 # False

# Text
"hello" == "hello" # True

'hello' == 'Hello' # False

'dog' != 'cat' # True

True == True # True

True != False # True

42 == 42.0 # True

42 == '42' # False

# <, >, <=, >=
42 < 100 # True

42 > 100 # False

42 < 42 # False

eggCount = 42
eggCount <= 42 # True

myAge = 29
myAge >= 10 # True

# Remember that the == means that it's whether two equal each other
# The = operator assigns a variable to something

# Boolean Operators
# And
True and True # True
True and False # False
False and True # False
False and False # True

# Or
True or True # True
True or False # True
False or True # True
False or False # False

# Not - Operates to the opposite Boolean value
not True # False
not not not not True # True - T > F > T > F > T ends T

# Mixing the two
(4 < 5) and (5 < 6) # True - T and T = True

(4 < 5) and (9 < 6) # False - T and F = False

(1 == 2) or (2 == 2) # True - F or T = True

# Expressions
2 + 2 == 4 and not 2 + 2 == 5 and 2 * 2 == 2 + 2 # True

# Flow Control
# If statement
name = 'Alice'
if name == 'Alice':
    print('Name is ' + name)

# Else statement - what happens if false
if name == 'Alice':
    print('Name is ' + name)
else:
    print('Name is not ' + name)

# Elif - If you want many possible clausese to eecute. Provides another condition
# that is checked only if all of the previous conditions were false.
age = 10
if name == 'Alice':
    print('Hi, Alice')
elif age < 12:
    print('You are not Alice, kiddo')

# Something better
name = 'Carol'
age = 3000
if name == 'Alice':
    print('Hi, Alice')
elif age < 12:
    print('You are not Alice, kiddo')
elif age > 2000:
    print('Unlike you, Alice is not an undead, immortal vampire')
elif age > 100:
    print('You are not Alice, grannie')

# All 3 - If, Else, Elif
name = 'Carol'
age = 3000
if name == 'Alice':
    print('Hi, Alice')
elif age < 12:
    print('You are not Alice, kiddo')
else:
    print('You are neither Alice nor a little kid')

# While loops
# Until a condition is met things keep going

# Normal oops
spam = 0
if spam < 5:
    print('Hello, world.')
    spam = spam + 1

spam = 0
while spam < 5:
    print('Hello, world.')
    spam = spam + 1

# Break Statements
# Breaks you out of a loop, great for long lists or while loops
while True:
    print('Please type your name')
    name = input()
    if name == 'your name':
        break
print('Thank you!')

while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':
        continue
    print('Hello, Joe. What is the password? (It is a fish.)')
    password = input()
    if password == 'swordfish':
        break
print('Access granted.')

# Range stuff
print('My name is')
for i in range(5):
    print('Jimmy Five Times (' + str(i) + ')')

# More stuff
total = 0
for num in range(101):
    total = total + num
print(total)

for i in range(12, 16):
    print(i)

for i in range(0, 10, 2):
    print(i)

# Importing Modules
# Uses the import keyword and you can download extra ones or use the ones that
# are native to Python. Like Math or OS. These are downloaded with Python but 
# are not loaded off rip/when Python gets booted up.
import random
import secrets
for i in range(5):
    print(random.randint(1,10))

# Can also import multiple things at once
import random, os, math #etc

# Can also use the as keyword
import math as mt
import random as rn

# Ending program early
import sys
cnt = 0
while True:
    print('Type exit to exit.')
    response = input()
    if response == 'exit':
        sys.exit()
    print('You typed ' + response + '.')
    cnt += 1
    if cnt >= 10:
        break
    


# Fun little guessing game
# This is a guess the number game.
import random
secretNumber = random.randint(1,20)
print('I am thinking of a number between 1 and 20')
# Ask player to guess 6 times
for guessesTaken in range(1, 7):
    print('Take a guess')
    guess = int(input())
    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break # Condition is right, congrats
if guess == secretNumber:
    print('Good job! You guess my number in ' + str(guessesTaken) + 'guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))


# Rock paper scissors game Poggies
import random, sys

print('ROCK, PAPER, SCISSORS')

# These variables keep track of the number of wins, losses, and ties.
wins = 0
losses = 0
ties = 0

while True: # The main game loop.
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    while True: # The player input loop.
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        playerMove = input()
        if playerMove == 'q':
            sys.exit() # Quit the program.
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break # Break out of the player input loop.
        print('Type one of r, p, s, or q.')

    # Display what the player chose:
    if playerMove == 'r':
        print('ROCK versus...')
    elif playerMove == 'p':
        print('PAPER versus...')
    elif playerMove == 's':
        print('SCISSORS versus...')

    # Display what the computer chose:
    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computerMove = 'r'
        print('ROCK')
    elif randomNumber == 2:
        computerMove = 'p'
        print('PAPER')
    elif randomNumber == 3:
        computerMove = 's'
        print('SCISSORS')

    # Display and record the win/loss/tie:
    if playerMove == computerMove:
        print('It is a tie!')
        ties = ties + 1
    elif playerMove == 'r' and computerMove == 's':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'p' and computerMove == 'r':
        print('You win!')
        wins = wins + 1
    elif playerMove == 's' and computerMove == 'p':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'r' and computerMove == 'p':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 'p' and computerMove == 's':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 's' and computerMove == 'r':
        print('You lose!')
        losses = losses + 1
