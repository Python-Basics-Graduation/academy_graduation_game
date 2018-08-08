import pyglet
import resources
from pyglet.window import mouse


game_window = pyglet.window.Window(width=1240,height=720,caption="Simon's War",resizable=True)
cursor = pyglet.window.ImageMouseCursor(resources.cursor,16,8)
game_window.set_mouse_cursor(cursor)
label = pyglet.text.Label("SIMON'S WAR",
                          font_name='ARIAL',
                          font_size=36,
                          x=game_window.width//2, y=game_window.height//2,
                          anchor_x='center', anchor_y='center')

class Button(pyglet.sprite.Sprite):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


@game_window.event
def on_draw():
    game_window.clear()
    button.draw()

@game_window.event
def on_mouse_release(x, y, button, modifiers):
    label.draw()

def update(dt):
    pass

if __name__ == '__main__':
    button = Button(resources.start,x=game_window.width//3)

    pyglet.clock.schedule_interval(update, 0.001)
    pyglet.app.run()
