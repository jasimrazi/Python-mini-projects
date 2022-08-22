import random
import string

print("Welcome to Password Generator\n")

length = int(input("Enter the length of the password: "))

letters = string.ascii_letters
numbers = string.digits
specials = "!@#$%&"

all = letters + numbers + specials

temp_password = random.sample(all,length)
password = "".join(temp_password)

print("Your password is:",password)
input()



