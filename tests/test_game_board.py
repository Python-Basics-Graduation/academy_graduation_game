from unittest import TestCase
import game_board

class GameBoardTest(TestCase):

    def test_calculate_board_position_with_correct_values(self):
        result = game_board.calculate_board_vertices(1280, 720, 800, 450)
        self.assertEqual(result, [[240, 202], [1040, 202], [1040, 652], [240, 652]])
    def test_calculate_board_position_with_incorrect_values(self):
        result = game_board.calculate_board_vertices(800, 450, 1280, 720,)
        self.assertEqual(result, [[240, 202], [1040, 202], [1040, 652], [240, 652]])
