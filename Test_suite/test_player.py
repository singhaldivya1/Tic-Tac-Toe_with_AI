# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 02:43:28 2018

@author: singh
"""

import io
import sys
import unittest
import unittest.mock
from Board import Board
from Players import Player



class TestTicTacToePlayer(unittest.TestCase):
    
    def test_PlayerClass(self):
        game_board = Board()
        game_player = Player(game_board,"X")
        self.assertIsInstance(game_player,Player)
    
    def test_PlayerSymbol(self):
        game_board = Board()
        game_player = Player(game_board,"X")
        self.assertEqual(game_player.symbol,"X")
    
    def test_PlayerBoard(self):
        game_board = Board()
        game_player = Player(game_board,"X")
        self.assertEqual(game_player.board, game_board)
        
    def test_makeMove(self):
        game_board = Board()
        game_player = Player(game_board,"X")
        with unittest.mock.patch('builtins.input', return_value="7"):
            game_player.make_move()        
        self.assertEqual(game_player.board.getSymbol(7),"X" )
    
    
    
if __name__ == "__main__":
    suit = unittest.TestLoader().loadTestsFromTestCase(TestTicTacToePlayer)
    unittest.TextTestRunner(verbosity=2).run(suit)