from Tkinter import *
import math
import random
import time
from itertools import chain


# from Node import Node
# from AllGraph import Graph

###############################################################################
# this is just a class with a few helper functions in it

class Helpers:

    def __init__(self):
        self.helper = 'helpful'

    def wait(self, t, m=""):
        """
        Pause output for given amount of seconds
        """
        print("{}".format(m))
        for i in range(t):
            print("...")
            time.sleep(1)

    def info(self, i):
        print(i)

