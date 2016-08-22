from itertools import product
from enum import Enum
import itertools


"""A Color in the wireworld"""
class Color(Enum):
    yellow = '.'    # conductor
    blue = 'H'      # head
    red = 't'       # tail

    """Return the color corresponding to a character.
    Used when loading from file."""
    @staticmethod
    def char_to_color(c):
        if c == '.': return Color.yellow
        if c == 't': return Color.red
        if c == 'H': return Color.blue
        if c == 'b' or c == ' ': return None
        raise Exception('Unknown char: ' + c)


"""The Wireworld engine stores the world current state
and provides a method to step to the next state."""
class Engine:

    def __init__(self, world):
        self.world = world

        # All neighbors as delta (-1,-1 to 1, 1)
        self.dd = list(product([-1, 0, 1], repeat= 2))
        self.dd.remove((0, 0))

        # Compute dimensions
        values = world.values()
        points = list(itertools.chain(*values))
        self.size_x = max(points, key=lambda x: x[0])[0] + 1
        self.size_y = max(points, key=lambda x: x[1])[1] + 1


    """Return the current state of the world as a map.
    keys: Color; values: list of (x, y) tuples.

    For instance:
        {
            Color.blue:    [(2, 0)],
            Color.red:     [(1, 0)],
            Color.yellow:  [(0, 0), (3, 0)]
        }
    """
    def state(self):
        return self.world


    def dimensions(self):
        return (self.size_x, self.size_y)


    """Step the world to the next state."""
    def tick(self):
        new_world = Engine.__new_world()

        # conductor -> head if 1 or 2 neighbors, conductor otherwise
        for x, y in self.world[Color.yellow]:
            n = sum((x+dx, y+dy) in self.world[Color.blue] for dx, dy in self.dd)
            if n == 1 or n == 2:
                color = Color.blue
            else:
                color = Color.yellow
            new_world[color].append((x, y))

        new_world[Color.red] = self.world[Color.blue]       # head -> tail
        new_world[Color.yellow] += self.world[Color.red]    # tail -> conductor

        self.world = new_world
        return self.world



    """Create a new, empty world."""
    @staticmethod
    def __new_world():
        world = dict()
        for color in Color:
            world[color] = []
        return world


    """Load a world from a file.
    Expected format: 1 char per cell.
    `.` = conductor, `H` = head, `t` = tail.
    A space `' '` or nothing at the end of the line: empty
    """
    @staticmethod
    def load(file_name):
        world = Engine.__new_world()

        with open(file_name, 'r') as f:
            for line_number, line in enumerate(f):
                line = line.rstrip('\n\r ')
                for char_index, c in enumerate(line):
                    color = Color.char_to_color(c)
                    if color != None:
                        world[color].append((char_index, line_number))

        print(world)
        return world
