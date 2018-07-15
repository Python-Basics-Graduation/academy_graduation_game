import pyglet


class Cell:
    def __init__(self, position_x, position_y, cell_size, state):
        self.position_x = position_x    # position is bottom left corner
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
                                ('c3B', (0, 0, 255,
                                         0, 0, 255,
                                         0, 0, 255,
                                         0, 0, 255,
                                         0, 0, 255)))


def draw_background(win_width, win_height,
                    board_width, board_height, columns_num, rows_num):
    board_vertices = calculate_board_vertices(win_width, win_height,
                                              board_width, board_height)
    cell_size = calculate_cell_size(board_width, board_height,
                                    columns_num, rows_num)
    batch = pyglet.graphics.Batch()
    draw_board(board_vertices, batch)
    draw_cells(board_vertices[0][0], board_vertices[0][1],
               cell_size, columns_num, rows_num, batch)
    batch.draw()


def calculate_cell_size(board_width, board_height, columns_num, rows_num):
    if (board_width // columns_num == board_height // rows_num and
            board_width % columns_num == 0 and
            board_height % rows_num == 0):
        cell_size = board_width // columns_num
        return cell_size
    else:
        raise ValueError("Incorrect board dimensions or numbers of "
                         "columns/rows. Cells must be square.")


def draw_board(board_vertices, batch):
    batch.add(4, pyglet.gl.GL_QUADS, None,
              ('v2i', (board_vertices[0][0], board_vertices[0][1],
                       board_vertices[1][0], board_vertices[1][1],
                       board_vertices[2][0], board_vertices[2][1],
                       board_vertices[3][0], board_vertices[3][1]))
              )


def draw_cells(board_left, board_bottom, cell_size,
               columns_num, rows_num, batch):
    position_x = board_left
    position_y = board_bottom
    for column in range(rows_num):
        for row in range(columns_num):
            cell = Cell(position_x, position_y, cell_size, 0)
            cell.add_cell_to_batch(batch)
            position_x += cell_size
        position_x = board_left

# the drawing cursor must return to the starting position of the new row:
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
