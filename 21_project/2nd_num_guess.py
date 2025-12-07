import random

print("Welcome to my Number guessing game")

play = input("Do you want to play?(y/n) ")

if play != 'y':
    quit()


print("Let's Play")
number = random.randint(1,100)
while True:
    guess = input("Guess the number between 1 and 100: ")
    if int(guess) == number:
        print("Correct Guess")
        quit()
    elif int(guess) < number:
        print(f"Your guess is low")
    elif int(guess) > number:
        print("Your guess is high")
    elif guess.lower() == 'exit':
        quit()
        