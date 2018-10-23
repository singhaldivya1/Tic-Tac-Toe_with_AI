# -*- coding: utf-8 -*-
"""
Created on Sun Sep  2 20:37:37 2018

@author: singh
"""
import random
import time
from enum import Enum
from board import Board
from computer import Computer
from players import Player

#enum used to define different game modes
class GameMode(Enum):
    HUMAN_vs_HUMAN = 1
    COMP_vs_HUMAN = 2
    COMP_vs_COMP = 3
    
#Class that handles the play
class Game:
    
    #Constructor
    def __init__(self):
        self.board = Board()
        self.player1symbol = 'X'
        self.player2symbol = 'O'
        self.player1 = None
        self.player2 = None
        self.game_mode = None
        self.difficulty = 0
        self.isPlayer1First = True
    
    # to set the game mode 
    def set_game_mode(self):
        print("\nChoose amongst three modes:\n  1) Human vs Human\n  2) Computer vs Human\n  3) Computer vs Computer\n")
        case = input()
        while (not case.isnumeric()) or (int(case) < 1 or int(case) > 3) :
            print("Invalid selection")
            print("\nChoose amongst three modes:\n  1) Human vs Human\n  2) Computer vs Human\n  3) Computer vs Computer\n")
            case = input()
        self.game_mode = int(case)
        
     # setting up players for the game according to the game mode   
    def setup_players(self):
        if (GameMode(self.game_mode) == GameMode.HUMAN_vs_HUMAN):
            self.get_player_symbol()
            self.player1 = Player(self.board, self.player1symbol)
            self.player2 = Player(self.board, self.player2symbol)
            self.set_plays_first()
        elif (GameMode(self.game_mode) == GameMode.COMP_vs_HUMAN):
            self.get_player_symbol()
            self.set_difficulty()
            self.player1 = Player(self.board, self.player1symbol)
            self.player2 = Computer(self.board, self.player2symbol, self.difficulty)
            self.set_plays_first()
        else:
            self.player1 = Computer(self.board, self.player1symbol, 1)
            self.player2 = Computer(self.board, self.player2symbol, 3)
            
      # asking user to select the symbol      
    def get_player_symbol(self):
        print("Player1, choose your symbol O or X")
        self.player1symbol = input()
        while(self.player1symbol != "X" and self.player1symbol != "O"):
            print("Invalid selection!!")
            print("Choose your symbol O or X")
            self.player1symbol = input()
        if self.player1symbol =="X":
            self.player2symbol ="O"
        else:
            self.player2symbol = "X"
            
     # asking user who wants to play first       
    def set_plays_first(self):
        print("Does %s(Player 1) want to play first?...Type 1 for Yes and 0 for No" %(self.player1symbol))
        ans = input()
        while (not ans.isnumeric()) or (int(ans) != 1 and int(ans)!=0):
            print("Invalid selection!!")
            print("Does X(Player 1) want to play first?...Type 1 for Yes and 0 for No")
            ans = input()
        ans = int(ans)
        if (ans == 0):
            self.isPlayer1First = False
            
      # setting up game difficult if game mode is human vs computer      
    def set_difficulty(self):
        print(" Select the mode :\n 1 - Easy \n 2 - Medium \n 3 - Difficult")
        mode = input()
        while (not mode.isnumeric()) or (int(mode)<1 or int(mode)>3):
            print("Invalid input!!")
            print(" Select the mode :\n 1 - Easy \n 2 - Medium \n 3 - Difficult")
            mode = input()
        self.difficulty = int(mode)
    
    
    #method responsible to handle the game play
    def start_game(self):
        self.set_game_mode()
        self.setup_players()
        self.begin_play()
        print("Game Over!!!!!\n")
        self.printResult()
        
        print("Do you want to play again? Press 1 for Yes 0 for No")
        gameagain = input()
        while  (not gameagain.isnumeric()) or (int(gameagain) != 1 and int(gameagain)!=0):
            print("Invalid selection!!")
            print("Do you want to play again? Press 1 for Yes 0 for No")
            gameagain = input()
        gameagain = int(gameagain)
        if gameagain == 1:
            self.__init__()
            self.start_game()
        
    def printResult(self):
        if self.board.game_is_over(self.player1symbol):
            print("Winner is player 1")
        elif self.board.game_is_over(self.player2symbol):
            print("Winner is player 2")
        else:
            print("Game is tie")


    def begin_play(self):
        if(self.isPlayer1First):
            while not self.board.game_is_over(self.player1symbol) and not self.board.game_is_over(self.player2symbol)  and not self.board.tie():
                print("Player 1 is playing with symbol: {}".format(self.player1symbol))
                self.player1.make_move()
                print(self.board)
                if not self.board.game_is_over(self.player1symbol) and not self.board.game_is_over(self.player2symbol)  and not self.board.tie():
                    print("Player 2 is playing with symbol: {}".format(self.player2symbol))
                    self.player2.make_move()
                    print(self.board)
        else:
            while not self.board.game_is_over(self.player1symbol) and not self.board.game_is_over(self.player2symbol)  and not self.board.tie():
                print("Player 2 is playing with symbol: {}".format(self.player2symbol))
                self.player2.make_move()
                print(self.board)
                if not self.board.game_is_over(self.player1symbol) and not self.board.game_is_over(self.player2symbol)  and not self.board.tie():
                    print("Player 1 is playing with symbol: {}".format(self.player1symbol))
                    self.player1.make_move()
                    print(self.board)
              

if __name__ == '__main__':
  game = Game()
  game.start_game()
  print("THANK YOU FOR PLAYING!!!!!!")

        
    