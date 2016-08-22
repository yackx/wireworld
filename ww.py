#!/usr/bin/env python

from engine import Engine
from gui import Gui


def main():
    initial_state = Engine.load('diode.txt')
    ww = Engine(initial_state)
    Gui(ww).start()


if __name__ == "__main__":
    main()
