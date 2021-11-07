from numpy.core.defchararray import rindex
import lightsout
import numpy as np


dest = np.array([
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1],
])


columns = dest.shape[1]
rows = dest.shape[0]

dest = dest.reshape((rows*columns, ))

solution_matrix = lightsout.solution_matrix(columns, rows)


# Solve using inverse matrix
#inv = np.linalg.inv(solution_matrix)
#solution = inv.dot(dest)%2

# Solve using 'solve' method
solution = np.linalg.solve(solution_matrix, dest)%2
print(solution)

solution = solution.astype(int)

print(solution_matrix.dot(solution)%2)

solution_board = lightsout.Board.from_flat(list(solution), columns, rows)

print(solution_board)