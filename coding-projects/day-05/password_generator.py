import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

password = ""

for letter in range(0, nr_letters):
    random_letter = random.choice(letters)
    password += random_letter


for symbol in range(0, nr_symbols):
    random_symbol = random.choice(symbols)
    password += random_symbol

for number in range(0, nr_numbers):
    random_number = random.choice(numbers)
    password += random_number
print(f"Your easy password is: {password}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number

password = []

for letter in range(0, nr_letters):
    random_letter = random.choice(letters)
    password.append(random_letter)


for symbol in range(0, nr_symbols):
    random_symbol = random.choice(symbols)
    password.append(random_symbol)

for number in range(0, nr_numbers):
    random_number = random.choice(numbers)
    password.append(random_number)

random.shuffle(password)
password_string = ""
for char in password:
    # random_char = random.choice(password)
    password_string += char

print(f"Here is your hard password: {password_string}")