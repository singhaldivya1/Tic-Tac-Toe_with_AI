# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 01:12:46 2018

@author: singh
"""

import io
import sys
import unittest
import unittest.mock
from Board import Board




class TestTicTacToeBoard(unittest.TestCase):
    def test_BoardClass(self):
        game_board = Board()
        self.assertIsInstance(game_board,Board)
        
    def test_getBoard(self):
        game_board = Board()
        self.assertEqual(game_board.getBoard(), ['0', '1', '2', '3', '4', '5', '6', '7', '8'])
    
    def test_getSymbol(self):
        game_board = Board()
        self.assertEqual(game_board.getSymbol(5), '5')
        
    def test_setSymbol(self):
        game_board = Board()
        game_board.setSymbol(4,'X')
        self.assertEqual(game_board.getSymbol(4), 'X')
        
    def test_game_is_over_horizontal_true(self):
        game_board = Board()
        game_board.board = ["X", "X", "X", "X", "O", "O", "O", "X", "O"]
        self.assertTrue(game_board.game_is_over("X"))
    
    def test_game_is_over_diagonal_true(self):
        game_board = Board()
        game_board.board = ["X", "O", "X", "O", "X", "O", "O", "O", "X"]
        self.assertTrue(game_board.game_is_over("X"))
        
    
    
    def test_setup(self):
        game_board = Game()
        self.assertIsInstance(game_board,Game)
    
    def test_game_is_over_vertical_true(self):
        game_board = Board()
        game_board.board = ["X", "O", "X", "X", "O", "O", "X", "X", "O"]
        self.assertTrue(game_board.game_is_over("X"))
        
    def test_game_is_over_false(self):
        game_board = Board()
        game_board.board = ["O", "O", "X", "X", "X", "O", "O", "X", "X"]
        self.assertFalse(game_board.game_is_over("X"))
        
    def test_tie_true(self):
        game_board = Board()
        game_board.board = ["O", "O", "X", "X", "X", "O", "O", "X", "X"]
        self.assertTrue(game_board.tie())
    
    def test_tie_false(self):
        game_board = Board()
        game_board.board = ["X", "O", "X", "X", "O", "O", "X", "X", "8"]
        self.assertFalse(game_board.tie())
    
    def test_reset_board(self):
        game_board = Board()
        game_board.board = ["X", "O", "X", "X", "O", "O", "X", "X", "8"]
        game_board.reset_board()
        self.assertEqual(game_board.getBoard(),['0', '1', '2', '3', '4', '5', '6', '7', '8'])
        
    
if __name__ == "__main__":
    #unittest.main()
    suit = unittest.TestLoader().loadTestsFromTestCase(TestTicTacToeBoard)
    unittest.TextTestRunner(verbosity=2).run(suit)
