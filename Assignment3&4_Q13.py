from math import *

x = int(input("x = "))                           #x coordinate of end-effector w.r.t. to base frame.
y = int(input("y = "))                           #y coordinate of end-effector w.r.t. to base frame.
z = int(input("z = "))                           #z coordinate of end-effector w.r.t. to base frame.

l1 = int(input("Link 1 length= "))
l2 = int(input("Lnik 2 length = "))
d1 = int(input("Link 3 height  = "))
d = d1 - z

q2 = acos ((x**2+y**2-l1**2-l2**2)/(2*l1*l2))
q1 = atan(y/x) - atan((l2*sin(q2))/(l1+l2*cos(q2)))

q2 = round(degrees(q2),2)
q1 = round(degrees(q1),2)
print("q1 = ",q1)
print("q2 = ",q2)


