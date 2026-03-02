import random
number = random.randint(1, 100)
attempts = 0
print("Welcome to Number Guessing Game")
print("Guess a number between 1 and 100")
while True:
    guess=int(input("Enter the number: "))
    attempts+=1
    if(guess>number):
        print("Too Long")
    elif(guess<number):
        print("Too Short")
    else:
        print("Correct! You guessed the number in", attempts, "attempts.")
        break
