import pyglet
from pyglet.window import mouse
from pyglet_gui.theme import Theme

cell_size = 50

class Cell:
    def __init__(self, position_x, position_y, cell_size, state):
        self.position_x = position_x    #position is bottom left corner
        self.position_y = position_y
        self.cell_size = cell_size
        self.state = state

    def add_cell_to_batch(self, batch):
        left = self.position_x
        right = self.position_x + self.cell_size
        bottom = self.position_y
        top = self.position_y + self.cell_size

        vertex_list = batch.add(5, pyglet.gl.GL_LINE_STRIP, None,
        ('v2i', (left, bottom,
                right, bottom,
                right, top,
                left, top,
                left, bottom)),
        ('c3B', (0, 0, 255, 0, 0, 255, 0, 0, 255, 0, 0, 255, 0, 0, 255)))


def draw_background(win_width, win_height, board_width, board_height):
    board_vertices = calculate_board_vertices(win_width, win_height, board_width, board_height)
    batch = pyglet.graphics.Batch()
    draw_board(board_vertices, batch)
    draw_cells(board_vertices[0][0], board_vertices[0][1], cell_size, batch)
    batch.draw()

def draw_board(board_vertices, batch):
    batch.add(4, pyglet.gl.GL_QUADS, None,
        ('v2i', (board_vertices[0][0], board_vertices[0][1],
                 board_vertices[1][0], board_vertices[1][1],
                 board_vertices[2][0], board_vertices[2][1],
                 board_vertices[3][0], board_vertices[3][1]))
    )


def draw_cells(board_left, board_bottom, cell_size, batch):
    position_x = board_left
    position_y = board_bottom
    for column in range(9):
        for row in range(16):
            cell = Cell(position_x, position_y, cell_size, 0)
            cell.add_cell_to_batch(batch)
            position_x += cell_size
        position_x = board_left

#the drawing cursor must return to the starting position of the new row:
        batch.add(1, pyglet.gl.GL_LINE_STRIP, None,
        ('v2i', (position_x, position_y)),
        ('c3B', (0, 0, 255)))

        position_y += cell_size



def calculate_board_vertices(win_width, win_height, board_width, board_height):
    if (win_width >= board_width) & (win_height >= board_height):
        left = (win_width - board_width) // 2
        right = left + board_width
        bottom = (win_height - board_height) * 3 // 4
        top = bottom + board_height
        board_vertices = [
                [left, bottom],
                [right, bottom],
                [right, top],
                [left, top]
        ]
        return board_vertices
    else:
         raise ValueError("The Window size must be bigger than the Board size")

if __name__ == '__main__':
    pyglet.app.run()
