#!/usr/bin/env python

import Tkinter as tk
import time
from itertools import product


block = 20


def char_to_color(c):
    if c == '.': return 'yellow'
    if c == 't': return 'red'
    if c == 'H': return 'blue'
    raise Exception('Unknown char: ' + c)


def load_object(name):
    world = dict()
    for k in ['blue', 'red', 'yellow']:
        world[k] = []

    with open(name + '.txt', 'r') as f:
        for line_number, line in enumerate(f):
            line = line.rstrip('\n\r ')
            for char_index, c in enumerate(line):
                if c != ' ':
                    world[char_to_color(c)].append((char_index, line_number))

    return world


def tick(world):
    new_world = dict()

    dd = list(product([-1, 0, 1], repeat= 2))
    dd.remove((0, 0))

    new_world['blue'] = []
    new_world['yellow']= []
    for x, y in world['yellow']:
        n = sum((x+dx, y+dy) in world['blue'] for dx, dy in dd)
        if n == 1 or n == 2:
            color = 'blue'
        else:
            color = 'yellow'
        #print "{0}, {1} has {2} neighbors".format(x, y, n)
        new_world[color].append((x, y))

    # head -> tail
    new_world['red'] = world['blue']
    # tail -> conductor
    new_world['yellow'] += world['red']

    return new_world


def draw(frame, canvas):
    global ww

    # Draw cells
    for color, points in ww.iteritems():
        for point in points:
            point = [i * block for i in point]
            x, y = point
            canvas.create_rectangle(x, y, x+block, y+block, fill=color)
    # Render
    canvas.pack()
    frame.pack()
    # Next state
    ww = tick(ww)

    canvas.after(500, draw, frame, canvas)


def main():
    global ww
    ww = load_object('diode')

    # Tk, frame and canvas
    root = tk.Tk()
    frame = tk.Frame(root)
    canvas = tk.Canvas(frame, width=600, height=400, bg="black")
    draw(frame, canvas)
    root.mainloop()


if __name__ == "__main__":
    main()
