# this day is about building the hangman game.
import random
from art import logo, hangman_lives
from game_words import words

lives = 0

correct_guess = []

random_word = random.choice(words)

print(random_word)
print(logo)
placeholder = ""
for letter in random_word:
    placeholder += '_'
print(f"Word to guess: {placeholder}")

game_won = False
while not game_won:

    user_guess = input("Guess a letter: ").lower()
    if user_guess in correct_guess:

        print(f"You have already guessed {user_guess}")
        continue

    display = ""
    for char in random_word:
        if char == user_guess:
            display+= char
            correct_guess.append(user_guess)
        elif char in correct_guess:
            display += char
        else:
            display += "_"
    print(display)

    if user_guess not in random_word:
        print(f"You have guessed {user_guess}, that is not in the word. You lose a life")
        print(hangman_lives[lives])
        lives += 1
        print(f"You have used {lives} life out of {len(hangman_lives)}")
        if lives == len(hangman_lives):
            print("You lost")
            game_won = True
            print("You lost")
    if "_" not in display:
        game_won = True
        print("You win!")
