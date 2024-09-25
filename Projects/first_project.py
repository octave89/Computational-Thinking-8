###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################

# shapes
s1 = codesters.Circle(100, 100, 200, 'blue')
s1 = codesters.Circle(-150, -150)
s2 = codesters.Circle(100, -100, 200, 'green')
s2 = codesters.Circle(150, 150)
s3 = codesters.Circle(-100, 100, 200, 'yellow')
s3 = codesters.Circle(-150, 150)
s4 = codesters.Circle(-100, -100, 200, 'red')
s4 = codesters.Circle(150, -150)


# sprites
stage.set_background("space")
sprite1 = codesters.Sprite("pro controller", -150, 150)
sprite1.set_size(0.6)
sprite2 = codesters.Sprite("horsey", 150, -150)
sprite2.set_size(0.2)
sprite3 = codesters.Sprite("piano", -150, -150) 
sprite3.set_size(1)
sprite4 = codesters.Sprite("book", 150, 150)
sprite4.set_size(0.3)

message1 = codesters.Text("Elara Emery", 0,0, "white")
message2 = codesters.Text("I coded this :D", 0, 100, "black")