import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

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

r = 3
z = 5
center = np.array([r, 0, z], dtype=float)

verts_c = verts - center

total_steps = 2**8
steps = np.linspace(0, 1, total_steps, dtype=float)

fig, ax = plt.subplots()
ax.axis([-r/2, r/2, -r/2, r/2])
ax.set_aspect('equal')

lines = []
s1 = None
s2 = None

projs = verts_c[:, :2] / verts_c[:, 2:]

starts = projs[edges[:, 0]]
ends = projs[edges[:, 1]]

s1 = ax.scatter(projs[:, 0], projs[:, 1], color='red', marker='.')

for i in range(len(edges)):
    line, = ax.plot([starts[i, 0], ends[i, 0]], [starts[i, 1], ends[i, 1]], 'k')
    lines.append(line)

def update(step):
    center = [r * np.cos(2 * np.pi * step),
              r * np.sin(2 * np.pi * step),
              z]

    verts_c = verts - center

    projs = verts_c[:, :2] / verts_c[:, 2:]

    starts = projs[edges[:, 0]]
    ends = projs[edges[:, 1]]

    s1.set_offsets(np.column_stack([starts[:, 0], starts[:, 1]]))

    for i in range(len(edges)):
        lines[i].set_xdata([starts[i, 0], ends[i, 0]])
        lines[i].set_ydata([starts[i, 1], ends[i, 1]])

    return s1, *lines

ani = FuncAnimation(fig, update, frames=steps, blit=True, interval=20, repeat=False)
plt.show()
