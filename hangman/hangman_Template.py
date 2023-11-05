'''
Make sure you complete all the TODOs in this file.
The prints have to contain the same text as indicated, don't add any more prints,
or you will get 0 for this assignment.
'''
import random

class Hangman:
    def __init__(self, word_list, num_lives):
        self.word = random.choice(word_list)
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = set()
        self.word_guessed = ["_" for e in range(len(self.word))]
        self.ask_for_input()

    def check_guess(self, guess):
        letter = guess.lower()
        if (letter in self.word):
            print(f"Good guess! {guess} is in the word.")
            for index in range(len(self.word)):
                if (letter == self.word[index]):
                    self.word_guessed[index] = letter
                    self.list_of_guesses.add(letter)
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {letter} is not in the word.")
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self):
        while True:
            guess = input("Enter a letter: ")
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that")
                self.list_of_guesses.add(guess)
            else:
                self.check_guess(guess)
                break

    def __str__(self):
        return "".join(self.word_guessed)

def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)
    while True:
        print(game)
        if (game.num_lives == 0):
            print("You lost")
            print(f"The word was {game.word}")
            break

        elif (game.num_letters > 0):
            game.ask_for_input()

        elif (game.num_letters <= 0 and game.num_lives != 0):
            print('Congratulations. You won the game!')
            break

if __name__ == '__main__':
    word_list = ['apple', 'bananas', 'grape', 'pear', 'strawberry']
    play_game(word_list)
# %%
