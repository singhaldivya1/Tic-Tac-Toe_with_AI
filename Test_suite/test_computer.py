# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 02:53:59 2018

@author: singh
"""

import io
import sys
import unittest
import unittest.mock
from Board import Board
from Computer import Computer
from Players import Player



class TestTicTacToeComputer(unittest.TestCase):
    
    def test_ComputerClass(self):
        game_board = Board()
        game_player = Computer(game_board,"X",1)
        self.assertIsInstance(game_player,Computer)
    
    def test_ComputerSymbol(self):
        game_board = Board()
        game_player = Computer(game_board,"X",2)
        self.assertEqual(game_player.symbol,"X")
    
    def test_ComputerBoard(self):
        game_board = Board()
        game_player = Computer(game_board,"X",3)
        self.assertEqual(game_player.board, game_board)
        
    def test_ComputerGameMode(self):
        game_board = Board()
        game_player = Computer(game_board,"X",2)
        self.assertEqual(game_player.game_mode,2)
    
    def test_Player2Symbol(self):
        game_board = Board()
        game_player = Computer(game_board,"X",3)
        self.assertEqual(game_player.player2Symbol, "O")

    def test_random_play(self):
        game_board = Board()
        game_player = Computer(game_board,"X",1)
        game_board.board = ["X", "O", "X", "X", "O", "5", "O", "7", "8"]
        game_player.random_play()
        self.assertIn(game_player.board.getBoard(),[["X", "O", "X", "X", "O", "X", "O", "7", "8"]\
                                        ,["X", "O", "X", "X", "O", "5", "O", "X", "8"]\
                                        ,["X", "O", "X", "X", "O", "5", "O", "7", "X"]])
    
    def test_eval_board(self):
        game_board = Board()
        game_player = Computer(game_board,"X",2)
        game_board.board = ["X", "O", "X", "X", "4", "5", "O", "7", "8"]
        game_player.eval_board()
        self.assertEqual(game_player.board.getBoard(),["X", "O", "X", "X", "X", "5", "O", "7", "8"])
      
    def test_get_best_move(self):
        game_board = Board()
        game_player = Computer(game_board,"X",2)
        game_board.board = ["X", "1", "X", "3", "O", "5", "6", "7", "8"]
        self.assertEqual(game_player.get_best_move(), 1)
#    
    
    def test_minmax(self):
        game_board = Board()
        game_player = Computer(game_board,"X",3)
        game_board.board = ["X", "X", "O", "O", "O", "5", "X", "O", "X"]
        result = game_player.minmax("O")
        self.assertEqual(result["Index"],5)
        
        
    def test_makeMoveEasy(self):
        game_board = Board()
        game_player = Computer(game_board,"X",1)
        game_board.board = ["X", "O", "X", "X", "O", "5", "O", "7", "8"]
        game_player.make_move()
        self.assertIn(game_player.board.getBoard(),[["X", "O", "X", "X", "O", "X", "O", "7", "8"]\
                                        ,["X", "O", "X", "X", "O", "5", "O", "X", "8"]\
                                        ,["X", "O", "X", "X", "O", "5", "O", "7", "X"]])
    
    
    def test_makeMoveMedium(self):
        game_board = Board()
        game_player = Computer(game_board,"X",2)
        game_board.board = ["X", "O", "X", "X", "4", "5", "O", "7", "8"]
        game_player.make_move()
        self.assertEqual(game_player.board.getBoard(),["X", "O", "X", "X", "X", "5", "O", "7", "8"])
      
#    
    
    def test_makeMoveDifficult(self):
        game_board = Board()
        game_player = Computer(game_board,"X",3)
        game_board.board = ["X", "X", "O", "O", "O", "5", "X", "O", "X"]
        game_player.make_move()
        self.assertEqual(game_player.board.getSymbol(5),"X")
        
        
if __name__ == "__main__":
    suit = unittest.TestLoader().loadTestsFromTestCase(TestTicTacToeComputer)
    unittest.TextTestRunner(verbosity=2).run(suit)