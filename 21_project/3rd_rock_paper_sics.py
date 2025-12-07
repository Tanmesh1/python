# Let's see how many times user gets correct and how many times computer gets correct
import random 

user_wins = 0
comp_wins = 0
options = ["rock","paper","scissor"]


while True:
    user_move = input("Enter Rock/Paper/Scissor or Q to quit: ").lower()
    if user_move == "q":
        break
    
    if user_move not in options:
        continue
    random_number = random.randint(0,2)
    
    computer_pick = options[random_number]
    print("Computer Picked",computer_pick+".")
    
    if user_move == "rock" and computer_pick == "scissor":
        print("You Won!")
        user_wins += 1
        
        
    elif user_move == "scissor" and computer_pick == "paper":
        print("You Won!")
        user_wins += 1
        
        
    elif user_move == "paper" and computer_pick == "rock":
        print("You Won!")
        user_wins += 1
        
        
    else:
        print("You Lost!")
        comp_wins += 1
        
print("Your wins: " + str(user_wins) + " Computer wins: " + str(comp_wins))
print("GoodBye")
    