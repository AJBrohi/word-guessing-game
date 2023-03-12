import random
from hangman_art import stages,logo
from hangman_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(logo)

# print(f'Pssst, the solution is {chosen_word}.')

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    
    if guess in display:
        print(f"You already guessed the letter {guess}.")
        
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(f"{guess} is not in the word. You lost all of your lives.\nYou lose.\nCorrect answer was: {chosen_word}")
        else:
            print(f"{guess} is not in the word. You lost a life.\nRemaining Life: {lives}")
    print(f"{' '.join(display)}")
    
    if "_" not in display:
        end_of_game = True
        print("Congratulation! You guessed all the letters correctly.\nYou win.")
    
    print(stages[lives])