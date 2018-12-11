import tkinter as tk


class Gui:
    """Displays the Wireworld and make it evolve to its next states"""

    def __init__(self, world, delay):
        """Init the GUI with the Wireworld"""
        self.world = world
        self.delay = delay

        world_width, world_height = self.world.dimensions()
        canvas_width, canvas_height, self.block_size = self.__compute_sizes(world_width, world_height)

        self.root = tk.Tk()
        self.root.title('Wireworld')
        self.frame = tk.Frame(self.root)
        self.canvas = tk.Canvas(self.frame, width=canvas_width, height=canvas_height, bg="black")

    def __compute_sizes(self, world_width, world_height):
        """Compute canvas and block sizes"""
        canvas_max_width = 1000
        canvas_min_width = 20
        canvas_max_height = 750
        canvas_min_height = 15
        block_max_size = 20
        block_min_size = 2

        def clip(lo, x, hi):
            return lo if x <= lo else hi if x >= hi else x

        canvas_width  = clip(canvas_min_width, world_width*block_max_size, canvas_max_width)
        canvas_height = clip(canvas_min_height, world_height*block_max_size, canvas_max_height)

        block_width = int(min(canvas_width / world_width, block_max_size))
        block_height = int(min(canvas_height / world_height, block_max_size))
        block_size = int(max(min(block_width, block_height), block_min_size))

        print('world={0}/{1}, canvas={2}/{3}, block_size={4}'.format(
            world_width, world_height, canvas_width, canvas_height, block_size))

        return canvas_width, canvas_height, block_size

    def start(self):
        """Start animating the world"""
        self.__draw()
        self.root.mainloop()

    def __draw(self):
        """Draw the current state of the world, then pause.
        This function schedules a call to itself via `after`."""
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
        self.canvas.after(self.delay, self.__draw)
