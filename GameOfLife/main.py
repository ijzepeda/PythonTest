# /usr/env/python
# encoding:utf-8

import os
import time
from GameOfLife import GameOfLife

clear = lambda: os.system('clear')

def main():
    clear()
    print("Game of Life")
    rows, cols = int(input("How many Rows:")), int(input("How many Columns:"))
    game = GameOfLife(rows, cols)
    while True:
        clear()
        print(game)
        game.iterate()
        time.sleep(0.5)


if __name__ == '__main__':
    main()
