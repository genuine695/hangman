from HangmanModel import HangmanModel
from HangmanView import HangmanView

class HangmanController:
     '''
     Controller class of MVC architecture.

     Controller directs the data flow into Model and update the View
     based on its feedback.

     Attributes
     ----------
     model (HangmanModel): The model instance containing the game state and logic.
     view (HangmanView): The view instance responsible for displaying the game's output to the user.
    
     Methods
     -------

     start_game()
        creates the games state by initialising the word list and number of lives
        initialises model class
    
    play_game():
        Starts the game and carries on playing until the player wins or lose
    
     '''

     def __init__(self):
        self.model = None
        self.view = HangmanView()

     def start_game(self):
        # Creates the games state by initialising the word list and number of lives
        word_list = ['apple', 'bananas', 'grape', 'pear', 'strawberry']
        num_lives = 5
        # Initialises model class
        self.model = HangmanModel(word_list,num_lives)

     def play_game(self):
        self.start_game()
        # Loops through until 
        while True:
            # Display the lives left, letters attempted and hangman status
            self.view.display(self.model)
            if self.model.is_game_won():
                # Displays Win state
                self.view.display_win(self.model)
                break
            elif self.model.is_game_lost():
                # Displays Lose state
                self.view.display_loss(self.model)
                break
            else:
                # Calls method for user to enter letter
                self.model.ask_for_input()

