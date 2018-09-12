import pyglet
import game_board
from pyglet.window import mouse


window = pyglet.window.Window(1280, 720,
                              caption="Game",
                              resizable=False
                              )


background_batch, cells = game_board.prepare_batch(1280, 720, 50)
@window.event
def on_draw():
    window.clear()

    game_board.draw_background(background_batch)


@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        for cell in cells:
            cell.on_mouse_press(x, y)

@window.event
def on_mouse_release(x, y, button, modifiers):
    if button == mouse.LEFT:
        for cell in cells:
            cell.on_mouse_release(x, y)

if __name__ == '__main__':
    pyglet.app.run()
