import random
class HangmanModel:
    '''
    A Hangman Game that asks the user for a letter and checks if it is in the word.
    It starts with a default number of lives and a random word from the word_list.

    The model represents the application's data and business logic, 
    handling the retrieval, processing, and storage of data
    
    Parameters:
    ----------
    word_list: list
        List of words to be used in the game
    num_lives: int
        Number of lives the player has
    
    Attributes:
    ----------
    word: str
        The word to be guessed picked randomly from the word_list
    word_guessed: list
        A list of the letters of the word, with '_' for each letter not yet guessed
        For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']
        If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
    num_letters: int
        The number of UNIQUE letters in the word that have not been guessed yet
    num_lives: int
        The number of lives the player has
    list_of_guesses: set
        A list of the letters that have already been tried
    Methods:
    -------
    check_guess(guess)
        Checks if the letter is in the word.
    ask_for_input()
        Asks the user for a letter.
    '''
    def __init__(self, word_list, num_lives):
        # instance varaibles for hangman model
        self.word = random.choice(word_list)
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = set()
        self.word_guessed = ["_" for e in range(len(self.word))]
        self.ask_for_input()

    def check_guess(self, guess):
        '''
        Checks if the letter is in the word.
        If it is, it replaces the '_' in the word_guessed list with the letter.
        If it is not, it reduces the number of lives by 1.
        Parameters:
        ----------
        guess: str
            The letter to be checked
        '''
        letter = guess.lower()
        
        #
        if (letter in self.word):
            print(f"\t\t\tGood guess! {guess} is in the word.")

            # Replaces the dashes with letters
            for index in range(len(self.word)):
                if (letter == self.word[index]):
                    self.word_guessed[index] = letter
                    # Adds the letter to a list of attempted letters
                    self.list_of_guesses.add(letter)
            # One of the variables to check the win state
            self.num_letters -= 1
        else:
            # Lose a life for every letter not in word
            self.num_lives -= 1
            print(f"\t\t\tSorry, {letter} is not in the word.")
            print(f"\t\t\tYou have {self.num_lives} lives left.")
            self.list_of_guesses.add(guess)

    def ask_for_input(self):
        '''
        Asks the user for a letter and checks two things:
        1. If the letter has already been tried
        2. If the character is a single character
        If it passes both checks, it calls the check_letter method.
        '''
        while True:
            #
            guess = input("\t\t\tEnter a letter: ")
            # Checks if the given input is a letter
            if len(guess) != 1 or not guess.isalpha():
                print("\t\t\tInvalid letter. Please, enter a single alphabetical character.")
            # Checks if the given input has already entered
            elif guess in self.list_of_guesses:
                print("\t\t\tYou already tried that")
            # Calls check_guess method to verify if the letter is valid
            else:
                self.check_guess(guess)
                break

    def is_game_won(self):
         '''
         Checks if the player has won the game
         '''
         return self.num_letters <= 0 and self.num_lives != 0

    def is_game_lost(self):
        '''
        Check if the player has lost the game
        '''
        return self.num_lives == 0

    def get_word_guessed(self):
        '''
        Returns the word to be guessed.
        '''
        return self.word_guessed

    def get_num_lives(self):
        '''
        Returns the number of lives the player has left
        '''
        return self.num_lives

    def get_list_of_guesses(self):
        '''
        Returns the number of
        '''
        return self.list_of_guesses