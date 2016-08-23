#!/usr/bin/env python

from engine import Engine
from gui import Gui

import argparse


def main(path, delay):
    initial_state = Engine.load(path)
    ww = Engine(initial_state)
    Gui(ww, delay).start()


if __name__ == "__main__":
    parser = argparse.ArgumentParser('Wireworld animation')
    parser.add_argument('world', help='File path to a wireworld')
    parser.add_argument('delay', help='Delay (ms) between each frame')
    args = parser.parse_args()
    main(args.world, args.delay)
