from itertools import product

class Engine:

    def __init__(self, world):
        self.world = world

        # All neighbors as delta (-1,-1 to 1, 1)
        self.dd = list(product([-1, 0, 1], repeat= 2))
        self.dd.remove((0, 0))


    def state(self):
        return self.world


    def tick(self):
        new_world = Engine.__new_world()

        # conductor -> head if 1 or 2 neighbors, conductor otherwise
        for x, y in self.world['yellow']:
            n = sum((x+dx, y+dy) in self.world['blue'] for dx, dy in self.dd)
            if n == 1 or n == 2:
                color = 'blue'
            else:
                color = 'yellow'
            new_world[color].append((x, y))

        new_world['red'] = self.world['blue']       # head -> tail
        new_world['yellow'] += self.world['red']    # tail -> conductor

        self.world = new_world
        return self.world


    @staticmethod
    def __new_world():
        world = dict()
        for k in ['blue', 'red', 'yellow']:
            world[k] = []
        return world


    @staticmethod
    def __char_to_color(c):
        if c == '.': return 'yellow'
        if c == 't': return 'red'
        if c == 'H': return 'blue'
        raise Exception('Unknown char: ' + c)


    @staticmethod
    def load(file_name):
        world = Engine.__new_world()

        with open(file_name, 'r') as f:
            for line_number, line in enumerate(f):
                line = line.rstrip('\n\r ')
                for char_index, c in enumerate(line):
                    if c != ' ':
                        world[Engine.__char_to_color(c)].append((char_index, line_number))

        return world
