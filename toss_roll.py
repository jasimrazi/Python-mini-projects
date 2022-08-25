import random

print("[Please type Q to quit]")

while True:

    answer = input(
        "Do you want to 'roll a die' or 'toss a coin'? (A/B): ").lower()

    if (answer == 'a' or answer == 'roll a die'):
        r1 = random.randrange(1, 7)
        print("The die landed on", r1)
        continue

    elif (answer == 'b' or answer == 'toss a coin'):
        list = ['head', 'tail']
        r2 = random.choice(list)
        print("The coin landed on", r2)
        continue

    elif (answer == "q" or answer == "quit"):
        break

    else:
        print("Invalid Input")


quit()
