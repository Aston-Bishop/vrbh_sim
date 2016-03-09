from Tkinter import *
import math
import random
import time
from itertools import chain

from Node import Node
from AllGraph import Graph

print()

###############################################################################

# Note! You might notice that the layout of this code is a bit weird and there
# are doc strings EVERYWHERE. The reason is that I'm intending to convert it to
# markdown afterwards and thought that this method might make things a bit
# easier for that (it's not something that I usually do).

###############################################################################

"""
Some helper functions to begin with
"""

def print_matrix(m):
    """
    Just print the input matrix out to the screen
    """
    print("Matrix = \n")
    for row in m:
        print(row)

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
            matrix[-1].append([j,i])
    return matrix

###############################################################################

"""This file is for testing the logic of the simple algoritm.

I want to see if using mutliple lists for the directions of the edges makes
sense, and will do this just using 2D arrays within this file rather than
tkinter, and transfer the logic over after.

When the current graph is set up with 5x5 matrix the following is output -

```
[ <0,0>, <1,0>, <2,0>, <3,0>, <4,0>,  ]
[ <0,1>, <1,1>, <2,1>, <3,1>, <4,1>,  ]
[ <0,2>, <1,2>, <2,2>, <3,2>, <4,2>,  ]
[ <0,3>, <1,3>, <2,3>, <3,3>, <4,3>,  ]
[ <0,4>, <1,4>, <2,4>, <3,4>, <4,4>,  ]
```
"""

"""
Variables
"""

size = 9
matrix = []

###############################################################################

"""Now I want to be able to access the nodes using the simple algorithm

For example, on the first iteration with a robot position of [4,4] the edges
that are required are -

```
                        [4, 3]

                [3, 4]  <Robot> [5, 4]

                        [4, 5]
```

[4,3] the top
[4,5] the bottom


the other two are the edges between, though for this stage they are the *only*
ones between the top and bottom (this will increase as the code increases).

                                 [4, 2]
                         [3, 3]          [5, 3]
                 [2, 4],         [4, 4]          [6, 4]
                         [3, 5]          [5, 5]
                                 [4, 6]

Here [4, 4] is still the robot, and note that the nodes [5,4] and the like
(that were searched on the last iteration) aren't included in this search.

The purpose of seperating the logic between Top and Bottom should now be easier
to demonstrate, as the Top and Bottom nodes can both search 3 edges on the next
iteration while the rest only search one edge (eithe to the right or the left
depending on which side they're on).

Here are the three nodes that would be searched on the next iteration by Top
node (4,2)

```
                                 [4, 1],
                         [3, 2], [4, 2], [5, 2]
```

And here are the 3 that would be searched by the bottom node [4, 6]

```
                         [3, 6], [4, 6], [5, 6]
                                 [4, 7]
```

From here one can see that all other nodes would (within this algorithm) only
have to search the nodes immediately to their left/right.

Here's what would be searched on the next iteration for all edges -


```
                                 [4, 1],
                         [3, 2]          [5, 2]
                 [2, 3]                          [6, 3]
         [1, 4]                  [4, 4],                 [7, 4]
                 [2, 5]                          [6, 5]
                         [3, 6]          [5, 6]
                                 [4, 7]
```

Hopefully the above illustrates how the algoritm is working

"""

matrix = create_matrix(size)
print_matrix(matrix)


"""
This just shows where the robot is currently (sanity check)
"""
Robot = (4,4)
print("\nRobot position = \n")
print(matrix[Robot[0]][Robot[1]])


"""Now I want to get the *first* iteration of edges.

For the first iteration I'm going to have to *set* the top and bottom edges,
though for the following iterations these will be the previous ones + 1

Using R for Robot because I'm lazy

"""

R = Robot

"""
So this is going to be the first Top and Bottom edges

[1]
"""

TopEdge = (R[0], (R[1] - 1))
BottomEdge = (R[0], (R[1] + 1))

"""
Test that these work -
"""

print("\nTop and Bottom edges : \n")
print(TopEdge, BottomEdge)

"""Output :

```text
>>> Top and Bottom edges :
>>> ((4, 3), (4, 5))
```

Cool, as wanted from the [ascii] illustrations earlier.

We now need to get the 'inbetween' bits, even though there are only two for
this iteration their position should be based on the location of Top and Bottom
nodes rather than the robot position, so that they will fill up as the Top and
Bottom nodes get further from the Robot position.

For this I'm going to work out the difference between the top and the bottom
nodes, then divide it by two
"""

difference_top_bottom= abs(TopEdge[1] - BottomEdge[1]) / 2

"""Now I'm going to create the nodes for the edges.

The problem that might arise is that there are duplicate edges (though
hopefully there will be far fewer duplicates than before, and there will only
be one duplicate as the values grow)

I'm using a set() structure so that there are no duplicates stored.
"""

edges = set()
inc = 1

for n in range(difference_top_bottom):
    edges.add((TopEdge[0]    - inc, TopEdge[1]    + inc))
    edges.add((BottomEdge[0] - inc, BottomEdge[1] - inc))
    edges.add((TopEdge[0]    + inc, TopEdge[1]    + inc ))
    edges.add((TopEdge[0]    + inc, TopEdge[1]    - inc ))


"""This now has all of the iterations needed for this run, in conjunction with
TopEdge and BottomEdge there are four edges to test
"""

print(edges)


"""The same logic can be used for other iterations as it should scale up,
create some functions to make things a bit easier to read -

"""

def calc_tb_distance(t, b):
    """Input of tuples t[op] and b[ottom] nodes, returns half the distance between
    the two

    """
    difference_top_bottom = abs(t[1] - b[1]) / 2
    return difference_top_bottom

def get_edges(t, b, d):
    """Input of t[op], b[ottom] tuples and the d[ifference] from them to the Robot

    This will return a set() of the values that should be tested.

    I'm leaving print statements in here so that you can run if you choose to
    in order to see how it's functioning

    """
    edges = set()

    print("Iteration number [distance value] = {}".format(d))
    print("\n\n")
    for n in range(d):
        n = n  + 1

        topLeft = (t[0] - n, t[1] + n)
        print("Top Left {} = {}".format(n,topLeft))
        edges.add((topLeft))

        bottomLeft = (b[0] - n, b[1] - n)
        print("Bottom Left {} = {}".format(n, bottomLeft))
        edges.add(bottomLeft)

        topRight = (t[0] + n, t[1] + n)
        print("Top Right {} = {}".format(n, topRight))
        edges.add((topRight))

        bottomRight = (b[0] + n, b[1] - n)
        print("Bottom Right {} = {}".format(n, bottomRight))
        edges.add((bottomRight))

        print('\n')
    return edges


"""Now test these using increased iteration values, trying where the TopEdge is
(4,2) and the BottomEdge is (4, 6), the values expected are (from the above
diagram)

```
                         [3, 3]          [5, 3]
                 [2, 4],                         [6, 4]
                         [3, 5]          [5, 5]
```

"""

print("-" * 79)

edges = set()
TopEdge = (TopEdge[0], TopEdge[1] - 1)
BottomEdge = (BottomEdge[0], BottomEdge[1] + 1)
dist = calc_tb_distance(TopEdge, BottomEdge)
edges = get_edges(TopEdge, BottomEdge, dist)

print(edges)


"""Here it can be seen that the above logic is working given Tuples, a Matrix
and the above functions.

Try another iteration to ensure that it's functioning alright.

From teh above illustration this is the third (or 2nd, depending on if you want
to count zero for everything in your life or not) iteration -

```
                                 [4, 1],
                         [3, 2]          [5, 2]
                 [2, 3]                          [6, 3]
         [1, 4]                  [4, 4],                 [7, 4]
                 [2, 5]                          [6, 5]
                         [3, 6]          [5, 6]
                                 [4, 7]
```
"""
print("-" * 79)

edges = set()

TopEdge = (TopEdge[0], TopEdge[1] - 1)
BottomEdge = (BottomEdge[0], BottomEdge[1] + 1)
dist = calc_tb_distance(TopEdge, BottomEdge)
edges = get_edges(TopEdge, BottomEdge, dist)

print(edges)

"""One can see that all the values are in there, but might as well *double*
check that it's working alright. For the third iteration we're expecting a set
/ list / whatever of the following values

Not a pretty test I'll admit but -

"""

test_edges = [(4, 1), (3, 2), (5, 2), (2, 3), (6, 3), (1, 4), (7, 4), (2, 5),
              (6, 5), (3, 6), (5, 6), (4, 7) ]

OK = True

for test in test_edges:
    if test not in edges and test != TopEdge and test != BottomEdge:
        print("{} isn't in and it should be!".format(test))
        OK = False
if OK:
    print("All good")


"""At this point I'm satisfied the logic works, and *hopefully* this was
helpful in communicating it to others.

I might just leave this as it is, it's pretty readable.

"""

"""Some notes on the above -

[1] Looking back over this it would make more sense to assign the top and
bottom to the robot values for the first run and just go from there. Whether it
would be more expensive to do it this way or not idk, seems like it would be a
bit cleaner at least.


"""
