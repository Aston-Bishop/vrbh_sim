from Tkinter import *
import math
import random
import time
from itertools import chain

from Node import Node
from AllGraph import Graph

from pprint import pprint

from HelperClass import Helpers
H = Helpers()

from GlobalsFile import Globs
G = Globs()

print("search-around.py...")

###############################################################################

# this file is just for testing the search around algorithm. Instead of
# searching in the current manner the program should instead search every node
# around it and create lists with their info.

# ALGORITHM

# 2. Start from set of nodes edges
    # 2.2 test if item_node in set of edges
        # 2.2.1 if item_node in set then ....
    # 2.3 get all edges from current node set
        # 2.3.1 start from 2 again

###############################################################################

# Searching now seems to be working better within this example

###############################################################################

print ""

###############################################################################

# Set up the environment with canvas to use

# CREATE MAIN TKINTER ROOT
root = Tk()

canvas = Canvas(root,
                width = G.canvas_width,
                height = G.canvas_height,
                bg=G.canvas_background_colour)
canvas.pack()

# create a graph instance
simulation_graph = Graph(G.matrix_size,
                         G.matrix_size,
                         G.node_size,
                         canvas)

G.random_robot_start_position()

simulation_graph.render()
simulation_graph.place_robot(G.robot_start_position)

###############################################################################

# robot and item_node positions
start_pos = G.robot_start_position

# TODO: This is how many items want to be found by the program. if this is set
# to 1 then only one item is found, if it's set to 4 then 4 will be found etc.
items_to_find = 10

# initial set with the one element which is the robot
# seeker_set = set()
# set that will contain the items that have been found (if any) on that
# particular search
item_found = set()

robot_node = simulation_graph.get_node_from_tuple(G.robot_start_position)
placed_items = simulation_graph.generate_items(4, G.robot_start_position)
simulation_graph.create_generated_items(placed_items)

# Add the robot node to the set of initial values
G.seeker_set.add(robot_node)

# i want this set to keep hold of the last searched and render a different
# colour in the main_animate method
sought_set = set()

###############################################################################

def main_animate():
    # get edges around the start set
    G.seeker_set = simulation_graph.\
                   get_nodes_not_searched_around_set_of_nodes(G.seeker_set)

    # set and display seeker nodes
    simulation_graph.set_seek(G.seeker_set)

    # set and display sought nodes
    simulation_graph.set_sought(G.sought_set)

    G.sought_set = G.seeker_set

    G.all_sought_set.update(G.seeker_set)

    # test if there's an item in the seeker set
    for n in G.seeker_set:
        if n.am_item:
            # don't want the node to be an item any more
            n.reset()
            G.collected_items.add(n)

            # to be passed into the next search
            single_node_set = {n}

            # seeker and sought sets aren't needed anymore
            simulation_graph.reset_nodes(G.seeker_set)
            simulation_graph.reset_nodes(G.all_sought_set)
            # reset the sought sets from
            G.reset_sought_sets()
            simulation_graph.place_robot(n.pos, G.robot_start_position)

            # get the next nodes to search from the current position
            G.seeker_set = single_node_set
            G.robot_start_position = n.pos

    root.after(G.screen_refresh, main_animate)

# TODO: should be able to test if all the nodes have been foudn or not so far -
# this will be when the graph is filled up (no where else to search). Though if
# there are objects on the graph then this logic probably won't work so well.

###############################################################################

root.after(G.screen_refresh, main_animate)
root.mainloop()
root.destroy()
