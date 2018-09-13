import pyglet
import resources
from pyglet.window import mouse

path = '/Users/siczek/Python/final_game/git_repos/resources/'

class Cell(pyglet.sprite.Sprite):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.is_clicked = False

    @property
    def left(self):
        return self._x

    @property
    def right(self):
        return self._x + self.width

    @property
    def top(self):
        return self._y + self.height

    @property
    def bottom(self):
        return self._y

    def on_mouse_press(self, x, y):
        if self.left < x < self.right and self.bottom < y < self.top:
            self.is_clicked = True
            self.image = pyglet.image.load(path + 'marked_cell.png')

    def on_mouse_release(self, x, y):
        if self.left < x < self.right and self.bottom < y < self.top:
            if self.is_clicked:
                self.image = pyglet.image.load(path + 'clicked_cell.png')
        self.is_clicked = False


def prepare_batch(window_width, win_height, cell_size):
    batch = pyglet.graphics.Batch()
    position_x, position_y = calculate_board_position(
        window_width, win_height, cell_size)
    starting_point = position_x
    board = []
    for row_nr in range(9):
        for column_nr in range(16):
            game_board = Cell(
                resources.cell, x = position_x, y = position_y, batch = batch)
            board.append(game_board)
            position_x += cell_size
        position_x = starting_point
        position_y += cell_size
    return batch, board

def calculate_board_position(window_width, win_height, cell_size):
    board_position = []
    position_x = (window_width - cell_size * 16) // 2
    position_y = (win_height - cell_size * 9) * 3 // 4
    return position_x, position_y


def draw_background(batch):
    batch.draw()
