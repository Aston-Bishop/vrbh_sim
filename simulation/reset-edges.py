
from Tkinter import *
import math
import random
import time
from itertools import chain

from Node import Node
from AllGraph import Graph


"""This is just for testing the function to get all nodes that need to be
reset """

def create_matrix(s):
    """Create a square matrix to the given size (s) for testing.
    The function starts with an empty list, for every additional row needed it
    creates a new list and appends it to the original one.
    The matrix.append([]) puts a new list (row) INTO the matrix, and the
    matrix[-1] ensures that we're adding to the empty list just input to the
    matrix.
    matrix []
    Then matrix [[]]
    Etc.
    For a size of three the matrix created would be
    [
    [[0, 0], [1, 0], [2, 0]],
    [[0, 1], [1, 1], [2, 1]],
    [[0, 2], [1, 2], [2, 2]]
    ]
    """
    matrix = []
    for i in range(s):
        matrix.append([])
        for j in range(s):
            matrix[-1].append((j, i))
    return matrix

###############################################################################


def get_nodes_to_reset(t, b, m):
    """

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

print('...')

m = create_matrix(15)



mid = len(m[0]) / 2
bm = len(m) - 1

# This is the top and bottom positions for the nodes here.

# TODO: This isn't going to be general though as it's only for when the Robot
# is in the center
top = (mid, 0)
bot = (mid, bm)


v = get_nodes_to_reset(top, bot, m)

print(len(v))

for i in v:
    print(i)





# a = [
#     (2, 3), (3, 5), (5, 6)
# ]

# c = set()
# c.update(a)
# print(c)
