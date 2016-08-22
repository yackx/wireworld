import tkinter as tk

block = 20

"""Displays the Wireworld and make it evolve to its next states"""
class Gui:

    """Init the GUI with the Wireworld"""
    def __init__(self, world):
        self.world = world

        self.root = tk.Tk()
        self.frame = tk.Frame(self.root)
        self.canvas = tk.Canvas(self.frame, width=600, height=400, bg="black")


    """Start animating the world"""
    def start(self):
        self.__draw()
        self.root.mainloop()


    """Draw the current state of the world, then pause.
    This function schedule a call to itself via `after`."""
    def __draw(self):
        # Draw cells
        for color, points in self.world.state().items():
            for point in points:
                point = [i * block for i in point]
                x, y = point
                self.canvas.create_rectangle(x, y, x+block, y+block, fill=color.name)

        # Render
        self.canvas.pack()
        self.frame.pack()

        # Next state
        self.world.tick()

        # Refresh periodically
        self.canvas.after(500, self.__draw)
