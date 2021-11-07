import gauss_all as gauss
import lightsout
import numpy as np

#current = np.zeros((21, 21))
current = np.zeros((11, 11))

destination = np.zeros_like(current)

dest = (current + destination) % 2

columns = dest.shape[1]
rows = dest.shape[0]

dest = dest.reshape((rows*columns, ))

print("Generating truth matrix...")

solution_matrix = lightsout.solution_matrix(columns, rows)
print("Done!")

solution = gauss.gauss(solution_matrix, dest)
best_solution = gauss.filter_results(solution)
print("Best solution has {} steps".format(gauss.count_ones(best_solution)))

solution_board = lightsout.Board.from_flat(best_solution, columns, rows)

print(solution_board)