class HangmanView:
    def __init__(self):
        self.introduction()

    def display(self, model):
        stages = ["""
               --------
               |      |
               |      O
               |     \\|/
               |      |
               |     / \\
               -
            """,
            # head, torso, both arms, and one leg
            """
               --------
               |      |
               |      O
               |     \\|/
               |      |
               |     / 
               -
            """,
            # head, torso, and both arms
            """
               --------
               |      |
               |      O
               |     \\|/
               |      |
               |      
               -
            """,
            # head, torso, and one arm
            """
               --------
               |      |
               |      O
               |     \\|
               |      |
               |     
               -
            """,
            # head and torso
            """
               --------
               |      |
               |      O
               |      |
               |      |
               |     
               -
            """,
            # initial empty state
            """
               --------
               |      |
               |      
               |    
               |      
               |     
               -
            """
        ]
        print(stages[model.get_num_lives()])
        print("\t\t\t"+"".join(model.get_word_guessed()))
        print("\t\t\tLetters you have tried: " + ", ".join(model.get_list_of_guesses()) + "\n")

    def display_win(self, model):
        print(r"""
        __   __            _    _ _       _ 
        \ \ / /           | |  | (_)     | |
         \ V /___  _   _  | |  | |_ _ __ | |
          \ // _ \| | | | | |/\| | | '_ \| |
          | | (_) | |_| | \  /\  / | | | |_|
          \_/\___/ \__,_|  \/  \/|_|_| |_(_)


                    """)
        print("\n\t\t\tCongratulations! You've won!")

    def display_loss(self, model):
        print(r"""
           _____                         ____                 
          / ____|                       / __ \                
         | |  __  __ _ _ __ ___   ___  | |  | |_   _____ _ __ 
         | | |_ |/ _` | '_ ` _ \ / _ \ | |  | \ \ / / _ \ '__|
         | |__| | (_| | | | | | |  __/ | |__| |\ V /  __/ |   
          \_____|\__,_|_| |_| |_|\___|  \____/  \_/ \___|_|   


            """)
        print("\n\t\t\tGAME OVER. Better luck next time!")
        print(f"\t\t\tThe secret word was: {model.word}")

    def introduction(self):
        print(r"""
          _    _                                         
         | |  | |                                        
         | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
         |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
         | |  | | (_| | | | | (_| | | | | | | (_| | | | |
         |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                              __/ |                      
                             |___/                       
         Welcome to Hangman!
         Guess the secret word one letter at a time
         The word to guess is represented by a row of dashes, representing each letter of the word
         
         Instructions:
         
         1. The game will show you how many letters there are in the word
         2. Type one letter per round to guess the word
         3. If your chosen letter exists in the word, the game will reveal its correct position(s)
         4. If the word does not contain the letter, the game will draw one element of the hangman 'gallows'
         5. The game continues until:
            - The word is guessed (WIN), or;")
            - All the parts of the hangman are displayed (LOSE).")
    
                            Good luck!   
    
                    """)
