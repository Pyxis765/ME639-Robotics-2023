import numpy as np
import math 

P = [0, 0, 0]


for i in range(3):
    P[i] = int(input())
# P = input().split()
# for i in range(0,3):
#     P[i] = int(P[i])
def d2r( angle ):
    angle = (angle/180)*3.14
    return angle

def r2d(angle):
    angle = (angle/3.14)*180
    return angle

l1 = 1
l2 = 1
l3 = 1

r = np.sqrt(P[0]*P[0] + P[1]*P[1])


theta_1 = np.arctan(P[0]/P[1])
theta_2 = np.arctan(r/P[2])

print(r2d(theta_1))
print(r2d(theta_2))


