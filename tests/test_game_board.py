from unittest import TestCase
import game_board


class GameBoardTest(TestCase):

    def test_calculate_board_position_with_correct_values(self):
        result = game_board.calculate_board_vertices(1280, 720, 800, 450)
        self.assertEqual(result, [[240, 202], [1040, 202],
                                  [1040, 652], [240, 652]])

    def test_calculate_board_position_with_incorrect_values(self):
        with self.assertRaises(ValueError):
            game_board.calculate_board_vertices(800, 450, 1280, 720)

    def test_calculate_board_position_same_size_even(self):
        result = game_board.calculate_board_vertices(800, 450, 800, 450)
        self.assertEqual(result, [[0, 0], [800, 0], [800, 450], [0, 450]])

    def test_calculate_board_position_same_size_odd(self):
        result = game_board.calculate_board_vertices(801, 451, 801, 451)
        self.assertEqual(result, [[0, 0], [801, 0], [801, 451], [0, 451]])

    def test_calculate_board_position_1_px_size_difference(self):
        result = game_board.calculate_board_vertices(801, 451, 800, 450)
        self.assertEqual(result, [[0, 0], [800, 0], [800, 450], [0, 450]])

    def test_calculate_cell_size_correct_values(self):
        result = game_board.calculate_cell_size(800, 450, 16, 9)
        self.assertEqual(result, 50)

    def test_calculate_cell_size_incorrect_cell_is_not_square(self):
        with self.assertRaises(ValueError):
            game_board.calculate_cell_size(800, 400, 16, 10)

    def test_calculate_cell_size_incorrect_modulo_is_not_zero(self):
        with self.assertRaises(ValueError):
            game_board.calculate_cell_size(801, 450, 16, 9)
