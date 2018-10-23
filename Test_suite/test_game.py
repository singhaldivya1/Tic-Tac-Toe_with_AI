# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 03:17:05 2018

@author: singh
"""

class TestTicTacToeGame(unittest.TestCase):
    
    def test_GameClass(self):
        game = Game()
        self.assertIsInstance(game,Game)
        
    def test_set_game_mode(self):
        game = Game()
        with unittest.mock.patch('builtins.input', return_value="1"):
            game.set_game_mode()  
        self.assertEqual(game.game_mode,1 )
        
    def test_get_player_symbol(self):
        game = Game()
        with unittest.mock.patch('builtins.input', return_value="X"):
            game.get_player_symbol()  
        self.assertEqual(game.player1symbol,"X")
    
    def test_get_player_symbol(self):
        game = Game()
        with unittest.mock.patch('builtins.input', return_value="O"):
            game.get_player_symbol()  
        self.assertEqual(game.player2symbol,"X")
        
    def test_set_plays_first(self):
        game = Game()
        with unittest.mock.patch('builtins.input', return_value="1"):
            game.set_plays_first()  
        self.assertTrue(game.isPlayer1First)
    
    def test_set_plays_first(self):
        game = Game()
        with unittest.mock.patch('builtins.input', return_value="0"):
            game.set_plays_first()  
        self.assertFalse(game.isPlayer1First)
        
    def test_set_difficulty(self):
        game = Game()
        with unittest.mock.patch('builtins.input', return_value="1"):
            game.set_difficulty()  
        self.assertEqual(game.difficulty,1 )
   
if __name__ == "__main__":
    suit = unittest.TestLoader().loadTestsFromTestCase(TestTicTacToeGame)
    unittest.TextTestRunner(verbosity=2).run(suit)