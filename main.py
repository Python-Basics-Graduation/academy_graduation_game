import pyglet
import resources
from pyglet.window import mouse


game_window = pyglet.window.Window(width=1240,height=720,caption="Simon's War",resizable=False)
# game_window.push_handlers(pyglet.window.event.WindowEventLogger())
cursor = pyglet.window.ImageMouseCursor(resources.cursor,16,8)
game_window.set_mouse_cursor(cursor)
label = pyglet.text.Label("SIMON'S WAR",
                          font_name='ARIAL',
                          font_size=36,
                          x=game_window.width//2, y=game_window.height//2,
                          anchor_x='center', anchor_y='center')

# TODO: Move this to another file
class Button(pyglet.sprite.Sprite):
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

    def on_mouse_release(self, x, y):
        if self.left < x < self.right and self.bottom < y < self.top:
            if self.is_clicked:
                print("teraz serio dziala")
        self.is_clicked = False


# TODO: Make this sane
buttons = []
button_menu = Button(resources.start, x=game_window.width//3)
buttons.append(button_menu)


@game_window.event
def on_draw():
    game_window.clear()
    for button_menu in buttons:
        button_menu.draw()

@game_window.event
def on_mouse_press(x, y, button, modifiers):
    # TODO: Check if left mouse?
    for button_menu in buttons:
        button_menu.on_mouse_press(x, y)

@game_window.event
def on_mouse_release(x, y, button, modifiers):
    for button_menu in buttons:
        button_menu.on_mouse_release(x, y)
    # TODO: Check if left mouse?


def update(dt):
    pass

if __name__ == '__main__':

    pyglet.clock.schedule_interval(update, 0.001)
    pyglet.app.run()
