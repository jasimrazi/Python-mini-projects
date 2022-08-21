print ("Welcome to Password Manager\n")
print ("Type Q to quit\n")


def add():
    name = input("Enter the user name: ")
    pwd = input("Enter the password: ")

    f = open("passwords.txt","a")
    f.write(name+"|"+pwd+"\n")
    f.close()


def view():
    with open("passwords.txt","r") as f:
         for line in f:
            data = line.rstrip()
            username, password = data.split("|")
            print("User:",username,"| Password:",password)
            


while True:
    answer = input("Do you want view or add a password (view/add): ").lower()

    if answer == "view":
        view()

    elif answer == "add":
        add()

    elif answer == 'q':
        break
    
    else:
        print("Invalid Input")
        continue