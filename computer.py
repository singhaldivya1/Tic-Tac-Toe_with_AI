# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 01:08:38 2018

@author: singh
"""
from players import Player
import random
import time

class Computer(Player):
    
    def __init__(self,board,symbol,mode):
        Player.__init__(self,board,symbol)
        self.game_mode = mode
        self.player2Symbol = 'X'
        if (symbol == 'X'):
            self.player2Symbol = 'O'
      # to make move according to the difficulty level 
    def make_move(self):
        if self.game_mode == 1:         #easy
            self.random_play()
        elif self.game_mode == 2:       #medium
            self.eval_board()
        else:                           #hard
            best_move = self.minmax(self.symbol)
            self.board.setSymbol(best_move["Index"], self.symbol)

            
    # used in easy mode
    def random_play(self):
        time.sleep(2)
        available_spaces = [s for s in self.board.getBoard() if s != "X" and s != "O"]
        spot = random.choice(available_spaces)
        self.board.setSymbol(int(spot), self.symbol)
    
    #method to get computer's move for difficult level.. will use minmax 
    def minmax(self,curr_player):
        if self.board.getSymbol(4) == "4":
            return {"Score":0,"Index":4}
        score = 0
        available_spaces = [s for s in self.board.getBoard() if s != "X" and s != "O"]   #available spots
        # checking for the conditions such as win, lose, and tie and returning a value accordingly
        if self.board.game_is_over(self.symbol):   # if the comp wins return +10
            return {"Score":10}
        elif(self.board.game_is_over(self.player2Symbol)):  # if the human wins return +10
            return {"Score":-10}
        elif(len(available_spaces) == 0):
            return {"Score":0}
        
        moves =[]   # moves to save all possible scores ..each element of it will be a list
        for i in available_spaces:
            i = int(i)
            score = 0
            index = self.board.getSymbol(i)
            self.board.setSymbol(i,curr_player)             #set the empty spot to current player
            
            if (curr_player == self.symbol):
                result = self.minmax (self.player2Symbol)   #player2symbol = comp
                score = result["Score"]
            else:
                result = self.minmax (self.symbol)  #player2symbol = comp
                score = result["Score"]
            
            self.board.setSymbol(i, index)       #resetting the spot to empty
            objmove= {"Score":score,"Index":index}
            moves.append(objmove)
        bestmove = -99999999
        bestscore = 0               
        #if it is the computer's turn loop over the moves and choose the move with the highest score
        if (curr_player == self.symbol):
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
    
    #method used to get the computer's move on medium level       
    def eval_board(self):
        time.sleep(2)
        spot = None
        while spot is None:
          if self.board.getSymbol(4) == "4":
            spot = 4
            self.board.setSymbol(spot, self.symbol)
          else:
            spot = self.get_best_move()
            if self.board.getSymbol(spot) != "X" and self.board.getSymbol(spot) != "O":
              self.board.setSymbol(spot, self.symbol)
            else:
              spot = None
              
    #method to be used inside eval_board..used for medium level play
    def get_best_move(self):
        available_spaces = [s for s in self.board.getBoard() if s != "X" and s != "O"]
        best_move = None
    
        for avail in available_spaces:
          self.board.setSymbol(int(avail), self.symbol)
          if self.board.game_is_over(self.symbol):
            best_move = int(avail)
            self.board.setSymbol(int(avail), avail)
            return best_move
          else:
            self.board.setSymbol(int(avail), self.player2Symbol)
            if self.board.game_is_over(self.player2Symbol):
              best_move = int(avail)
              self.board.setSymbol(int(avail), avail)
              return best_move
            else:
              self.board.setSymbol(int(avail), avail)
    
        if best_move:
          return best_move
        else:
          return int(available_spaces[0])
        
        
    