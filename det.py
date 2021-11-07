from numpy.core.defchararray import rindex
import lightsout
import numpy as np

columns = 3
rows = 3

solution_matrix = lightsout.solution_matrix(columns, rows)

print(np.linalg.det(solution_matrix))
print(np.linalg.inv(solution_matrix).round()%2)