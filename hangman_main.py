# Step 1
import os
import random
from hangman_words import word_list


# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
from hangman_art import logo
from hangman_art import stages

print(logo)
chosen_word = random.choice(word_list)
print(chosen_word)

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

display = []
lives = 0
for i in chosen_word:
    display += "_"
end_of_game = False
while end_of_game == False:
    guess = input("Guess a letter: ").lower()
    os.system('cls')

    # TODO-3 - Check if the letter the user guessed (guess) is one of the leters in the chosen_word.
    length = len(word_list)
    if guess in display:
        print(f"You have already guessed the letter {guess},and ")

    if guess in chosen_word:
        print("You guessed correct")
        for letter in range(0, len(chosen_word)):
            if chosen_word[letter] == guess:
                display[letter] = guess
        print(*display, sep=' ')

    else:
        # keep track of the player lives
        print(
            f"Oops!  you guessed {guess}, that is not in the word you lose a chance")
        if lives == -7:
             print("You Lose")
             break
        else:
            lives -= 1
            print(stages[lives])
           

# if the complete man gets hanged display the result
   

    if "_" not in display:
        end_of_game = True
        print("You win")
