import random
# Rock Paper Scissors ASCII Art

# Rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper ="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors ="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
# art from: https://gist.github.com/wynand1004/b5c521ea8392e9c6bfe101b025c39abe

choice = [rock, paper, scissors]

user_choice = int(input("Choose: 0-rock, 1-paper, 2-scissors"))

computer_choice = random.randint(0, 2)
if 0 <= user_choice <= 2:
    print("You chose: ")
    print(choice[user_choice])

    print("Computer chose: ")
    print(choice[computer_choice])

    if computer_choice == 0 and user_choice == 0:
        print("It's a tie!")
    elif user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif user_choice == 1 and computer_choice == 0:
        print("You win!")
    elif user_choice == 2 and computer_choice == 1:
        print("You win!")
    else:
        print("You lose!")
else:
    print("Invalid number. You lose.")

print("Thanks for playing.")
