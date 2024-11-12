#Sprites
import codesters

k = codesters.Sprite("kitten", 50, 0)
d = codesters.Sprite("KOA_Nassau_2697x1517.png", -50, 0)
k.set_size(1) 
d.set_size(0.1)



#movement
def move_up(sprite):
    sprite.move_up(5)

def move_left(sprite):
    sprite.move_left(5)

def move_right(sprite):
    sprite.move_right(5)

def move_down(sprite):
    sprite.move_down(5)

d.event_key("w", move_up)
d.event_key("s", move_down)
d.event_key("d", move_right)
d.event_key("a", move_left)

k.event_key("up", move_up)
k.event_key("down", move_down)
k.event_key("right", move_right)
k.event_key("left", move_left)

#drawing
def draw(sprite):
    sprite.pen_down()

def stop_drawing(sprite):
    sprite.pen_up()

def erase(sprite):
    sprite.pen_clear()

k.event_key("q", draw)
k.event_key("k", stop_drawing)
k.event_key("e", erase)

d.event_key("q", draw)
d.event_key("k", stop_drawing)
d.event_key("e", erase)

#show and hide

def hide(sprite):
    sprite.hide()

def show(sprite):
    sprite.show()





