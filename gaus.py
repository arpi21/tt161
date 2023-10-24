import numpy as np

def gaus(A, b):
    n = len(A)
    m = np.column_stack((A, b))

    for i in range(n):
        pivot_row = i
        for j in range(i + 1, n):
            if abs(m[j, i]) > abs(m[pivot_row, i]):
                pivot_row = j

        m[[i, pivot_row]] = m[[pivot_row, i]]

        for j in range(i + 1, n):
            factor = m[j, i] / m[i, i]
            m[j, i:] -= factor * m[i, i:]


    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (m[i, -1] - np.sum(m[i, i+1:n] * x[i+1:])) / m[i, i]

    return x

A = np.array([[2, 1, -1],
              [3, 2, 1],
              [1, 3, 2]], dtype=float)
b = np.array([8, 11, 6], dtype=float)
x_vector = gaus(A, b)
print(x_vector)
