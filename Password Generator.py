import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Ask the user for the desired password length
length = int(input("Enter the desired password length: "))
print("Your generated password is:", generate_password(length))
