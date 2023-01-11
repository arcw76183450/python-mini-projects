#Step 4

import random
from hangman_words import word_list
from hangman_art import stages
from hangman_art import logo

end_of_game = False
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6

display = []
for _ in range(word_length):
    display += "_"

print(logo)
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        lives -= 1
    if lives == 0:
        end_of_game = True
        print('You Lose')
    print(f"{' '.join(display)}")
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])