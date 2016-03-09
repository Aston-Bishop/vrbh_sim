from Tkinter import *
import math
import random
import time
from itertools import chain

from Node import Node
from AllGraph import Graph
from GlobalsFile import Globs

G = Globs()

###############################################################################


# INIT VARIABLES
NODE_NUM_W = 50
NODE_NUM_H = 50
NODE_SIDE_LEN = 15

MATRIX_TOTAL_NODE_AMOUNT = NODE_NUM_H * NODE_NUM_W # 3x3 = 9
MATRIX_WIDTH = NODE_NUM_W * NODE_SIDE_LEN          # eg 3x3 matrix with NODE_SIZE of 2 = 6 wide
MATRIX_HEIGHT = NODE_NUM_H * NODE_SIDE_LEN         # eg 3x3 with NODE_SIZE 2 = 6 high
NODE_SIZE = NODE_SIDE_LEN

CANVAS_BACKGROUND_COLOUR = 'white'
# Think frames per seconds, just a milliseconds value of how often to refresh
# the page
SCREEN_REFRESH = 100

# CREATE MAIN TKINTER ROOT
root = Tk()
# Create the canvas with given sizes
canvas = Canvas(root,
                width = MATRIX_WIDTH,
                height = MATRIX_HEIGHT,
                bg=CANVAS_BACKGROUND_COLOUR)
canvas.pack()

###############################################################################

# TODO: If the robot is set to the edge of the screen the search values will
# overlap (like snake or something bleeding over). Also when this happens teh
# reset method doesn't work.

# Position for the robot to start at while testing
robot_tuple = (35,20)

test_graph = Graph(NODE_NUM_H, NODE_NUM_W, NODE_SIZE, canvas)

test_graph.render()
test_graph.place_robot(robot_tuple)

###############################################################################

def reset_values(t, b, r):
    """Takes input of top and bottom tuples for the search graph and resets them
    to the robot position.

    """
    t = (r[0], r[1])
    b = (r[0], r[1])
    return t, b

def calc_tb_distance(t, b):
    """Input of tuples t[op] and b[ottom] nodes, returns half the distance between
    the two

    """
    difference_top_bottom = abs(t[1] - b[1]) / 2
    return difference_top_bottom

def get_reset_edges(t, b):
    """Resetting is a bit different to the seeker edges - as ALL nodes in the
    'diamond' need to be reset here, wheras for the seeker (get_edges()) it's
    just the external nodes which should be set.
    """
    pass

def get_edges(t, b, d, m=test_graph.matrix):
    """Input of t[op], b[ottom] tuples and the d[ifference] from them to the Robot

    This will return a set() of the values that should be tested.

    # TODO: This is for the seeker nodes right?
    """

    # TODO: These values are so that if the value of the next node is greater
    # than the edge of the screen they can be set to be the edge of the screen instead.

    # TODO: This might be more efficient if at the end the values are hard
    # coded somewhere else rather than setting jf things up in here
    matrix_x_range = len(m[0]) - 1
    matrix_y_range = len(m) - 1

    min_x = 0
    max_x = NODE_NUM_W
    min_y = 0
    max_y = NODE_NUM_H

    edges = set()

    for n in range(d):
        # TODO: How does it get the side values, i get how it gets the ones above and below
        # but not the sides

        n = n  + 1

        # Create nodes to be added to the set()
        topLeft = (t[0] - n, t[1] + n)
        topRight = (t[0] + n, t[1] + n)
        bottomLeft = (b[0] - n, b[1] - n)
        bottomRight = (b[0] + n, b[1] - n)

        # Check that the nodes aren't outside of the matrix index.

        # TODO: This isn't currently working though i don't think...

        # Add nodes to the edges set

        # Top left
        if topLeft[0] >= 0:
            if topLeft[1] >= 0:
                edges.add(topLeft)

        # Top right
        if bottomLeft[0] >= 0:
            if bottomLeft[1] < NODE_NUM_H:
                edges.add(bottomLeft)

        # bottom left
        if topRight[0] < NODE_NUM_W:
            if topRight[1] >= 0:
                edges.add(topRight)

        # bottom right
        if bottomRight[0] < NODE_NUM_W:
            if bottomRight[1] < NODE_NUM_H:
                edges.add(bottomRight)

    return edges

def get_nodes_to_reset(t, b, m):
    """# TODO: Though this works at the moment - it might make sense to just do a
    square rather than working out the diamon as is done here. Reason being that if
    the search is close to the edge of the screen the shape won't be a diamond in
    the same way as this is expecting. However just resetting the rectangle around
    it would work - permitting that the nodes being reset weren't either obstacles
    or other items (this would be something to check)

    ###############################################################################

    INPUT
    -----

    t[op] > tuple > the top node of search

    b[ottom] > tuple > bottom node of search

    m[atrix] > 2D list > 2D list of node objects, this is the graph.

    RETURN
    ------

    Returns a set() which has all of the node object index positions from the
    search top to bottom

    EXAMPLE
    -------

    m[atrix] to use for values, which will be structured as (for a 3x3 matrix
    size where n represents a node object)

    m = [
        [n, n, n],
        [n, n, n],
        [n, n, n]]

    Here Top and Bottom nodes represent the node on the top or the bottom of
    the search as it's viewed from the screen.

    EXAMPLE SEARCH TOP / BOTTOM

    here [2,0] would be the top and [2,4] would be the bottom -

                        (2, 0)
                (1, 1), (2, 1), (3, 1)
        (0, 2), (1, 2), (2, 2), (3, 2), (4, 2)
                (1, 3), (2, 3), (3, 3)
                        (2, 4)

    """

    # TODO: Changing 'alt' value alters the amount of 'seeker buffers' that are
    # on the edge of the search graph
    alt = 1
    t = (t[0] , t[1] + alt)
    b = (b[0], b[1] - alt)

    # need half the distance between the nodes + 1 because it needs to iterate
    # from the top node to the center position and from the bottom node to the
    # center position

    d2 = (abs(t[1] - b[1]) / 2) + 1

    s = set()

    # Iterate from the top to the center and from the bottom to the center.
    for i in range(d2):

        # i rows away from either the top or the bottom node
        top_row    = t[1] + i
        bottom_row = b[1] - i

        # values that set the most left and most right nodes for each
        # iteration. For example on the Example Matrix in the doc string for
        # the second iteration (1,1) would be top left and (3,1) would be top
        # right.
        topLeft     = t[0] - i
        topRight    = t[0] + i
        bottomLeft  = b[0] - i
        bottomRight = b[0] + i

        # Once the top left and right nodes have been found everything
        # inbetween them can be got through list slicing
        top_list    = (m[top_row][topLeft:topRight+1])
        bottom_list = (m[bottom_row][bottomLeft:bottomRight+1])

        # s.update() is a method to add list values to sets. bit more info here
        # - https://docs.python.org/2/library/sets.html#set-objects
        s.update(top_list)
        s.update(bottom_list)

    return s

# TODO: Nodes should search everything around them


# search everything around node
    # anything that hasn't been searched add to 'to search'
# Search everything in 'to search' set / array
    # anything that hasn't been searched add to new 'to search' list

###############################################################################

TopEdge    = (robot_tuple[0], robot_tuple[1])
BottomEdge = (robot_tuple[0], robot_tuple[1])
edges      = set()

def mmain_animate():
    pass

def main_animate():

    # TODO: globals urgh - shouldn't need these
    global TopEdge
    global BottomEdge
    global edges

    # this should be all of the edges from the previous run, which
    # (after being searched) should now be set to sought
    try:
        for e in edges:
            test_graph.set_sought(e)
    except UnboundLocalError as firstRun:
        # TODO: This will kick up an error on the first pass so just catch it
        # for now
        pass

    edges = set()

    TopEdge    = (TopEdge[0], TopEdge[1] - 1)
    BottomEdge = (BottomEdge[0], BottomEdge[1] + 1)
    dist = calc_tb_distance(TopEdge, BottomEdge)

    edges = get_edges(TopEdge, BottomEdge, dist)

    if TopEdge[1] >= 0:
        edges.add(TopEdge)
    if BottomEdge[1] <=  NODE_NUM_W- 1:
        edges.add(BottomEdge)

    if dist >= 1000:
        # clear the search pattern
        reset_nodes = get_nodes_to_reset(TopEdge, BottomEdge, test_graph.matrix)
        test_graph.reset_nodes(reset_nodes)
        TopEdge, BottomEdge =  reset_values(TopEdge, BottomEdge, robot_tuple)
        # reset the edges to an empty set
        edges = set()
    else:
        # create the next line of seekers
        for e in edges:
            test_graph.set_seeker(e)

    root.after(SCREEN_REFRESH, main_animate)

###############################################################################

root.after(SCREEN_REFRESH, main_animate)
root.mainloop()
root.destroy()
