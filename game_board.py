import pyglet
from pyglet.window import mouse

window = pyglet.window.Window(1000, 600,
                caption="Game",
                resizable=False
            )
def draw_board():
    batch = pyglet.graphics.Batch()

    pyglet.gl.glLineWidth(1)

    batch.add(4, pyglet.gl.GL_QUADS, None,
        ('v2i', (100, 100,
                 900, 100,
                 900, 550,
                 100, 550))
    )
    for hor_line in range(1,9):
        batch.add(2, pyglet.gl.GL_LINES, None,
            ('v2i', (100, 100 + 50*hor_line,
                     900, 100 + 50*hor_line)),
            ('c3B', (0, 0, 255, 0, 0, 255))
            )
    for ver_line in range(1,16):
        batch.add(2, pyglet.gl.GL_LINES, None,
            ('v2i', (100 + 50*ver_line, 100,
                     100 + 50*ver_line, 550)),
            ('c3B', (0, 0, 255, 0, 0, 255))
            )
    batch.draw()

@window.event
def on_draw():
    window.clear()
    draw_board()


@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        pass

def on_mouse_enter(x, y):
    pass

def on_mouse_leave(x, y):
    pass

def calculate_board_size(length, width):
    pass

def calculate_cell_size(length, width):
    pass


if __name__ == '__main__':
    pyglet.app.run()
