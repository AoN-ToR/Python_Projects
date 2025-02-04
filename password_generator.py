import random
import string
import time

def get_user_input(prompt, valid_options=None):
    while True:
        user_input = input(prompt).lower()
        if valid_options:
            if user_input in valid_options:
                return user_input
            else:
                print("Invalid input. Try again.")
        else:
            if user_input.isdigit() and int(user_input) > 2:
                return int(user_input)
            elif user_input == "q":
                quit()
            else:
                print("Invalid input. Try again.")

char_allowed = []

length = get_user_input("How many characters would you like in your password? (q to quit, min length = 3) ")
use_letters = get_user_input("Should we use letters in your password? (Y/n) ", ["y", "n"]) == "y"
use_numbers = get_user_input("Should we use numbers in your password? (Y/n) ", ["y", "n"]) == "y"
use_special_chars = get_user_input("Should we use special characters in your password? (Y/n) ", ["y", "n"]) == "y"

char_allowed = [use_letters, use_numbers, use_special_chars]

def generate(length, char_allowed):
    characters = ""
    if char_allowed[0]:
        characters += string.ascii_letters
    if char_allowed[1]:
        characters += string.digits
    if char_allowed[2]:
        characters += string.punctuation

    if not characters:
        print("Insufficient material.")
        quit()

    # Ensure the inclusion of at least one character from each allowed category
    password = []
    if char_allowed[0]:
        password.append(random.choice(string.ascii_letters))
    if char_allowed[1]:
        password.append(random.choice(string.digits))
    if char_allowed[2]:
        password.append(random.choice(string.punctuation))

    # Generate the rest of the password
    while len(password) < length:
        password.append(random.choice(characters))

    # Shuffle the password list and convert to string
    random.shuffle(password)
    return "".join(password)

password = generate(length, char_allowed)
for i in range(2):
    print(".", end="")
    time.sleep(1)
print(f"\n\nHere is your freshly done new password:\n{password}\n\nSee you later! ")
