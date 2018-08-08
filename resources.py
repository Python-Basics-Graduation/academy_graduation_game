import pyglet

pyglet.resource.path = ["resources"]
pyglet.resource.reindex()

start = pyglet.resource.image("start.png")
cursor = pyglet.resource.image("cursor.png")
