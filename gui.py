import tkinter as tk

canvas_max_width = 1000
canvas_min_width = 20
canvas_max_height = 750
canvas_min_height = 15
block_max_size = 20
block_min_size = 1

"""Displays the Wireworld and make it evolve to its next states"""
class Gui:

    """Init the GUI with the Wireworld"""
    def __init__(self, world):
        self.world = world

        world_width, world_height = self.world.dimensions()
        canvas_width, canvas_height, self.block_size = self.__compute_sizes(world_width, world_height)

        self.root = tk.Tk()
        self.frame = tk.Frame(self.root)
        self.canvas = tk.Canvas(self.frame, width=canvas_width, height=canvas_height, bg="black")


    """Compute canvas and block sizes"""
    def __compute_sizes(self, world_width, world_height):
        canvas_width = int(world_width * block_max_size)
        if canvas_width > canvas_max_width:
            canvas_width = canvas_max_width
        elif canvas_width < canvas_min_width:
            canvas_width = canvas_min_width

        canvas_height = int(world_height * block_max_size)
        if canvas_height > canvas_max_height:
            canvas_height = canvas_max_height
        elif canvas_height < canvas_min_height:
            canvas_height = canvas_min_height

        block_width = block_max_size
        if block_width * world_width > canvas_width:
            block_width = canvas_width / world_width

        block_height = block_max_size
        if block_height * world_height > canvas_height:
            block_height = canvas_height / world_height

        block_size = max(block_width, block_height)
        if block_size < block_min_size:
            block_size = block_min_size

        print('world={0}/{1}, canvas={2}/{3}, block_size={4}'.format(
            world_width, world_height, canvas_width, canvas_height, block_size))

        return canvas_width, canvas_height, block_size


    """Start animating the world"""
    def start(self):
        self.__draw()
        self.root.mainloop()


    """Draw the current state of the world, then pause.
    This function schedules a call to itself via `after`."""
    def __draw(self):
        b_size = self.block_size
        # Draw cells
        for color, points in self.world.state().items():
            for point in points:
                point = [i * b_size for i in point]
                x, y = point
                self.canvas.create_rectangle(x, y, x+b_size, y+b_size, fill=color.name)

        # Render
        self.canvas.pack()
        self.frame.pack()

        # Next state
        self.world.tick()

        # Refresh periodically
        self.canvas.after(500, self.__draw)
