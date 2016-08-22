#!/usr/bin/env python

import tkinter as tk

from engine import Engine


block = 20


def draw(frame, canvas):
    global ww

    # Draw cells
    ww.state()
    for color, points in ww.state().items():
        for point in points:
            point = [i * block for i in point]
            x, y = point
            canvas.create_rectangle(x, y, x+block, y+block, fill=color.name)
    # Render
    canvas.pack()
    frame.pack()
    # Next state
    ww.tick()

    canvas.after(500, draw, frame, canvas)


def main():
    global ww

    initial_state = Engine.load('diode.txt')
    ww = Engine(initial_state)

    # Tk, frame and canvas
    root = tk.Tk()
    frame = tk.Frame(root)
    canvas = tk.Canvas(frame, width=600, height=400, bg="black")
    draw(frame, canvas)
    root.mainloop()


if __name__ == "__main__":
    main()
