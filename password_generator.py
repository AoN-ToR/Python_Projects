import random
import string
import time

char_allowed = [""]


while True:
    n = input("How many char would you like in your password (q to quit, min lenght = 3)? ")
    if n.lower == "q":
        quit()
    elif n.isdigit():
        length = int(n)
        if length > 2:
            break
        print("Invalid input. Try again.")
    else:
        print("Invalid input. Try again.")

while True:
    n = input("Should we use letters in your password? (Y/n) ").lower()
    if n == "y":
        char_allowed.append(True)
        break
    elif n == "n":
        char_allowed.append(False)
        break
    else:
        print("Invalid input. Try again.")

while True:
    n = input("Should we use numbers in your password? (Y/n) ").lower()
    if n == "y":
        char_allowed.append(True)
        break
    elif n == "n":
        char_allowed.append(False)
        break
    else:
        print("Invalid input. Try again.")

while True:
    n = input("Should we use special caracters in your password? (Y/n) ").lower()
    if n == "y":
        char_allowed.append(True)
        break
    elif n == "n":
        char_allowed.append(False)
        break
    else:
        print("Invalid input. Try again.")



def generate(length, char_allowed):
    letters = string.ascii_letters
    numbers = string.digits
    spe_chars = string.punctuation

    list = [letters, numbers, spe_chars]
    lenght_list = 3

    for i in range(3):
        if char_allowed[i] == False:
            list.pop(i)
            lenght_list -= 1
    if len(list) < 1:
        print("Insufficient material.")
        quit()

    else:
        list2 = letters + numbers + spe_chars
        password = ""
        for i in range(length):
            char = list2[random.randint(0, len(list2)-1)]
            password = str(password) + str(char)
        check = lenght_list
        for item in list:
            for j in range(len(item)):
                if item[j] in password:
                    check -= 1
                    break
        if check == 0:
            for i in range(2):
                print(".", end="")
                time.sleep(1)
            print(f"\n\nHere is your freshly done new password:\n{password}\n\nSee you later! ")
        else:
            print(".", end="")
            time.sleep(1)
            generate(length, char_allowed)

generate(length, char_allowed)