# Conditional statements
print("Welcome to the rollercoaster!!")
height = int(input("What is your height? "))


price = 0
if height >= 120:
    age = int(input("how old are you? "))
    if age >= 45 and age <= 55:
        print("everything will be okay. Here is a free ride on us!")
        price += 0
    if age <= 12:
        print("Child tickets are $5")
        price += 5
    elif age <= 18:
        print("Youth tickets are $7")
        price += 7
    else:
        print("Adult tickets are $12")
        price += 12
    want_photo = input("Would you like to add a photo? y/n ").lower()
    if want_photo.startswith('y'):
        price += 3
    print(f"You total price is ${price}")
else:
    print("You can't ride.")


# Coding task - odd or even
#
# number = int(input("What number would you like to check? "))
#
# if number % 2 == 0:
#     print(f"The number {number} is even.")
# else:
#     print(f"The number {number} is odd")
