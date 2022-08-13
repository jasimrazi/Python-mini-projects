from tkinter import Y
from numpy import char



print("Welcome to the quiz")
playing = input("Do you want to play the game? (Y/N): ").lower() 
option1='y'
option2='yes'
if playing != 'y':
    quit()


score=0    #The actual Program Starts Here
total=4
print("\n[Please input options as answers]\n")
ans=input("How many rings are on the Olympic flag? \nA: 4 B: 5\n")
if ans.upper() == 'B':
    print("\nYour answer is Correct")
    score=score+1
else:
    print("\nYour answer is Incorrect")

ans=input("\nHow many holes are on a standard bowling ball? \nA: 2\nB: 3\n")
if ans.upper() == 'B':
    print("\nYour answer is Correct")
    score=score+1
else:
    print("\nYour answer is Incorrect")

ans=input("\nWhat are the main colors on the flag of Spain? \nA: Red & Yellow\nB: Black & Yellow\n")
if ans.upper() == 'A':
    print("\nYour answer is Correct")
    score=score+1
else:
    print("\nYour answer is Incorrect")

ans=input("\nWhich of these animals appear in the Chinese zodiac? \nA: Bear\nB: Dog\n")
if ans.upper() == 'B':
    print("\nYour answer is Correct")
    score=score+1
else:
    print("\nYour answer is Incorrect\n")
print("------------------------------------\n")
print(f"Your score is: {score} out of {total} questions\n")  #Printing the Score
if score==0:
    print("You Suck...")
elif score==1:
    print("Your score is meh...")
elif score==2:
    print("Still Bad!")
elif score==3:
    print("You a little smart huh...")
else:
    print("Damn, you a genius...")
print("\n------------------------------------\n")
input()