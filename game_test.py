# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 01:12:46 2018

@author: singh
"""

import io
import sys
import unittest
import unittest.mock
from game import Game, GameMode


class TestTicTacToe(unittest.TestCase):
    def test_setup(self):
        game_board = Game()
        self.assertIsInstance(game_board,Game)
    
    def test_printing(self):
        game_board = Game()
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        game_board.printing()
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue()," 0 | 1 | 2 \n===+===+===\n 3 | 4 | 5 \n===+===+===\n 6 | 7 | 8 \n\n")
        
    def test_get_human_spot(self):
        game_board = Game()
        game_board.board = ["X", "O", "X", "X", "O", "5", "O", "7", "8"]
        
        with unittest.mock.patch('builtins.input', return_value="7"):
            game_board.get_human_spot("X")
            
        self.assertEqual(game_board.board, ["X", "O", "X", "X", "O", "5", "O", "X", "8"])
        
    def test_eval_board(self):
        game_board = Game()
        game_board.board = ["X", "O", "X", "X", "4", "5", "O", "7", "8"]
        game_board.eval_board("O","X")
        self.assertEqual(game_board.board,["X", "O", "X", "X", "O", "5", "O", "7", "8"])
      
    def test_get_best_move(self):
        game_board = Game()
        game_board.board = ["X", "1", "X", "3", "O", "5", "6", "7", "8"]
        self.assertEqual(game_board.get_best_move(game_board.board,"X","O"), 1)
    
    
    def test_tie_true(self):
        game_board = Game()
        game_board.board = ["O", "O", "X", "X", "X", "O", "O", "X", "X"]
        self.assertTrue(game_board.tie(game_board.board))
    
    def test_tie_false(self):
        game_board = Game()
        game_board.board = ["X", "O", "X", "X", "O", "O", "X", "X", "8"]
        self.assertFalse(game_board.tie(game_board.board))
        
    def test_minmax(self):
        game_board = Game()
        game_board.board = ["X", "X", "O", "O", "O", "5", "X", "O", "X"]
        result = game_board.minmax(game_board.board,"O","X")
        self.assertEqual(result["Index"],5)
        
    def test_game_is_over_horizontal_true(self):
        game_board = Game()
        game_board.board = ["X", "X", "X", "X", "O", "O", "O", "X", "O"]
        self.assertTrue(game_board.game_is_over(game_board.board, "X"))
        
    def test_game_is_over_diagonal_true(self):
        game_board = Game()
        game_board.board = ["X", "O", "X", "O", "X", "O", "O", "O", "X"]
        self.assertTrue(game_board.game_is_over(game_board.board, "X"))
        
    def test_game_is_over_vertical_true(self):
        game_board = Game()
        game_board.board = ["X", "O", "X", "X", "O", "O", "X", "X", "O"]
        self.assertTrue(game_board.game_is_over(game_board.board, "X"))
        
    def test_game_is_over_false(self):
        game_board = Game()
        game_board.board = ["O", "O", "X", "X", "X", "O", "O", "X", "X"]
        self.assertFalse(game_board.game_is_over(game_board.board, "X"))
    
    def test_random_play(self):
        game_board = Game()
        game_board.board = ["X", "O", "X", "X", "O", "5", "O", "7", "8"]
        game_board.random_play("X")
        self.assertIn(game_board.board,[["X", "O", "X", "X", "O", "X", "O", "7", "8"]\
                                        ,["X", "O", "X", "X", "O", "5", "O", "X", "8"]\
                                        ,["X", "O", "X", "X", "O", "5", "O", "7", "X"]])
    
    
if __name__ == "__main__":
    #unittest.main()
    suit = unittest.TestLoader().loadTestsFromTestCase(TestTicTacToe)
    unittest.TextTestRunner(verbosity=2).run(suit)
