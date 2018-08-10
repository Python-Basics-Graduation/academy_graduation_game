import pyglet
from pyglet.window import mouse

window = pyglet.window.Window()
window.push_handlers(pyglet.window.event.WindowEventLogger())

@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        print("L m was presed")
    elif button == mouse.RIGHT:
        print("R m was presed")

@window.event
def on_draw():
    window.clear()

pyglet.app.run()
