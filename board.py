# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 02:36:14 2018

@author: singh
"""

class Board:

    def __init__(self):
        self.board =  None
        self.reset_board()
    
    
    def getBoard(self):
        return self.board
            
    def getSymbol(self, position):
        return self.board[position]
    
    def setSymbol(self, position, symbol):
        self.board[position] = symbol
    
    #method to check if either of the players has won
    def game_is_over(self, player_symbol):
        if (
                (self.board[0] == self.board[1] == self.board[2] == player_symbol) or
                (self.board[3] == self.board[4] == self.board[5] == player_symbol) or
                (self.board[6] == self.board[7] == self.board[8] == player_symbol) or
                (self.board[0] == self.board[3] == self.board[6] == player_symbol) or
                (self.board[1] == self.board[4] == self.board[7] == player_symbol) or
                (self.board[2] == self.board[5] == self.board[8] == player_symbol) or
                (self.board[0] == self.board[4] == self.board[8] == player_symbol) or
                (self.board[2] == self.board[4] == self.board[6] == player_symbol)
                ):
            return True;
        else:
            return False;
    
    
    #method to check if it is a tie (Method is called only after calling game_is_over())
    def tie(self):
        if (len([s for s in self.board if s == "X" or s == "O"]) == 9):
            return True
        else: 
            return False
        
    #method to reset the board
    def reset_board(self):
        self.board = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
        
    def __repr__(self):
        return  "['%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s']" % \
            (self.board[0], self.board[1], self.board[2],
                 self.board[3], self.board[4], self.board[5],
                 self.board[6], self.board[7], self.board[8])

    def __str__(self):
        return " %s | %s | %s \n===+===+===\n %s | %s | %s \n===+===+===\n %s | %s | %s \n" % \
            (self.board[0], self.board[1], self.board[2],
                 self.board[3], self.board[4], self.board[5],
                 self.board[6], self.board[7], self.board[8])
    