import numpy as np

def filter_zero(a):
    return a[~np.all(a == 0, axis=1)]

def invalid(a):
    inv = np.zeros((a.shape[1],))
    inv[-1] = 1
    return any((a == inv).all(1))

#Not entirely correct, but I believe it should be fine for my use cases
#TODO: Find all solutions
def gauss(input, output):
    out = np.column_stack((input, output))
    work = out[:]
    while work.shape[0] > 0:
        if invalid(work):
            raise Exception("Could not solve")
        best_index = work.argmax(axis=1)
        best = best_index.argmin()
        work[[0, best]] = work[[best, 0]]
        best = work[0]
        work = work[1:]
        indices = work[:,min(best_index)] == 1
        work[indices] = (work[indices] + best) % 2
    print((out == 0).all(axis=1).sum())
    out = filter_zero(out)
    work = out[:]
    r = np.zeros(output.shape[0], dtype=int)

    inv = np.zeros((work.shape[1],), dtype=int)
    inv[-1] = 1

    while work.shape[0] > 0:
        best = work[-1]
        work = work[:-1]
        index = best.argmax()
        r[index] = best[-1]
        if r[index]:
            work[work[:,index] == 1] += inv
            work[work[:,index] == 1] %= 2
    return r