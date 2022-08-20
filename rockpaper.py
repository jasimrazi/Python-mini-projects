import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissor"]

while True:
    user_input = input("Type Rock/Paper/Scissor or Q to quit: ").lower()

    if user_input == 'q':
        break

    if user_input not in options:
        print("Invalid Input")
        continue

    random_number = random.randint(0,2)
    computer_input = options[random_number]
    print(f"Computer picked {computer_input}. ")

    #rock=0 paper=1 scissor=2
    if user_input=="rock" and computer_input=="scissor":
        print("You've won")
        user_wins+=1
    elif user_input=="paper" and computer_input=="rock":
        print("You've won")
        user_wins+=1
    elif user_input=="scissor" and computer_input=="paper":
        print("You've won")
        user_wins+=1
    elif user_input == computer_input:
        print("Its a draw")
    else:
        print("You've lost")
        computer_wins+=1


print(f"You've won {user_wins} times.")
print(f"Computer won {computer_wins} times.")




