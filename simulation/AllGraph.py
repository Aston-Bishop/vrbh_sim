from Tkinter import *
import math
import random
import time
# used to convert the 2D array into a 1D array
from itertools import chain
from pprint import pprint

from Node import Node

from HelperClass import Helpers
H = Helpers()

from GlobalsFile import Globs
G = Globs()

class Graph:
    """Store the node objects and provide some higher level methods on them

    Not set is used for testing
    """

    def __init__(self,
                 NODE_NUM_H,
                 NODE_NUM_W,
                 NODE_SIZE,
                 canvas = "Not set"
    ):

        """
        Initialise a Matrix of Nodes

        Input of matrix width, matrix height, node size
        """
        # TODO: SHOULD THE CANVAS BE PASSED INTO THE GRAPH CLASS LIKE THIS?
        # WORKS SO...?
        self.canvas = canvas

        # CREATE A 2D MATRIX TO STORE NODES
        node_list = []
        # Create each row
        for j in range(NODE_NUM_H):
            node_list.append([])
            # Create nodes in each row
            for i in range(NODE_NUM_W):
                node_list[-1].append(Node(i, j, NODE_SIZE, self.canvas))

        # total number of nodes in the matrix
        self.node_number = (NODE_NUM_W * NODE_NUM_H)

        # total width and height of canvas in pixels
        self.pixel_width = (NODE_NUM_W * NODE_SIZE)
        self.pixel_height = (NODE_NUM_H * NODE_SIZE)
        # the matrix containing all nodes.
        self.matrix = node_list

        self.number_of_rows = NODE_NUM_W

        # It's a square matrix so only need to consider this case. I'm using a
        # dictionary as they're very fast to look up, I'm purely using this for
        # looking up key values to see whether a coordinate is within the
        # allowed range
        self.valid_range = dict()
        for i in range(NODE_NUM_W):
            self.valid_range[i] = i

    def run(self):
        pass

    def render(self):
        """This should render the graph on screen.

        Ideally this will only have to be done once.

        """
        for index_r, a_row in enumerate(self.matrix):
            for index_b, a_node in enumerate(a_row):
                a_node.display()

    def set_seeker(self, p):
        """Set node at postiion p in the graph to be a seeker.

        # TODO: It's worth considering whether this is the most appropriate
        place to have this method. I think that it makes sense to talk to the
        graph for this? Leaving this for others to consider.

        """
        self.matrix[p[0]][p[1]].set_seeker()
        self.matrix[p[0]][p[1]].display()

    def set_sought(self, p):
        """Set node at postiion p in the graph to be sought (it's already been accessed
        / looked at)

        """
        self.matrix[p[0]][p[1]].set_sought()
        self.matrix[p[0]][p[1]].display()

    def reset_nodes(self, node_set):
        """reset all nodes of the input set

        input - node_set are the nodes that are to be reset by this method. This
        is a set() object

        """
        # print("Reset nodes : ")
        # print("Resetting the nodes : {}".format(pprint(node_set)))

        for node in node_set:
            node.reset()

    def create_random_item(self):
        """
        convert a random value on the grid to an item object.

        Input of the robot position as items shouldn't be placed there
        """
        # choose random row
        row = random.choice(self.matrix)
        node = random.choice(row)
        return node

    def generate_items(self,
                       number_of_items,
                       robot_node,
                       objects=None
                       ):
        """This function should generate items in the given position within the graph

        This shouldn't place any items :

            * Where the robot is positioned
            * where any objects are (not yet implemented)

        """
        placed_items = set()

        while len(placed_items) < number_of_items:
            item = self.create_random_item()
            placed_items.add(item)
            placed_items.discard(robot_node)

        return placed_items

    def create_generated_items(self, item_set):
        """
        set the previously generated items to be items on the graph
        """
        for item in item_set:
            item.set_item()

    def set_seek(self,seeker_set):
        """
        Iterate over the input set() and set any non item nodes to be seekers
        """
        for n in seeker_set:
            if not n.am_item:
                n.set_seeker()

    def set_sought(self, sought_set):
        """
        Iterate over input sought_set and set nodes to sought if they're not items
        """
        for n in sought_set:
            if not n.am_item:
                n.set_sought()

    def print_item_locations(self):
        """
        helper - this function is just for getting info whilst working on things

        I just want to get a print out of all the items that are currently in the graph
        """
        print("--------------------------------")
        print("print_item_locations function : ")
        for row in self.matrix:
            for node in row:
                if node.am_item == True:
                    print(node)
        print("--------------------------------")

    def draw_seekers(self, seeker_set):
        """take input of a set of nodes that are to be set to seekers and rendered on
        screen

        """


        for node in seeker_set:
            p = node.pos
            self.matrix[p[0]][p[1]].set_seeker()
            self.matrix[p[0]][p[1]].display()
            # node.set_seeker()
            # node.display()


    def place_item(self, node_item):
        """
        create an item at the given location given input of a node

        # TODO: Input of node / tuple?
        """
        print("place_item : ")
        print("Placing item at {}\n".format(node_item.pos))
        self.matrix[node_item.mx][node_item.my].am_item = True

    def place_robot(self, r, old_robot=None):
        """This will enable one to place the Robot on the Graph somewhere.

        Takes input of r which should be a position in the matrix to assign a
        robot node.

        eg r = (20,20) will create a robot node in the middle of a 20x20 matrix

        # TODO: this should take a tuple in or a node object? Whatever it takes
        # it should then call the function in the node class that creates the
        # robot node
        """
        # TODO: This will occaisionally place out of bounds so needs fixing!

        if old_robot:
            self.matrix[old_robot[1]][old_robot[0]].reset()
            self.matrix[r[1]][r[0]].set_robot()
        else:
            self.matrix[r[1]][r[0]].set_robot()

    def get_node_from_tuple(self, t):
        """
        With input of a tuple the graph should return the node object at that location
        """
        if self.invalid_graph_position(t):
            print("Error, tuple position is invalid, tuple : {}".format(t))
            print("Max range is 0 to {}".format(self.valid_range))
        else:
            # TODO: I had to change these to [1][0] for some reason - x,y are switched
            return self.matrix[t[1]][t[0]]


    def create_items():
        """
        This method should create a certain amount of items on screen
        """
        pass

    def get_nodes_not_searched_around_set_of_nodes(self, node_set):
        """
        Takes input of a set of nodes and for each node in that set returns
        nodes around it that haven't yet been searched
        """
        nodes_not_searched = set()

        for node in node_set:
            nodes = (self.get_nodes_not_searched_around_node(node))
            node.am_sought = True
            for n in nodes:
                nodes_not_searched.add(n)

        return nodes_not_searched

    def get_nodes_not_searched_around_node(self, node):
        """
        This will return all the edges of the input node

        Returns a set() of node objects that are around the edges of the input
        node and have't yet been searched

        # TODO: This could be streamlined - it's explicit for now though
        """

        # Set containing tuples representing matrix coordinates
        directions = set()
        # set that will be filled with node instances if the tuple coordinates are valid
        directions_nodes = set()
        # left
        directions.add(node.node_left())
        # right
        directions.add(node.node_right())
        # up
        directions.add(node.node_up())
        # down
        directions.add(node.node_down())

        # CHECK THAT THE COORDINATES ARE VALID
        remove_set = set()
        for direction in directions:
            if self.invalid_graph_position(direction):
                # add invalid nodes to set that will be used to subtract from the directions set after
                remove_set.add(direction)
                # directions.remove(direction)
            else:
                # TODO: Don't think this line is needed
                # n = (self.get_node_from_tuple(direction))
                directions_nodes.add(self.get_node_from_tuple(direction))

        directions = directions.difference_update(remove_set)

        # Set the input node to sought as it should have been dealt with by now
        node.am_sought = True

        # this will be the set of nodes that are valid positions and haven't
        # been searched yetjf
        return_set = set()

        # check whether the nodes have been searched yet
        for node in directions_nodes:
            if node.am_sought == False:
                return_set.add(node)

        return return_set

    def check_if_item_in_set(self, node_set):
        """
        Take input of a set and check whether there are any items in it.
        """
        items = set()
        for node in node_set:
            if node.am_item == True:
                items.add(node)
        return items

    def node_in_graph(self, node):
        """
        Check that the input node is in the graph
        """
        gmin = 0
        gmax = self.number_of_rows
        node_vals = (node.mx, node.my)
        # TODO: I'm currently trying to get this so that I can error check for
        # whether or not the nodes are within the range of the graphs matrix

    def invalid_graph_position(self, tup):
        """
        takes in a tuple representing a position, if the tuple isn't within the range of the jf matrix then return false

        """
        if tup[0] in self.valid_range and tup[1] in self.valid_range:
            return False
        else:
            return True

    def get_not_searched(self, nodes_set):
        """
        Given a set of Nodes this will return all those within that haven't
        been searched yet
        """
        s = set()
        for n in nodes_set:
            if n.am_sought == False:
                # This means the node hasn't been searched yet and needs to be
                s.add(n)
            else:
                # It's already been searched - no need to search it again
                pass
        return s

    def check_if_item_in_seekers(self, seekers):
        """
        Takes an input of seeker nodes and checks whether any of them is an
        item node
        """
        items = set()
        for s in seekers:
            if s.am_item == True:
                items.add(s)
        if items:
            return items
        else:
            return False

    def receive_tuple_position(self, n):
        """The graph should be able to receive a tuple position and find nearby
        nodes based on that.

        At the moment the tuple input is a node position on a 40x40 matrix,
        rather than its pixel value.

        This needs to take the input of a node rather than a pixel value.

        """
        n1 = n[0]
        n2 = n[1]

        # this will get the <x, y> for the Pixel coordinates rather than the
        # Matrix coordinate? As in - the matrix coordinates would be the row
        # column where the matrix was ~ 40x40 or whatever, returning a value of
        # 500 + means that they're
        # pixles rather than nodes.
        # The nodes have the <x, y> to render to canvas though, so this
        # probably makes sense.
        # this is a node here

        node_req = self.matrix[n1 - 1][n2]
        return node_req

    def draw_line():
        """This is going to take a path and draw a line along the given path. The path
        will have to be a list of node locations, or just nodes and read the
        locations from them directly.

        """
        pass

    def __str__(self):
        """
        Method to call when a graph instance is printed as a string.

        Currently just returns a string made up of all the rows

        """
        return_string = "\nGraph Info : \n"
        return_string += "Matrix size : \n{} X {}".format(self.number_of_rows,
                                                         self.number_of_rows)
        return return_string

    def get_left_node(self):
        """
        Get the node to the left of the given node
        """
        pass

    def get_right_node(self):
        """
        Get node to the right of the given node
        """
        pass

    def get_above_node(self):
        """
        Get the node above the given node
        """
        pass

    def get_below_node(self):
        """
        Get the node beneath the given node
        """
        pass


    def get_matrix_n(self):
        """
        At the moment when one pulls a node from the matrix the values are it's
        """
        pass

###############################################################################

    def check_if_in_range_node(self, node):
        """
        Check that a node value is in range of the graph
        """
        if node.mx > self.number_of_rows or node.mx < 0:
            print("Node is out of range :")
            print("node : {}".format(node.pos))
            H.wait(6, "error...")
        if node.my > self.number_of_rows or node.my < 0:
            print("Node y is out of range :")
            print("node : ".format(node.pos))
            H.wait(6, "error...")

    def get_all_neighbours(self, n):
        """This is a naive method for getting all neighbours of a given node.

        Given the input of a node "n" this method should return the address of the
        4 nodes that are around it

        """
        return n
