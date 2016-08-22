from itertools import product

class World:

    def __init__(self, world):
        self.world = world


    def state(self):
        return self.world


    def tick(self):
        new_world = dict()

        dd = list(product([-1, 0, 1], repeat= 2))
        dd.remove((0, 0))

        new_world['blue'] = []
        new_world['yellow']= []
        for x, y in self.world['yellow']:
            n = sum((x+dx, y+dy) in self.world['blue'] for dx, dy in dd)
            if n == 1 or n == 2:
                color = 'blue'
            else:
                color = 'yellow'
            #print "{0}, {1} has {2} neighbors".format(x, y, n)
            new_world[color].append((x, y))

        # head -> tail
        new_world['red'] = self.world['blue']
        # tail -> conductor
        new_world['yellow'] += self.world['red']

        self.world = new_world
        return self.world


    @staticmethod
    def __char_to_color(c):
        if c == '.': return 'yellow'
        if c == 't': return 'red'
        if c == 'H': return 'blue'
        raise Exception('Unknown char: ' + c)


    @staticmethod
    def load(file_name):
        world = dict()
        for k in ['blue', 'red', 'yellow']:
            world[k] = []

        with open(file_name, 'r') as f:
            for line_number, line in enumerate(f):
                line = line.rstrip('\n\r ')
                for char_index, c in enumerate(line):
                    if c != ' ':
                        world[World.__char_to_color(c)].append((char_index, line_number))

        return world
