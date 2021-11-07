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
    print("Running Gaussian elimination")
    while work.shape[0] > 0:
        best_index = work.argmax(axis=1)
        best = best_index.argmin()
        work[[0, best]] = work[[best, 0]]
        best = work[0]
        work = work[1:]
        indices = work[:,min(best_index)] == 1
        work[indices] = (work[indices] + best) % 2
        if invalid(work[indices]):
            raise Exception("Could not solve")
    free = (out == 0).all(axis=1).sum()
    print("Free variables: {}".format(free))
    print("Different solutions: {}".format(1 << free))
    out = filter_zero(out)
    work = out[:]
    r = [None]*output.shape[0]

    inv = np.zeros((work.shape[1],), dtype=int)
    inv[-1] = 1
    print("Finding solutions")
    while work.shape[0] > 0:
        best = work[-1]
        work = work[:-1]
        index = best.argmax()
        r[index] = (best[-1] == 1,list(np.where(best[index+1:-1] == 1)[0] + index+1))
        i = work[:,index] == 1
        work[i] += best
        work[i] %= 2
    indices = [i for (i, a) in enumerate(r) if a == None]
    for i in range(1 << len(indices)):
        p = [0] * len(r)
        for j, index in enumerate(indices):
            p[index] = int((i & (1 << j)) != 0)
        for j, v in enumerate(r):
            if v != None:
                p[j] = int(v[0])
                for k in v[1]:
                    p[j] += p[k]
                p[j] %= 2
        yield p
    return r

def count_ones(a):
    return len([None for v in a if v == 1])

def filter_results(results):
    r = list(results)
    lengths = [count_ones(v) for v in r]
    a = list(set(lengths))
    a.sort()
    print("Possible step counts: {}".format(a))
    print("Default solution takes {} steps".format(lengths[0]))
    m = a[0]
    return r[lengths.index(m)]