#!/usr/bin/env python

import Tkinter as tk

from world import World


block = 20


def draw(frame, canvas):
    global ww

    # Draw cells
    ww.state()
    for color, points in ww.state().iteritems():
        for point in points:
            point = [i * block for i in point]
            x, y = point
            canvas.create_rectangle(x, y, x+block, y+block, fill=color)
    # Render
    canvas.pack()
    frame.pack()
    # Next state
    ww.tick()

    canvas.after(500, draw, frame, canvas)


def main():
    global ww

    initial_state = World.load('diode.txt')
    ww = World(initial_state)

    # Tk, frame and canvas
    root = tk.Tk()
    frame = tk.Frame(root)
    canvas = tk.Canvas(frame, width=600, height=400, bg="black")
    draw(frame, canvas)
    root.mainloop()


if __name__ == "__main__":
    main()
