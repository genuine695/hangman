# Hangman
	   _    _
	  | |  | |                                        
         | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
         |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
         | |  | | (_| | | | | (_| | | | | | | (_| | | | |
         |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                              __/ |                      
                             |___/
                  
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

## Description

The Hangman Game in Python is a simple console-based game where players try to guess a word by suggesting letters within a certain number of attempts. The aim of this project is to provide a fun and interactive way to play the classic Hangman game while also serving as a learning resource for Python beginners. By working on this project, you will learn:
The game has been implemented using the MVC architecture to promote better code practises

- Basic Python programming concepts.
- Handling user input and validation.
- Working with strings and random word selection.
- Implementing game logic and user interaction.

# Controls and game logic

- Game initially begins with a let word list from which a random word is picked and total lives
- Initially all the letters in the word is represented as dashes 
- To input a letter: type in a letter where it says "Enter letter: " and hit enter
- If the letter is in the word, it will replace the dash with the letter in its respective position
- If the letter is not in the word, you will lose a life
- If you lose all your lives, the CLI interface will display "Lost" state
- If you guess all the letters correct before its finished, the CLI interface will display "Win" state
- If you attempt to enter a letter that has already been attempted you will message saying you have already attempted it 

# Installation:

Clone the github repository into your local drive. Make sure git and python is installed in your system

# Journey from inception to implementation

The things I learned from this experience:
	- MVC architecture
	- Working on a project incrementally
	- Applying all the skills I have learnt so far: Git, VScode, object-oriented programming skills
	- Overcoming setbacks and challenges
	- Writing docstrings to promote readability 

# What could be done in the future
	- Implement GUI
	- Implement a design pattern such as observer pattern
	- Reduce code smells and better commenting
	
