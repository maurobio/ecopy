import numpy as np

def _isotonic_regression(y, weight, solution):
    y = np.asarray(y, dtype=float)
    weight = np.asarray(weight, dtype=float)
    solution = np.asarray(solution, dtype=float)
    solution[:] = y
    n = len(solution)
    if n <= 1:
        return solution
    n -= 1
    while True:
        i = 0
        pooled = False
        while i < n:
            k = i
            while k < n and solution[k] >= solution[k + 1]:
                k += 1
            if solution[i] != solution[k]:
                numerator = np.sum(solution[i:k+1] * weight[i:k+1])
                denominator = np.sum(weight[i:k+1])
                solution[i:k+1] = numerator / denominator
                pooled = True
            i = k + 1
        if not pooled:
            break
    return solution
