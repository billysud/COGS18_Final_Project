from main import *

# creating the entrance and exit floors since they are differently generated from middle floors
first_Level = create_top_level()
last_Level = create_bot_level()
lev = create_levels_list()

# putting in the levels list all of the levels and attempting to create a guaranteed pathway
levels[0] = first_Level
levels.append(lev)
levels[-1] = last_Level
validate_maze()

# creating a new turtle window
w = tr.Screen()
w.bgcolor("black")
w.setup(700, 700)

# drawing the maze
setup_maze(levels)

# input keys to commands
tr.listen()
tr.onkey(player.left, "Left")
tr.onkey(player.right, "Right")
tr.onkey(player.up, "Up")
tr.onkey(player.down, "Down")
w.tracer(0)


while True:
    w.update()
