import pyglet

pyglet.resource.path = ["/Users/siczek/Python/final_game/git_repos/resources/"]
pyglet.resource.reindex()

cell = pyglet.resource.image("free_cell.png")
clicked_cell = pyglet.resource.image("clicked_cell.png")
marked_cell = pyglet.resource.image("marked_cell.png")
