# Hangman Game in Python

This Hangman game was developed using Python.

![Hangman Game in Python](https://user-images.githubusercontent.com/29802859/224564979-a3412318-2137-4dbc-83bc-da6cd8f63df8.gif)


## Steps

1. Import random module to randomly select a word from the word_list.
2. Import stages and logo from hangman_art module to display the stages of the hangman game and logo respectively.
3. Create a display list with underscores "\_" for each letter in the randomly selected word.
4. Run a while loop that continues until the game ends.
5. In each iteration, ask the user to guess a letter and convert it to lowercase.
6. Check if the letter has already been guessed, if yes, then display a message stating so.
7. If the letter is not guessed already, then loop through the randomly selected word and replace the underscore in the display list with the correct letter if the guess is correct.
8. If the guess is incorrect, reduce the number of lives by 1 and check if the lives become 0, then the game is over.
9. Display the display list with guessed letters and underscores.
10. If all the letters have been guessed correctly, then the game is over and the player wins.

## Features of Python used in this code

- Variables and data types
- Loops and conditions
- Functions and modules
- List and string manipulation

## How to Play

1. Download the hangman_art.py, hangman_words.py, and hangman_game.py files.
2. Make sure you have Python installed on your computer.
3. Open the terminal and navigate to the folder where the downloaded files are saved.
4. Type python hangman_game.py to start the game.
5. Guess a letter and press Enter.
6. Keep guessing until you complete the word or run out of lives.
