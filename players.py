# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 01:52:49 2018

@author: singh
"""

class Player:
    
    def __init__(self,gameboard, player_symbol):
        self.board = gameboard
        self.symbol = player_symbol
     
    # to ask for human move   
    def make_move(self):
        spot = None
        while spot is None:
            print ("Enter [0-8]:")
            spot = input()
            while (not spot.isnumeric()):
                print("Invalid input : Input is not numeric")
                print ("Enter [0-8]:")
                spot = input()   
            spot = int(spot)
            if spot not in range(0,9):
                spot = None
                print("Invalid input : Input is not in range [0,9]")
            elif(self.board.getSymbol(spot) != "X" and self.board.getSymbol(spot) != "O"):
                 self.board.setSymbol(spot, self.symbol)
            else:
                print("Invalid input : Already occupied place")
                spot = None
        