#!/usr/bin/env python

from engine import Engine
from gui import Gui

import argparse


def main(path):
    initial_state = Engine.load(path)
    ww = Engine(initial_state)
    Gui(ww).start()


if __name__ == "__main__":
    parser = argparse.ArgumentParser('Wireworld animation')
    parser.add_argument('world', help='File path to a wireworld')
    args = parser.parse_args()
    main(args.world)
