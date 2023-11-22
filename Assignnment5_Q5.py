import numpy as np
import math

R = []                      #Rotation Matrix
n = 0
while n<3:          
    a =[]
    for j in range(3):    
        a.append(int(input()))
    R.append(a)
    n += 1
    


R03 = []                    #Rotation Matrix for first three links

for p in range(3):          
    b =[]
    for q in range(3):      
        b.append(int(input()))
    R03.append(a)


q = [0, 0, 0]              #Joint angles for the Spherical Wrist

def trans(A, B):
    for i in range(3):
        for j in range(3):
            B[i][j] = A[j][i]

R03_Trans = R03[:][:]
R03_Trans = trans(R03, R03_Trans)

R36  = np.dot(R03_Trans, R)


if (R36[1][3] ==0 & R36[2][3] == 0):          #By using Inverse Kinematics, calculating Joint angles
    if(R36[3][3] == 1):
        q[1] = 0
        q[0] = 0
        q[2] = math.atan(R36[2][1], R36[1][1])
    elif(R36[3][3] == -1):
        q[1] = 3.14
        q[0] = 0
        q[2] = math.atan(-R36[2][1], -R36[2][2])

else:
    q[1] = math.atan(R36[3][3], math.sqrt(1 - R36[3][3]**2))
    q[0] = math.atan( R36[1][3], R36[2][3])
    q[2] = math.atan(-R36[3][1], R36[3][2])

print("q[0] = theta_4 \nq[1] = theta_5 \nq[2] = theta_6")
print(q)
