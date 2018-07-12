import pyglet
from pyglet.window import mouse


def draw_board(win_width, win_height, board_width, board_height):
    board_vertices = calculate_board_vertices(win_width, win_height, board_width, board_height)

    batch = pyglet.graphics.Batch()

    pyglet.gl.glLineWidth(1)

    batch.add(4, pyglet.gl.GL_QUADS, None,
        ('v2i', (board_vertices[0][0], board_vertices[0][1],
                 board_vertices[1][0], board_vertices[1][1],
                 board_vertices[2][0], board_vertices[2][1],
                 board_vertices[3][0], board_vertices[3][1]))
    )
    for hor_line in range(1,9):
        batch.add(2, pyglet.gl.GL_LINES, None,
            ('v2i', (board_vertices[0][0], board_vertices[0][1] + 50*hor_line,
                     board_vertices[1][0], board_vertices[1][1] + 50*hor_line)),
            ('c3B', (0, 0, 255, 0, 0, 255))
            )
    for ver_line in range(1,16):
        batch.add(2, pyglet.gl.GL_LINES, None,
            ('v2i', (board_vertices[0][0] + 50*ver_line, board_vertices[0][1],
                     board_vertices[3][0] + 50*ver_line, board_vertices[3][1])),
            ('c3B', (0, 0, 255, 0, 0, 255))
            )
    batch.draw()



def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        pass

def on_mouse_enter(x, y):
    pass

def on_mouse_leave(x, y):
    pass


def calculate_board_size(width, height):
    pass

def calculate_board_vertices(win_width, win_height, board_width, board_height):
    if (win_width > board_width) & (win_height > board_height):
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

def calculate_cell_size(width, height):
    pass


def calculate_current_cell_vertices(x_pointer, y_pointer, board_vertices, cell_size):
    pass



if __name__ == '__main__':
    pyglet.app.run()
