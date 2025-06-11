print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza would you like? S, M, L? ").lower()
add_pepperoni = input("Would you like to add pepperoni to your pizza? y/n ").lower()
extra_cheese = input("Would you like to add extra cheese? y/n ").lower()

pizza_price = 0

if size == 's':
    pizza_price += 15
elif size == 'm':
    pizza_price += 20
else:
    pizza_price += 25

if add_pepperoni == 'y':
    if size == 's':
        pizza_price += 2
    else:
        pizza_price += 3

if extra_cheese == 'y':
    pizza_price += 1


print(f"Your final bill is ${pizza_price}")
