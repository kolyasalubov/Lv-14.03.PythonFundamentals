
import random

class Ghost(object):
    colours = ["white", "yellow", "red", "purple"]

    def __init__(self):
        self.color = random.choice(Ghost.colours)
        