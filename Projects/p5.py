# Section 1 - Setup
import codesters, random
from codesters import StageClass
stage = StageClass()
stage.set_background("hauntedhouse")


b = codesters.Sprite("bat")
b.set_size(0.15)
b.go_to(0,-200)
stage.disable_floor()


gameOver = False
lives = 4


# Baseball falling
def falling_object():
    global gameOver
    if not gameOver:
        x_position = random.randint(-250,250)
        object = codesters.Sprite("baseball", x_position, 250)
        object.set_size(0.4)
        object.set_y_speed(-5)
   
stage.event_interval(falling_object, 3)


# Collision
def collision(s1, s2):
    global lives, gameOver
   
    if s2.get_image_name() == "baseball":
        stage.remove_sprite(s2)
        if lives == 0:
            gameOver = True
            b.go_to(0, -200)
            b.say("Game over")
        else:
            lives -= 1 
            b.say("Ouch!", 1)

b.event_collision(collision)


# Controls

def hide(sprite): 
    sprite.hide()

def move_up(sprite):
    if lives > 0:
        b.move_up(5)
b.event_key("w", move_up)


def move_down(sprite):
    if lives > 0:
        b.move_down(5)
b.event_key("s", move_down)

def move_right(sprite):
    if lives > 0:
        b.move_right(5)
b.event_key("d", move_right)

def move_left(sprite):
    if lives > 0:
        b.move_left(5)
b.event_key("a", move_left)
