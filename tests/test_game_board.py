from unittest import TestCase
import game_board

class GameBoardTest(TestCase):

    def test_calculate_board_position_with_correct_values(self):
        result = game_board.calculate_board_position(1280, 720, 50)
        self.assertEqual(result, (240, 202))
