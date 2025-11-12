import random

secret_number = random.randint(1,100)
attempt = 0


while True:
    attempt += 1
    num = int(input("Give me the number between 1 to 100 :"))
    if num != secret_number:
        if num<secret_number:
            print("Too low ! Try again.")
        else: 
            print("Too high ! Try again.")
    else:
        print(f"Congratulation ! you guessed it in {attempt} attempts.")
        break
