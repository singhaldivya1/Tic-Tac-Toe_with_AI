# Project Title
Tic Tac Toe with AI


## Overview

This is a Tic Tac Toe game with a working Computer player.

There are 3 game modes: Human vs Human, Human vs Computer , Computer vs Computer

  * Human vs Human game has two human players.
  * Human vs Computer game has a human playing against a computer. This mode has additional 3 modes:
    * Easy - The computer here randomly picks the spot from the available spots
    * Medium - Here the computer will try to make a move where there is a chance for his win and play that move, if not then it will test if the opponent is winning and block with a move or else it will pick the first available move(if no one is winning) on the board.
    * Hard (AI) - Have used minmax algorithm to make the computer unbeatable. That means the human player will always loose or it will be a tie situation. Read about minimax algorithm in Russell, Norvig (2010) Adversarial Search in Artifial Intelligence: A Modern Approach. Also, here is the link to minimax algorithm - https://en.wikipedia.org/wiki/Minimax
  * Computer vs Computer game has two computer players playing against each other with no interaction from the user.
  

## Instructions to run the game
* Clone this repository
* Install python 3 
* This repo has 4 file: game.py, computer.py, players.py  and board.py.
* If using an IDE, open the project and run the "game.py" located in "python" folder. 'game.py' imports all the necessary classes used for the game.
  Please make sure all the four files are in the same directory.
* If using command-line follow the instructions mentionded on the link: https://www.pythoncentral.io/execute-python-script-file-shell/. 
(File is in the "python" folder with name "game.py"
* Once you run the file, follow on screen instructions to play the game.

## Running the tests

This game has a automated test suite for unit testing in the `/python/Test_suite` directory. To run the test suite run `test_game.py`, `test_board.py`,
 `test_computer.py` and `test_player.py` in your terminal to test all the classes.
