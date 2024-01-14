# Hangman Game

import random
import hangman_art
import hangman_words

stages = hangman_art.stages
logo = hangman_art.logo
word_list = hangman_words.word_list
random_word = random.choice(word_list).lower()
lives = 6

print(logo)

display_list = []
for i in range(0, len(random_word)):
    display_list.append("_")

while '_' in display_list and lives > 0:

    guess = input("Guess a letter: ").lower()

    for i in range(0, len(random_word)):
        if random_word[i] == guess:
            display_list[i] = guess
    if guess not in random_word:
        lives -= 1

    print(display_list)
    print(stages[lives])
    print(f"Remaining lives: {lives}")


if '_' not in display_list and lives > 0:
    print("You Won!!")

if lives == 0:
    print("You Losed!!")