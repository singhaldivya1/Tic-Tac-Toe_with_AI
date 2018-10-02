# -*- coding: utf-8 -*-
"""
Created on Sun Sep  2 20:37:37 2018

@author: singh
"""
import random
import time
from enum import Enum

#enum used to define different game modes
class GameMode(Enum):
    HUMAN_vs_HUMAN = 1
    COMP_vs_HUMAN = 2
    COMP_vs_COMP = 3
    DIFFICULT = 4
    MEDIUM = 5
    EASY = 6
    
#Class that handles the play
class Game:
    
    #Constructor
    def __init__(self):
        self.board = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
        self.player1symbol = 0
        self.player2symbol = 0

    
    #method prints the current status of the board
    def printing(self):
        print (" %s | %s | %s \n===+===+===\n %s | %s | %s \n===+===+===\n %s | %s | %s \n" % \
        (self.board[0], self.board[1], self.board[2],
             self.board[3], self.board[4], self.board[5],
             self.board[6], self.board[7], self.board[8]))
    
    #method responsible to handle the game play
    def start_game(self):
        # start by taking input from the user to select the game mode
        
        print("\nChoose amongst three modes:\n  1) Human vs Human\n  2) Computer vs Human\n  3) Computer vs Computer\n")
        case = input()
        while not case.isnumeric():
            print("Invalid selection")
            print("\nChoose amongst three modes:\n  1) Human vs Human\n  2) Computer vs Human\n  3) Computer vs Computer\n")
            case = input()
        case = int(case)
        #check if the user input is valid : valid->continue || invalid->take input again
        if(case>0 and case<4):
            #print initial board
            print("\nInitial Board:")
            self.printing()
            
            #check the user input for game mode and play accordingly
            # case 1 : Human vs Human
            if (GameMode(case) == GameMode.HUMAN_vs_HUMAN):
                self.player1symbol = "X"
                self.player2symbol = "O"
                
                # ask if player 1 with symbol X wants to go first
                print("Does X(Player 1) want to play first?...Type 1 for Yes and 0 for No")
                ans = input()
                while (not ans.isnumeric()) or (int(ans) != 1 and int(ans)!=0):
                    print("Invalid selection!!")
                    print("Does X(Player 1) want to play first?...Type 1 for Yes and 0 for No")
                    ans = input()
                ans = int(ans)
                
                while not self.game_is_over(self.board,"X") and not self.game_is_over(self.board,"O")  and not self.tie(self.board):
                    if ans ==1:
                        print("Player 1 is playing with symbol: {}".format(self.player1symbol))
                        self.get_human_spot("X")
                        self.printing()
                        if not self.game_is_over(self.board,"X") and not self.game_is_over(self.board,"O") and not self.tie(self.board):
                            print("Player 2 is playing with symbol: {}".format(self.player2symbol))
                            self.get_human_spot("O")
                            self.printing()
                    else:
                        print("Player 1 is playing with symbol: {}".format(self.player2symbol))
                        self.get_human_spot("O")
                        self.printing()
                        if not self.game_is_over(self.board,"X") and not self.game_is_over(self.board,"O") and not self.tie(self.board):
                            print("Player 2 is playing with symbol: {}".format(self.player1symbol))
                            self.get_human_spot("X")
                            self.printing()
                        
            # case 2 : Computer vs Human
            elif(GameMode(case) == GameMode.COMP_vs_HUMAN):
                    #take symbol from the user
                    print("Choose your symbol O or X")
                    self.player1symbol = input()
                    while(self.player1symbol != "X" and self.player1symbol != "O"):
                        print("Invalid selection!!")
                        print("Choose your symbol O or X")
                        self.player1symbol = input()
                    if self.player1symbol =="X" :    #human
                        self.player2symbol ="O"        #comp
                    else:
                        self.player2symbol = "X"
                        
                    #ask if the user wants to play frist
                    print("Do you want to play first?..Type 1 for Yes and 0 for No")
                    ans = input()
                    while (not ans.isnumeric()) or (int(ans) != 1 and int(ans)!=0):
                        print("Invalid selection!!")
                        print("Does X want to play first?...Type 1 for Yes and 0 for No")
                        ans = input()
                    ans = int(ans)
                    
                    #ask user for difficulty level
                    print(" Select the mode :\n 4 - Difficult \n 5 - Medium \n 6 - Easy")
                    mode = input()
                    while (not mode.isnumeric()) or (int(mode)<4 or int(mode)>6):
                        print("Invalid input!!")
                        print(" Select the mode :\n 4 - Difficult \n 5 - Medium \n 6 - Easy")
                        mode = input()
                    mode = int(mode)
                    
                    if (GameMode(mode) == GameMode.DIFFICULT):
                        while not self.game_is_over(self.board,"X") and not self.game_is_over(self.board,"O")  and not self.tie(self.board):
                            if ans == 1:     #human is playing first
                                print("Player 1 is playing with symbol: {}".format(self.player1symbol))
                                self.get_human_spot(self.player1symbol)
                                self.printing()
                                if not self.game_is_over(self.board,"X") and not self.game_is_over(self.board,"O") and not self.tie(self.board):
                                    print("Player 2 is playing with symbol: {}".format(self.player2symbol))
                                    time.sleep(2)
                                    bestSpot = self.minmax(self.board,self.player2symbol,self.player1symbol)
                                    self.board[bestSpot["Index"]] = self.player2symbol
                                    self.printing()
                            else:           #comp is first
                                print("Player 2 is playing with symbol: {}".format(self.player2symbol))
                                time.sleep(2)
                                bestSpot = self.minmax(self.board,self.player2symbol,self.player1symbol)
                                self.board[bestSpot["Index"]] = self.player2symbol
                                self.printing()
                                if not self.game_is_over(self.board,"X") and not self.game_is_over(self.board,"O") and not self.tie(self.board):
                                    print("Player 1 is playing with symbol: {}".format(self.player1symbol))
                                    self.get_human_spot(self.player1symbol)
                                    self.printing()
                                    
                    elif(GameMode(mode) == GameMode.MEDIUM):
                        while not self.game_is_over(self.board,"X") and not self.game_is_over(self.board,"O")  and not self.tie(self.board):
                            if ans ==1:
                                print("Player 1 is playing with symbol: {}".format(self.player1symbol))
                                self.get_human_spot(self.player1symbol)
                                self.printing()
                                if not self.game_is_over(self.board,"X") and not self.game_is_over(self.board,"O") and not self.tie(self.board):
                                    print("Player 2 is playing with symbol: {}".format(self.player2symbol))
                                    self.eval_board(self.player2symbol,self.player1symbol)
                                    self.printing()
                            else:
                                print("Player 1 is playing with symbol: {}".format(self.player1symbol))
                                self.eval_board(self.player1symbol,self.player2symbol)
                                self.printing()
                                if not self.game_is_over(self.board,"X") and not self.game_is_over(self.board,"O") and not self.tie(self.board):
                                    print("Player 2 is playing with symbol: {}".format(self.player2symbol))
                                    self.get_human_spot(self.player2symbol)
                                    self.printing()
                                    
                    elif(GameMode(mode) == GameMode.EASY):
                        while not self.game_is_over(self.board,"X") and not self.game_is_over(self.board,"O")  and not self.tie(self.board):
                            if ans == 1:
                                print("Player 1 is playing with symbol: {}".format(self.player1symbol))
                                self.get_human_spot(self.player1symbol)
                                self.printing()
                                if not self.game_is_over(self.board,"X") and not self.game_is_over(self.board,"O") and not self.tie(self.board):
                                    print("Player 2 is playing with symbol: {}".format(self.player2symbol))
                                    self.random_play(self.player2symbol)
                                    self.printing()
                            else:
                                print("Player 1 is playing with symbol: {}".format(self.player1symbol))
                                self.random_play(self.player2symbol)
                                self.printing()
                                if not self.game_is_over(self.board,"X") and not self.game_is_over(self.board,"O") and not self.tie(self.board):
                                    print("Player 2 is playing with symbol: {}".format(self.player2symbol))
                                    self.get_human_spot(self.player1symbol)
                                    self.printing()
                        
            # case 3 : Computer vs Computer
            elif(GameMode(case) == GameMode.COMP_vs_COMP):
                    self.player1symbol = "X"
                    self.player2symbol = "O"
                    while not self.game_is_over(self.board,"X") and not self.game_is_over(self.board,"O")  and not self.tie(self.board):
                            print("Player 1 is playing with symbol {}".format(self.player1symbol))
                            self.random_play(self.player1symbol)
                            self.printing()
                            if not self.game_is_over(self.board,"X") and not self.game_is_over(self.board,"O") and not self.tie(self.board):
                                print("Player 2 is playing with symbol {}".format(self.player2symbol))
                                bestSpot = self.minmax(self.board,self.player2symbol,self.player1symbol)
                                self.board[bestSpot["Index"]] = self.player2symbol
                                time.sleep(2)
                                self.printing()
                                
        #user input is invalid
        else:
            print("Sorry! Invalid GameMode!")
            self.start_game()
        
        #print the status of the game for players
        if self.game_is_over(self.board,"X"):
            if (self.player1symbol == "X"):
                print("Winner is player 1")
            else:
                print("Winner is player 2")
        elif self.game_is_over(self.board,"O"):
            if (self.player1symbol == "O"):
                print("Winner is player 1")
            else:
                print("Winner is player 2")
        elif(self.tie(self.board)):
            print("Game is tie")
            
            
        print("Game over\n")
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
                
    #method that takes input from the user for the next move and checks validity
    def get_human_spot(self, player_symbol):
        spot = None
        while spot is None:
            print ("Enter [0-8]:")
            spot = input()
            while (not spot.isnumeric()):
                print("Invalid selection")
                print ("Enter [0-8]:")
                spot = input()   
            spot = int(spot)
            if spot not in range(0,9):
                spot = None
                print("Invalid no")
            elif(self.board[spot] != "X" and self.board[spot] != "O"):
                 self.board[spot] = player_symbol
            else:
                print("Invalid No")
                spot = None
          
    #method used to get the computer's move on medium level       
    def eval_board(self, player_symbol, opponent_symbol):
        time.sleep(2)
        spot = None
        while spot is None:
          if self.board[4] == "4":
            spot = 4
            self.board[spot] = player_symbol
          else:
            spot = self.get_best_move(self.board,player_symbol,opponent_symbol)
            if self.board[spot] != "X" and self.board[spot] != "O":
              self.board[spot] = player_symbol
              
            else:
              spot = None
              
    #method to be used inside eval_board..used for medium level play
    def get_best_move(self, board, player_symbol,opponent_symbol, depth = 0, best_score = {}):
        available_spaces = [s for s in board if s != "X" and s != "O"]
        best_move = None
    
        for avail in available_spaces:
          board[int(avail)] = player_symbol
          if self.game_is_over(board,player_symbol):
            best_move = int(avail)
            board[int(avail)] = avail
            return best_move
          else:
            board[int(avail)] = opponent_symbol
            if self.game_is_over(board,opponent_symbol):
              best_move = int(avail)
              board[int(avail)] = avail
              return best_move
            else:
              board[int(avail)] = avail
    
        if best_move:
          return best_move
        else:
          return int(available_spaces[0])
      
    #method to check if it is a tie
    def tie(self, b):
        if (len([s for s in b if s == "X" or s == "O"]) == 9):
            return True
        else: 
            return False

    #method to get computer's move for difficult level.. will use minmax 
    def minmax(self,newBoard,curr_player,player2):
        if self.board[4] == "4":
            return {"Score":0,"Index":4}
        score = 0
        available_spaces = [s for s in newBoard if s != "X" and s != "O"]   #available spots
        # checking for the conditions such as win, lose, and tie and returning a value accordingly
        if self.game_is_over(newBoard,self.player2symbol ):   # if the comp wins return +10
            return {"Score":10}
        elif(self.game_is_over(newBoard,self.player1symbol)):  # if the human wins return +10
            return {"Score":-10}
        elif(len(available_spaces)== 0):
            return {"Score":0}
        
        moves =[]   # moves to save all possible scores ..each element of it will be a list
        for i in available_spaces:
            i = int(i)
            score = 0
            index = newBoard[i]
            newBoard[i] = curr_player             #set the empty spot to current player
            
            if (curr_player == self.player2symbol):
                result = self.minmax (newBoard,self.player1symbol, self.player2symbol)   #player2symbol = comp
                score = result["Score"]
            else:
                result = self.minmax (newBoard, self.player2symbol,self.player1symbol)  #player2symbol = comp
                score = result["Score"]
            
            newBoard[i] = index               #resetting the spot to empty
            objmove= {"Score":score,"Index":index}
            moves.append(objmove)
        bestmove = -99999999
        bestscore = 0               
        #if it is the computer's turn loop over the moves and choose the move with the highest score
        if (curr_player == self.player2symbol):
            bestscore = -1000000
            for each in moves:                  #each will be a list
                key = int(each["Index"] )                           
                value = int(each["Score"])
                if value > bestscore:
                    bestscore = value
                    bestmove = key
        #loop over the moves and choose the move with the lowest score
        else:
            bestscore = 1000000
            for each in moves:
                key = int(each["Index"] )                           
                value = int(each["Score"])
                if value < bestscore:
                    bestscore = value
                    bestmove = key
        return {"Score":bestscore,"Index":bestmove}
    
    #method to check if either of the players has won
    def game_is_over(self, board, player_symbol):
        if (
                (board[0] == board[1] == board[2] == player_symbol) or
                (board[3] == board[4] == board[5] == player_symbol) or
                (board[6] == board[7] == board[8] == player_symbol) or
                (board[0] == board[3] == board[6] == player_symbol) or
                (board[1] == board[4] == board[7] == player_symbol) or
                (board[2] == board[5] == board[8] == player_symbol) or
                (board[0] == board[4] == board[8] == player_symbol) or
                (board[2] == board[4] == board[6] == player_symbol)
                ):
            return True;
        else:
            return False;
    
    #method to get computer's move for easy level..it will randomly pick from available spaces
    def random_play(self,player_symbol):
        time.sleep(2)
        available_spaces = [s for s in self.board if s != "X" and s != "O"]
        spot = random.choice(available_spaces)
        self.board[int(spot)] = player_symbol
        
                    
                    
            
                

if __name__ == '__main__':
  game = Game()
  game.start_game()
  print("THANK YOU FOR PLAYING!!!!!!")

        
    