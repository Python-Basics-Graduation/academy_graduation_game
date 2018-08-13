import pyglet
import game_board


window = pyglet.window.Window(1280, 720,
                              caption="Game",
                              resizable=False
                              )

background_batch = game_board.prepare_batch(
    window.width, window.height, 800, 450, 16, 9)
@window.event
def on_draw():
    window.clear()
    game_board.draw_background(background_batch)

if __name__ == '__main__':
    pyglet.app.run()
