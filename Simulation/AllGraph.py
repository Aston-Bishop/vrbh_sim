from Tkinter import *
import math
import random
import time
# used to convert the 2D array into a 1D array
from itertools import chain

from Node import Node
# import Globals as gvs

class Graph:
    """Store the node objects and provide some higher level methods on them """

    def __init__(self,
                 NODE_NUM_H,
                 NODE_NUM_W,
                 NODE_SIZE,
                 canvas
            ):

        """
        Initialise a Matrix of Nodes

        Input of matrix width, matrix height, node size
        """
        # TODO: SHOULD THE CANVAS BE PASSED INTO THE GRAPH CLASS LIKE THIS?
        self.canvas = canvas

        # CREATE A 2D MATRIX TO STORE NODES
        node_list = []
        # Create each row
        for j in range(NODE_NUM_H):
            node_list.append([])
            # Create nodes in each row
            for i in range(NODE_NUM_W):
                node_list[-1].append(Node(j, i, NODE_SIZE, self.canvas))


        # total number of nodes in the matrix
        self.node_number = (NODE_NUM_W * NODE_NUM_H)
        # total width and height of canvas in pixels
        self.pixel_width = (NODE_NUM_W * NODE_SIZE)
        self.pixel_height = (NODE_NUM_H * NODE_SIZE)
        # the matrix containing all nodes.
        self.matrix = node_list

    def render(self):
        """This should render the graph on screen.

        Ideally this will only have to be done once.
        """
        for a_row in self.matrix:
            for a_node in a_row:
                a_node.display()

