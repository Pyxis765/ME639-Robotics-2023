import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

L1 = 1.0                              # Link 1 length
L2 = 1.0                              # Link 2 length
L3 = 1.0                              # Link 3 length
phie = 30

def desired_curve(t):                # Function for path 
    x = 1.5 * np.cos(t)
    y = 1.5 * np.sin(t)
    return x, y

def inv_kine(x, y):
    c2 = (((x**2)/L1) + ((y**2)/L2) - L1**2 - L2**2) / (2 * L1 * L2)   #Ellipse fucntion for tracing
    s2 = np.sqrt(1 - c2**2)
    q1 = np.arctan2(y, x) - np.arctan2(L2 * s2, L1 + L2 * c2)
    q2 = np.arctan2(s2, c2)
    q3 = phie - (q2 + q1)
    return q1, q2, q3

timesteps = 100
t_vals = np.linspace(0, 2 * np.pi, timesteps)

# Animation
fig, ax = plt.subplots()
ax.set_xlim(-4, 4)
ax.set_ylim(-4, 4)

link1, = ax.plot([], [], 'b-', lw=2)
link2, = ax.plot([], [], 'g-', lw=2, color='yellow')
link3, = ax.plot([], [], 'r-', lw=2)
endpoint, = ax.plot([], [], 'ro', color='black')
trajectory, = ax.plot([], [], 'k-', lw=1, color= 'green')  # Green line for tracing the trajectory

trajectory_x = []  # Lists to store the trajectory
trajectory_y = []

def fun_animation(frame):
    t = t_vals[frame]
    x_d, y_d = desired_curve(t)
    q1, q2, q3 = inv_kine(x_d, y_d)
    x1 = L1 * np.cos(q1)
    y1 = L1 * np.sin(q1)
    x2 = x1 + L2 * np.cos(q1 + q2)
    y2 = y1 + L2 * np.sin(q1 + q2)
    x3 = x2 + L3 * np.cos(phie)
    y3 = y2 + L3 * np.sin(phie)

    trajectory_x.append(x3)  # Append the current position to the trajectory
    trajectory_y.append(y3)

    link1.set_data([0, x1], [0, y1])
    link2.set_data([x1, x2], [y1, y2])
    link3.set_data([x2, x3], [y2, y3])
    endpoint.set_data(x3, y3)
    trajectory.set_data(trajectory_x, trajectory_y)

    return link1, link2, link3, endpoint, trajectory

ani = FuncAnimation(fig, fun_animation, frames=timesteps, blit=True)
plt.show()
