import random

class Node:
    """Will be each node on the screen - robot - obj etc...

    Takes input of x and y positions, and colour values for the different node
    types.

    """

    def __init__(self, 
                 x1, 
                 y1,
                 side_len,
                 canvas,
                 price=5,
                 colour="#555",
                 outline="#666",
                 robot_colour = "#FF0000",
                 seeker_colour = "#00FF00",
                 sought_colour = "#96FF96",
                 item_colour = "#0000FF"
                 ):

        # initialise the coordinates for the vertice

        # These are the matrix positions for Node
        self.mx = x1
        self.my = y1

        # These are the pixel positions for Node
        x1 = x1 * side_len
        y1 = y1 * side_len

        self.x1 = x1
        self.y1 = y1

        x2 = self.x1 + side_len
        y2 = self.y1 + side_len

        self.x2 = x2
        self.y2 = y2

        self.side_len = side_len

        # get the center point of a node object
        self.midx = (x1 + x2) / 2
        self.midy = (y1 + y2) / 2

        self.center_tuple = (self.mx, self.my)
        
        self.colour = colour
        self.canvas = canvas

        # colours for robot and seeker nodes
        # Further colours might be chosen from
        # http://paletton.com/#uid=12C0u0kllllnh++mjw0knaGjp00
        self.colour = colour
        self.robot_colour = robot_colour
        self.seeker_colour = seeker_colour
        self.prev_seeker_colour = sought_colour
        self.item_colour = item_colour

        self.outline = outline
        # TODO the vertices just have a price of 5 atm
        self.value = price
        # not sure if this'll be useful atm
        self.am_robot = False
        self.am_seeker = False
        self.am_prev_seeker = False
        self.am_item = False
        self.am_prev_robot = False
        self.am_wall = False
        self.am_path = False
        self.last_colour = None
        self.item_name = None
        self.item_value = None

        # This is used for making walls, walls will have a weight of 1, where all else will have a weight of 0
        self.weight = 0

    def display(self):
        """display the vertice on screen"""
        if self.last_colour != self.colour:
            self.canvas.create_rectangle(self.x1,
                                    self.y1,
                                    self.x2,
                                    self.y2,
                                    fill= self.colour,
                                    outline=self.outline)
            self.last_colour = self.colour

        else:
            pass

    def set_robot(self):
        """This needs to set the colour of a node to be the robot colour
        Maybe this should also take input to change the last one from being a
        robot
        """
        self.am_robot = True
        self.colour = "Red"

    def set_seeker(self):
        """Change the node to represent a seeker node given the class variable setting
        of

        self.seeker_colour

        """
        self.am_seeker = True
        self.colour = "Green"

    def set_prev_seeker(self):
        """Change the node to represent a previous seeker node given the class variable setting
        of

        self.seeker_colour

        """
        self.am_prev_seeker = True
        self.colour = "Yellow"

    def set_item(self):
        """Change the node to represent a item node given the class variable setting
        of it will also asign the node a name and value

        self.seeker_colour

        """
        item_name_list = ["Flowers", "Fruit", "Snacks", "Stationary", "Milk", "Bread", "Coffee"]
        if self.am_item == False:
            self.am_item = True
            self.item_name = item_name_list[random.randint(0, len(item_name_list)-1)]
        self.colour = "Pink"

    def set_prev_robot(self):
        """Change the node to represent a previous robot node given the class variable setting
        of

        self.seeker_colour

        """
        self.am_prev_robot = True
        self.colour = "Orange"


    def set_path(self):
        """Change the node to represent a path node given the class variable setting
        of

        self.seeker_colour

        """
        self.am_path = True
        self.colour = "Purple"

    def set_wall(self):
        self.am_wall = True
        self.set_colour("Black")
        """
        Not sure whether I will use the weight at all but the idea is for the weight to be
        returned and if it has a weight of 1 then it wont be searched. Might save having to put
        the wall nodes in a list, will implament if there is time.
        """
        self.weight = 1

    def reset(self):
        """
        This will reset the node to an initial condition
        """
        self.colour = "#555"
        self.set_colour(self.colour)
        self.am_seeker = False
        self.am_robot = False
        self.display()

    def set_colour(self, c):
        """
        Change the colour of the node - this will be used to show that the node
        currently has the robot on it... maybe this should be another method as well
        """
        self.colour = c

    def collected_items(self):
        self.collected_items = []
        self.collected_items.append(self.item_name)

    def __str__(self):
        info = "Matrix <x,y> = <{},{}>\nPixel x1 = {}, Pixel y1 = {},\nPixel x2 = {}, Pixel y2 = {}\n".format(
            self.mx,
            self.my, 
            self.x1, 
            self.y1, 
            self.x2, 
            self.y2)
        return info

    def return_node(self):
        co_ordinates = [self.mx,self.my]
        return co_ordinates
