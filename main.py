import pyglet
import game_board


window = pyglet.window.Window(1280, 720,
                caption="Game",
                resizable=False
            )


@window.event
def on_draw():
    window.clear()
    game_board.draw_board(window.width, window.height, 800, 450)

if __name__ == '__main__':
    pyglet.app.run()
