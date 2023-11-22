import numpy as np
n = int(input('No. of links = '))

X_dot = np.zeros((3, 1))
print("\nGive input of Linear velocities of end effector in x,y,z direction")
for i in range(3):
    X_dot[i, 0] = int(input(f"V[{i}]: "))

J = np.zeros((3,3))

print("\nGive input of Jacobian matrix")
for i in range(3):
    for j in range(n):
        J[i,j] = int(input(f"J[{i}][{j}]: "))
print(f'Jacobian Matrix = \n{J}')

J_inv = np.linalg.inv(J)
q_dot = np.matmul(J_inv,X_dot)
print("\nJoint velocities are:")
print(q_dot)