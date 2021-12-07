# credit https://www.youtube.com/watch?v=-0q_miviUDs
import turtle as tr
import random as rd

# Global variables
my_list = [" ", "x"]
levels = [""]


# Creating a class for a pen to draw
class Pen(tr.Turtle):
    def __init__(self):
        tr.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)


# Creating a class for the player
class Player(tr.Turtle):
    def __init__(self):
        super(Player, self).__init__()
        self.shape("square")
        self.color("green")
        self.penup()
        self.speed(0)

    def up(self):
        # calculating the theoretical position moving up
        move_to_x = player.xcor()
        move_to_y = player.ycor() + 24
        player.goto(move_to_x, move_to_y)

    def down(self):
        # calculating the theoretical position moving up
        move_to_x = player.xcor()
        move_to_y = player.ycor() - 24
        player.goto(move_to_x, move_to_y)

    def left(self):
        # calculating the theoretical position moving up
        move_to_x = player.xcor() - 24
        move_to_y = player.ycor()
        player.goto(move_to_x, move_to_y)

    def right(self):
        # calculating the theoretical position moving up
        move_to_x = player.xcor() + 24
        move_to_y = player.ycor()
        player.goto(move_to_x, move_to_y)


def create_level():
    """
    Function to create a randomized level
    Parameters
    ----------

    Returns
    -------
    list_to_floor(temp_level): str
        this is a string made of "x"'s and " "'s where "x" is a wall and " " is a path
    """
    temp_level = ["x"]

    for item in range(0, 25):
        randChoice = rd.choice(my_list)
        temp_level.append(randChoice)

    temp_level[25] = "x"

    return list_to_floor(temp_level)


def create_top_level():
    """
    Function to create a level that has all walls except for an entrance and an exit

    :return:
    out_string:str
        a string to represent the entrance/exit level where it is all "x"'s and one " "
    """
    out_string = "                          "
    temp_list = floor_to_list(out_string)
    rand = rd.choice(range(0, 5))

    for item in range(len(temp_list)):
        temp_list[item] = "x"

    temp_list[rand] = "P"
    out_string = ""

    for item in temp_list:
        out_string = out_string + str(item)
    return out_string


def create_bot_level():
    """
    Function to create a level that has all walls except for an entrance and an exit

    :return:
    out_string:str
        a string to represent the entrance/exit level where it is all "x"'s and one " "
    """
    out_string = "                          "
    temp_list = floor_to_list(out_string)
    rand = rd.choice(range(0, 4))

    for item in range(len(temp_list)):
        temp_list[item] = "x"

    temp_list[rand] = " "
    out_string = ""

    for item in temp_list:
        out_string = out_string + str(item)
    return out_string


def create_levels_list():
    """
    Function to generate individual levels and append into our global variable levels(list)

    :return:
    levels: list
        a list that contains the strings that represents the maze
    """
    for counter in range(0, 23):
        new_level = create_level()
        levels.append(new_level)
    return levels


# creating a pen and player to draw the maze and player
pen = Pen()
player = Player()


def setup_maze(level):
    """
    Function to draw the maze
    :param
    level: list
        a list with strings to be drawn

    :return:

    """
    # Nested loops to go across the list formatted like in a matrix
    for y in range(len(level)):
        for x in range(len(level[y])):

            character = level[y][x]
            screen_x = -288 + (x * 24)
            screen_y = 288 - (y * 24)

            if character == "x":
                pen.goto(screen_x, screen_y)
                pen.stamp()

            if character == "P":
                player.goto(screen_x, screen_y)


def validate_floor(invalid_floor, prev_floor, row):
    """
    Function to make sure the maze is valid and has a path from entrance to exit.
    :param invalid_floor: str, floor to fix
    :param prev_floor: str, floor before the bad floor
    :param row: int, the row in the list of the bad floor
    :return: fixed_floor: str the fixed floor
    """

    prevExit = find_exit(prev_floor)
    fixed_floor = floor_to_list(invalid_floor)
    fixed_floor[prevExit] = " "
    fixed_floor_string = list_to_floor(fixed_floor)
    levels[row] = fixed_floor_string

    return fixed_floor


def validate_maze():
    """
    Function to make sure there is a pathway from the entrance to the exit
    :return:
    """
    for item in range(len(levels)):
        if item != 0:
            fixed_floor = validate_floor(levels[item], levels[item - 1], item)
            levels[item] = fixed_floor


def floor_to_list(in_floor):
    """
    Function to turn a floor into a list so we can remove and append
    :param in_floor: str, the desired floor to be turned into a list
    :return: out: list the string as a list
    """
    out = []
    for item in in_floor:
        out.append(item)
    return out


def list_to_floor(in_list):
    """
    Function to turn a list into a floor so we can have representation of all levels as strings
    :param in_list: list, the list desired to be turned into a string
    :return: out: str, the string representation of the list
    """
    out = ""
    for item in in_list:
        out = out + str(item)
    return out


def find_exit(in_str):
    """
    Function to find the pathway given a floor
    :param in_str: str, the level that is desired to find a pathway
    :return: counter: int, the position of the first non-wall
    """
    counter = 0

    for item in in_str:

        if item != "x":
            return counter
        else:
            counter += 1
