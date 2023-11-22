import numpy as np
import math

r = int(input("Number of rows of Jacobian matrix: "))          #Rows of the Jacobian Matrix
c = int(input("Number of column of Jacobian matrix: "))        #Columns of the JAcobian Matrix

J = []                                   #Jacobian Matrix

for i in range(r):          
    a =[]
    for j in range(c):      
        a.append(int(input()))
    J.append(a)                          #adding value in the Jacobian Matrix

X_dot = []
for i in range(r):         
    b =[]
    for j in range(1):      
        b.append(int(input()))
    X_dot.append(b)

J_inv = np.linalg.inv(J)
 
q_dot = np.dot(J_inv, X_dot)

print(q_dot)