import pyglet

window = pyglet.window.Window(500, 650)
batch = pyglet.graphics.Batch()
elementos = []
etiquetas = []

elementos.append(pyglet.shapes.Rectangle(20,500,460,135,color=(255,255,255),batch=batch))
etiquetas.append(pyglet.text.Label( "x = 1.23456789 = y",
                                    font_name="Courier New",
                                    font_size=12,
                                    x = 22,
                                    y = 590,
                                    color=(255,20,15)

))

@window.event
def on_draw():
    window.clear()
    batch.draw()
    for label in etiquetas:
        label.draw()



pyglet.app.run()

