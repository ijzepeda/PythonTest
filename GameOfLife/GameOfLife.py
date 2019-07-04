# /usr/env/python
# encoding:utf-8

import random
import itertools


class GameOfLife(object):

    def __init__(self, rows, columns):
        self.rows = rows
        self.cols = columns
        row_life = lambda: [random.randint(0, 1) for n in range(self.cols)]
        self.game = [row_life() for n in range(self.rows)]

    def __str__(self):
        game = ''
        for row in self.game:
            for cell in row:
                game += '🀫 ' if cell else '. '
            game += '\n'
        return game

    def neighbour(self, row_no, col_no):
        #         Permutaciones de -1,1, en coordenadas, puedo usarlo hay una libreria
        # el set los hace un conjunto [tipo de lista] y omite las repeticiones, de ahi se pasa a lista
        nei_distance = list(set(itertools.permutations([-1, -1, 1, 1, 0], 2)))
        # regresa true or false si esta dentro o fuera de juego
        out_of_border = lambda x, y: not (x in range(self.rows) and y in range(self.cols))
        neighbours = 0
        for row_dist, col_dist in nei_distance:
            if not out_of_border(row_no + row_dist, col_no + col_dist):
                neighbours += 1 if self.game[row_no + row_dist][col_no + col_dist] else 0  # a '\' is added if I enter newline before 'else' IDKW
        return neighbours

    # core game logic
    def iterate(self):
        for row_no in range(self.rows):
            for col_no in range(self.cols):
                neighbours = self.neighbour(row_no, col_no)
                if neighbours < 2 or neighbours > 3:
                    self.game[row_no][col_no] = 0  # die or keep death
                elif neighbours == 3:
                    self.game[row_no][col_no] = 1  # born or keep alive



# GameOfLife obj