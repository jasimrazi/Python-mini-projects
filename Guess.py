from operator import truediv
import random

range=input("Please type a range: ")       #Checking the range condiotions
if range.isdigit():
    range=int(range)
    if range<=0:
        print('Please type a number more than 0 and try again')
        input()
else:
    print("Please a type a 'number'")
    input()

random_number=random.randint(0,range)      #Sets the range
total = 0                                  #Initialise the variable for no. of guesses

while True:                                #Giving hints using while loop
    guess=input("Guess the number: ")
    if guess.isdigit():
        guess=int(guess)
        total+=1
    else:
        print("[Please a type a 'number' this time]")
        continue

    if guess == random_number:
        print("You got it right!")
        print("\nYou took",total,"guesses in total.")
        input()
        break
    elif guess < random_number:
        print("Your guess is below the number")
    else:
        print("Your guess is above the number")
        







