import numpy as np
import itertools

class Board:
    def __init__(self, columns, rows):
        self.columns = columns
        self.rows = rows
        self.board = [[0]*columns for _ in range(rows)]
    
    def from_flat(flat, columns, rows):
        assert columns*rows == len(flat)
        b = Board(columns, rows)
        for y in range(rows):
            b.board[y] = flat[y*columns:(1+y)*columns]
        return b
    
    def flatten(self):
        return list(itertools.chain(*self.board))
    
    def _flip_bit(self, x, y):
        if x >= 0 and x < self.columns and y >= 0 and y < self.rows:
            self.board[y][x] = 1 - self.board[y][x]

    def flip(self, x, y):
        self._flip_bit(x, y)
        self._flip_bit(x-1, y)
        self._flip_bit(x+1, y)
        self._flip_bit(x, y-1)
        self._flip_bit(x, y+1)
    def __str__(self):
        return "\n".join([" ".join([str(v) for v in row]) for row in self.board])

class BoardVariant(Board):
    def flip(self, x, y):
        self._flip_bit(x, y)
        for v in range(self.columns):
            self._flip_bit(v, y)
        for v in range(self.rows):
            self._flip_bit(x, v)

def _flipped(columns, rows, x, y, ctor):
    b = ctor(columns, rows)
    b.flip(x, y)
    return b.flatten()

def _solution_matrix(columns, rows, ctor):
    vectors = []
    for y in range(rows):
        for x in range(columns):
            vectors.append(_flipped(columns, rows, x, y, ctor))
    return np.column_stack(vectors)

def solution_matrix(columns, rows):
    return _solution_matrix(columns, rows, Board)
def solution_matrix_variant(columns, rows):
    return _solution_matrix(columns, rows, BoardVariant)