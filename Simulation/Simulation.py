from Tkinter import *
import math
import random
import time
from itertools import chain

from Node import Node
from AllGraph import Graph
import Globals

###############################################################################

start_time = None

# CREATE MAIN TKINTER ROOT
root = Tk()

# INIT VARIABLES
NODE_NUM_W = Globals.matrix_size
NODE_NUM_H = Globals.matrix_size
NODE_SIDE_LEN = 15
MATRIX_TOTAL_NODE_AMOUNT = NODE_NUM_H * NODE_NUM_W # 3x3 = 9
MATRIX_WIDTH = NODE_NUM_W * NODE_SIDE_LEN          # eg 3x3 matrix with NODE_SIZE of 2 = 6 wide
MATRIX_HEIGHT = NODE_NUM_H * NODE_SIDE_LEN         # eg 3x3 with NODE_SIZE 2 = 6 high
NODE_SIZE = NODE_SIDE_LEN

CANVAS_BACKGROUND_COLOUR = 'white'
# Think frames per seconds, just a milliseconds value of how often to refresh
# the page
SCREEN_REFRESH = 250

# Create the canvas with given sizes
canvas = Canvas(root,
                width = MATRIX_WIDTH,
                height = MATRIX_HEIGHT,
                bg=CANVAS_BACKGROUND_COLOUR)
canvas.pack()

###############################################################################

test_graph = Graph(NODE_NUM_H, NODE_NUM_W, NODE_SIZE, canvas)

test_graph.render()

# TODO: Pass in a tuple instead of a fixed value. It makes no sense for the value to 
# just be one term for a 2D list, instead the Graph should receive a tuple to access the 
# node positions. 
# this should be roughly the center, 20th col in 20th row. 

def find_surrounding(initial_posistion):
    """
    # TODO: find_surrounding - info about function

    What's this function doing? Input / output

    """
    seeker_list=[]

    next_x = initial_posistion +1

    if next_x not in Globals.wall_list:
        if initial_posistion%NODE_NUM_H ==NODE_NUM_H - 1:
            pass
        else:
            seeker_list.append(next_x)

    prev_x = initial_posistion -1

    if prev_x not in Globals.wall_list:
        if initial_posistion%NODE_NUM_H == 0:
            pass
        else:
            seeker_list.append(prev_x)

    next_y = initial_posistion + NODE_NUM_W

    if next_y not in Globals.wall_list:
        if next_y > MATRIX_TOTAL_NODE_AMOUNT:
            pass
        else:
            seeker_list.append(next_y)

    prev_y = initial_posistion - NODE_NUM_W

    if prev_y not in Globals.wall_list:
        if prev_y < 0:
            pass
        else:
            seeker_list.append(prev_y)

    return seeker_list

fixed_robot = None
prev_seeker_list = set()

item_list = random.sample(xrange(MATRIX_TOTAL_NODE_AMOUNT), Globals.item_num)

def convert(co_ord):
    index = co_ord[1] + co_ord[0]*NODE_NUM_W
    return index

def convert_index(index):
    co_ord = (index//NODE_NUM_W, index%NODE_NUM_W)
    return co_ord

def robot_square(event):
    global start_time
    global fixed_robot
    global prev_seeker_list
    """
    Test function - Defines the clicked node as the robot from mouse selection
    """
    robot = test_graph.matrix[event.x//NODE_SIZE][event.y//NODE_SIZE] # Get the correct node
    robot.set_robot() # Set the node as a robot
    robot.display()
    canvas.unbind('<Button-1>')
    robot_tuple = robot.return_node()
    fixed_robot = convert(robot_tuple)
    prev_seeker_list.add(fixed_robot)
    start_time = time.time()

canvas.bind('<Button-1>', lambda event: robot_square(event))


def wall(event):
    wall = test_graph.matrix[event.x//NODE_SIZE][event.y//NODE_SIZE]
    wall.set_wall()
    wall.display()
    wall_coords = wall.return_node()
    fixed_wall = convert(wall_coords)
    Globals.wall_list.append(fixed_wall)

canvas.bind('<Button-3>', lambda event: wall(event))

collected_item_names = set()
collected_item_list = []
paths = []
node_path_list = set()

def main_animate():

    """This function is for testing the animation and was added by george just
    for while he was looking at a get_all_neighbours method in the graph class
    """
    global prev_seeker_list
    global item_list
    global fixed_robot
    global collected_item_list
    global collected_item_names
    global node_path_list
    global paths
    new_seeker_list = set()
    count = 0
    last_pos_values = {}

    if fixed_robot != None:

        for i in prev_seeker_list:
            newNodes = find_surrounding(i)

            for node in newNodes:
                last_pos_values[node]= i

            new_seeker_list.update(newNodes)
            new_seeker_list.difference_update(prev_seeker_list)

        for a_row in test_graph.matrix:
            for a_node in a_row:

                for item in item_list:
                    if item in prev_seeker_list:
                      
                        for node in new_seeker_list:
                            node = convert_index(node)
                            if node[1] >= NODE_NUM_W:
                                pass
                            elif node[0] >= NODE_NUM_H:
                                pass
                            else:
                                node = test_graph.matrix[node[0]][node[1]]
                                node.reset()

                        for node in prev_seeker_list:
                            node = convert_index(node)
                            if node[1] >= NODE_NUM_W:
                                pass
                            elif node[0] >= NODE_NUM_H:
                                pass
                            else:
                                node = test_graph.matrix[node[0]][node[1]]
                                node.reset()

                        path_back = []
                        current_search = item

                        while True:
                            found = False
                            for path in paths:
                                if current_search in path:
                                    if current_search not in path_back:
                                        if current_search == fixed_robot:
                                            pass
                                        else:
                                            path_back.append(current_search)
                                            current_search = path[current_search]
                                            found = True
                                        break

                            if not found:
                                break

                        for path_node in path_back:
                            node_path_list.add(path_node)

                        new_seeker_list = set()
                        collected_item_list.append(fixed_robot)

                        item_node = convert_index(item)
                        item_node = test_graph.matrix[item_node[0]][item_node[1]]
                        Globals.item_names.append(item_node.item_name)

                        fixed_robot = item
                        prev_seeker_list = set()
                        prev_seeker_list.add(fixed_robot)
                        item_list.remove(item)
                        paths = []

                if count in new_seeker_list:
                    a_node.set_seeker()
                    a_node.display()
                    paths.append({count: last_pos_values[count]})

                if count in prev_seeker_list:
                    a_node.set_prev_seeker()
                    a_node.display()

                if count in node_path_list:
                    a_node.set_path()
                    a_node.display()

                if count in item_list:
                    a_node.set_item()
                    a_node.display()

                if count == fixed_robot:
                    a_node.set_robot()
                    a_node.display()

                if count in collected_item_list:
                    a_node.set_prev_robot()
                    a_node.display()

                count += 1

    prev_seeker_list.update(new_seeker_list)

    if start_time != None:
        run_time = time.time() - start_time
        if run_time >= Globals.time_num:
            end()

    root.after(SCREEN_REFRESH, main_animate)

###############################################################################

def end():
    for runthrough in range(len(Globals.item_names)-1,0,-1):
        for i in range(runthrough):
            if Globals.item_names[i]>Globals.item_names[i+1]:
                temp = Globals.item_names[i]
                Globals.item_names[i] = Globals.item_names[i+1]
                Globals.item_names[i+1] = temp
    root.destroy()
    import Sorted_List


root.after(SCREEN_REFRESH, main_animate)

root.mainloop()

root.destroy()
