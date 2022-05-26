import random

user_wins = 0
computer_wins = 0

options = ["rock" , "paper", "Scissor"]

while True:
    user_Input = input("Type rock/scissor/paper or Q to quit:").lower()
    if user_Input == "q":
        break

    if user_Input not in options:
        continue
    random_numer = random.randint(0,2)
    computer_pick  = options[random_numer]
    print("computer picked", computer_pick + ".")

    if user_Input == "rock" and computer_pick == "scissor":
        print("you won")
        user_wins += 1

    if user_Input == "scissor" and computer_pick == "paper":
        print("you won")
        user_wins += 1

    if user_Input == "rock" and computer_pick == "paper":
        print("you won")
        user_wins += 1
    else:
        print("you lost")
        computer_wins +=1

print("You won", + user_wins, "times.")
print("The computer won", computer_wins, "times.")
print("By, the game is over")



    

