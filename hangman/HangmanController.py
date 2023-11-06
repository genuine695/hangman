from HangmanModel import HangmanModel
from HangmanView import HangmanView

class HangmanController:
     def __init__(self):
        self.model = None
        self.view = HangmanView()

     def start_game(self):
        word_list = ['apple', 'bananas', 'grape', 'pear', 'strawberry']
        num_lives = 5
        self.model = HangmanModel(word_list,num_lives)

     def play_game(self):
        self.start_game()
        while True:
            self.view.display(self.model)
            if self.model.is_game_won():
                self.view.display_win(self.model)
                break
            elif self.model.is_game_lost():
                self.view.display(self.model)
                break
            else:
                self.model.ask_for_input()

