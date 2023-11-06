import random
class HangmanModel:
    def __init__(self, word_list, num_lives):
        self.word = random.choice(word_list)
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = set()
        self.word_guessed = ["_" for e in range(len(self.word))]
        self.observers = []
        self.ask_for_input()

    def check_guess(self, guess):
        letter = guess.lower()
        if (letter in self.word):
            print(f"\t\t\tGood guess! {guess} is in the word.")
            for index in range(len(self.word)):
                if (letter == self.word[index]):
                    self.word_guessed[index] = letter
                    self.list_of_guesses.add(letter)
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"\t\t\tSorry, {letter} is not in the word.")
            print(f"\t\t\tYou have {self.num_lives} lives left.")
            self.list_of_guesses.add(guess)

    def ask_for_input(self):
        while True:
            guess = input("\t\t\tEnter a letter: ")
            if len(guess) != 1 or not guess.isalpha():
                print("\t\t\tInvalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("\t\t\tYou already tried that")
            else:
                self.check_guess(guess)
                break

    def is_game_won(self):
         return self.num_letters <= 0 and self.num_lives != 0

    def is_game_lost(self):
        return self.num_lives == 0

    def get_word_guessed(self):
        return self.word_guessed

    def get_num_lives(self):
        return self.num_lives

    def get_list_of_guesses(self):
        return self.list_of_guesses