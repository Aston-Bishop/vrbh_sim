from Tkinter import *
import math
import random
import time
from itertools import chain

class Globs:
    """This is a helper class for storing global variables in that shouldn't have
    to be accessed anywhere else in the file.

    values that are used in multiple classes / places should be moved into here
    instead

    """

    def __init__(self,
                 matrix_size=50,
                 node_size=15,
                 item_type = None,
                 screen_refresh=70,
                 canvas_background_colour="#0F1E15",
                 item_colour="#9EFD23",
                 robot_colour="#FC227E",
                 obstacle_colour="#FF4923",
                 robot_start_position = (4,5),
                 ):

        # Size of the square matrix, this should be a value such as 30 which
        # will then create a 30x30 matrix (will always be square)
        self.matrix_size = matrix_size

        # size of the nodes to be created in pixels
        self.node_size = node_size

        # these are the default colours to use for the robot
        # i used this for the default colours
        # http://paletton.com/#uid=c5i2u082X0kgddEhy00fz5ak5pXrDYz
        self.canvas_background_colour = canvas_background_colour
        self.item_colour              = item_colour
        self.robot_colour             = robot_colour
        self.obstacle_colour          = obstacle_colour

        # this just works like frame rate
        self.screen_refresh = screen_refresh

        # This is the start position for the robot object on the screen. This
        # could be set by an external method such as the interface at a later
        # date.
        self.robot_start_position = robot_start_position

        # Set that will be used to store the seeker objects whilst searching
        # for items
        self.seeker_set = set()
        # Set to store items that have been searched already
        self.sought_set = set()
        self.all_sought_set = set()

        # TODO: might make sense to set the type of item to be searched for if
        # there are going to be a few different kinds as considered. Such as A,
        # B, C were 'classes' of items.

        # There should be multiple types of item, such as A, B, C where A would
        # contain a random selection of elements such as fruit for example,
        # where it might contain for example:

        # ################################
        # TYPE    - VALUE - AMOUNT - TOTAL
        # ################################
        # apples  - 3     - 4      - 12
        # pears   - 2     - 3      - 6
        # oranges - 1     - 5      - 5
        # ################################
        # total   -       -        - 23
        # ################################

        # These would all be represented by one item on screen - but this item
        # would be a sort of basket that contained these multiple things within
        # it.

        # TODO: does it make sense to have multiple items on screen?

        self.item_type = item_type

        # this is a set of all the collected items that the robot has picked
        # up.
        self.collected_items = set()


        ###############################################
        # TODO: IT WOULD BE NICE TO HAVE A GLOBAL CANVAS AS WELL BUT CURRENTLY
        # THIS ISN'T WORKING. I'M NOT TOO SURE WHY AT THE MO THOUGH
        ###############################################

        # Canvas dimensions
        self.canvas_width = self.matrix_size * self.node_size
        self.canvas_height = self.matrix_size * self.node_size

        """
        # set up the canvas to be used across all files
        root = Tk()
        # It's always going to be a square matrix
        self.canvas_width = self.matrix_size * self.node_size
        self.canvas_height = self.matrix_size * self.node_size
        # create the actual canvas here
        self.canvas = Canvas(root,
                             width = self.matrix_size,
                             height = self.matrix_size,
                             bg=self.canvas_background_colour)

        # self.canvas.pack()

        """

    def set_robot_position(self):
        """
        # TODO: It might make sense to have the robot position set within
        # the globals file rather than in the graph section? Then the graph
        # can just read from there or something along those lines
        """
        pass

    def random_robot_start_position(self):
        """
        This will just randomise the starting position of the robot node
        """
        startx = random.randint(0,self.matrix_size)
        starty = random.randint(0,self.matrix_size)
        self.robot_start_position = (startx, starty)

    def reset_sought_sets(self):
        """
        reset the sets that contain info about the nodes that have been sought
        and that are currently seeker nodes
        """
        self.sought_set = set()
        self.all_sought_set = set()

