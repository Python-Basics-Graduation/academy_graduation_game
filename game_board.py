import pyglet
import resources
from pyglet.window import mouse

path = '/Users/siczek/Python/final_game/git_repos/resources/'
background = pyglet.graphics.OrderedGroup(0)
middleground = pyglet.graphics.OrderedGroup(1)
foreground = pyglet.graphics.OrderedGroup(2)


class Cell(pyglet.sprite.Sprite):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.is_clicked = False
        self.active = True

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
        if (self.active
                and self.left < x < self.right
                and self.bottom < y < self.top):
            self.is_clicked = True
            self.image = pyglet.image.load(path + 'marked_cell.png')

    def on_mouse_release(self, x, y):
        if (self.active
                and self.left < x < self.right
                and self.bottom < y < self.top):
            if self.is_clicked:
                self.image = pyglet.image.load(path + 'clicked_cell.png')
        self.is_clicked = False


def prepare_batch(window_width, win_height, cell_size):
    batch = pyglet.graphics.Batch()
    position_x, position_y = calculate_board_position(
        window_width, win_height, cell_size)
    #board []- 2 board vertices: bottom-left corner (x,y) and top-right(x,y)
    board_vertices = [
        position_x,
        position_y,
        position_x + cell_size * 16,
        position_y + cell_size * 9
        ]
    board = []
    for row_nr in range(9):
        for column_nr in range(16):
            game_board = Cell(
                resources.cell, x = position_x, y = position_y,
                batch = batch, group = background)
            board.append(game_board)
            position_x += cell_size
        position_x = board_vertices[0]
        position_y += cell_size
    add_grey_screen_to_batch(board_vertices, batch)
    add_red_line_to_batch(board_vertices, batch)
    return batch, board


def calculate_board_position(window_width, win_height, cell_size):
    board_position = []
    position_x = (window_width - cell_size * 16) // 2
    position_y = (win_height - cell_size * 9) * 3 // 4
    return position_x, position_y

def add_grey_screen_to_batch(board_vertices, batch):
    batch.add(
        4,
        pyglet.gl.GL_QUADS,
        middleground,
        ('v2i', (
            board_vertices[0],
            board_vertices[1],
            board_vertices[2],
            board_vertices[1],
            board_vertices[2],
            board_vertices[3],
            board_vertices[0],
            board_vertices[3])),
        ('c3B',(150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150))
        )

def add_red_line_to_batch(board_vertices, batch):
    """
    Args:
        board (array) - 4 digits representing 2 vertices(x,y) of the board:
            bottom - left
            top - right
    Result:
        Printing Red vertical line in the middle of the board, Red line is 50 px
            longer on each side
    """
    start_x = (board_vertices[2] - board_vertices[0]) // 2 + board_vertices[0]
    start_y = board_vertices[1] - 50
    end_x = start_x
    end_y = board_vertices[3] + 50
    pyglet.gl.glLineWidth(3)
    batch.add(
            2,
            pyglet.gl.GL_LINES,
            foreground,
            ('v2i',
            (start_x, start_y, end_x, end_y)),
            ('c3B',(255, 0, 0, 255, 0, 0))
        )

def draw_background(batch):
    batch.draw()
