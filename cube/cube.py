import numpy as np
import matplotlib.pyplot as plt

# inspiration: CMU 15-462/662

verts = np.array([[1, 1, 1],
                  [1, 1, -1],
                  [1, -1, 1],
                  [1, -1, -1],
                  [-1, 1, 1],
                  [-1, 1, -1],
                  [-1, -1, 1],
                  [-1, -1, -1]], dtype=float)

edges = np.array([[0, 1],
                  [0, 2],
                  [0, 4],
                  [1, 3],
                  [1, 5],
                  [2, 3],
                  [2, 6],
                  [3, 7],
                  [4, 5],
                  [4, 6],
                  [5, 7],
                  [6, 7]])

center = np.array([2, 3, 5], dtype=float)

verts_c = verts - center

steps = np.linspace(0, 10, 10**2)

projs = verts_c[:, :2] / verts_c[:, 2:]

starts = projs[edges[:, 0]]
ends = projs[edges[:, 1]]

plt.scatter(starts[:, 0], starts[:, 1], color='black', marker='.')
plt.scatter(ends[:, 0], ends[:, 1], color='black', marker='.')

for i in range(len(edges)):
    plt.plot([starts[i, 0], ends[i, 0]], [starts[i, 1], ends[i, 1]], 'k')

plt.show()
