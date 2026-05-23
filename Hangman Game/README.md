# CodeAlpha Hangman Game

## Project Overview

This project is a console-based Hangman Game developed in Python as part of the Python Programming Internship offered by CodeAlpha.

The game allows the player to guess a hidden word one letter at a time. The player has limited incorrect attempts before the game ends.

This project follows the MVC (Model-View-Controller) Design Pattern to keep the code clean, organized, and easy to maintain.
---

# Features
- Random word selection
- Hidden word display
- Letter-by-letter guessing
- Input validation
- Wrong guess tracking
- Win and lose conditions
- Restart game option
- Error handling
- Case-insensitive input
- Clean MVC architecture
---

# Technologies Used
- Python 3
- Object-Oriented Programming (OOP)
- MVC Design Pattern
---

# Project Structure
CodeAlpha_HangmanGame/
│
├── main.py
├── hangman_model.py
├── hangman_view.py
├── hangman_controller.py
└── README.md
---
## main.py
Main entry point of the project.

Responsibilities:
- starts the game
- handles unexpected errors
- creates controller object
---

## hangman_model.py
Handles:
- game data
- game rules
- word selection
- guess validation
- win/loss checking
---

## hangman_view.py
Handles:
- displaying game messages
- displaying game status
- displaying errors
- taking user-friendly output
---

## hangman_controller.py
Handles:
- game flow
- user input
- connecting Model and View
- restart system
- game loop
---

# Concepts Used
The following Python concepts are used in this project:
- random module
- while loops
- if-else conditions
- strings
- lists
- sets
- functions
- classes and objects
- exception handling
---

# Game Rules
1. The computer selects a random word.
2. The player guesses one letter at a time.
3. Only alphabet letters are allowed.
4. The player has 6 wrong attempts.
5. Correct guesses reveal letters.
6. Wrong guesses reduce remaining attempts.
7. The player wins by guessing the complete word.
8. The player loses after 6 incorrect guesses.
---

# Input Validation
The game handles:
- empty input
- numbers
- symbols
- multiple letters
- duplicate guesses
- uppercase and lowercase letters

Example:
- A and a are treated the same.
---
# How to Run the Project
## Step 1
Install Python 3 on your system.
Download Python from:
https://www.python.org/
---
## Step 2
Open terminal or command prompt inside project folder.
---
## Step 3
Run the following command:
python main.py
---

# Example Gameplay
WELCOME TO THE HANGMAN GAME

Current Word:
_ _ _ _ _ _

Remaining Guesses: 6
Enter a letter: p
Good job! 'p' is in the word.
---

# Future Improvements

Possible future upgrades:
- GUI version using Tkinter
- Difficulty levels
- Large word database
- Score system
- Multiplayer mode
- Sound effects
- Timer mode
---

# Internship Information
This project was created for the Python Programming Internship by CodeAlpha.
Official Website:
https://www.codealpha.tech
---

# Author
Muhammad Saqlain
---
