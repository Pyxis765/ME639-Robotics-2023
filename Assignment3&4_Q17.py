from math import *

d1 = 1
l2 = 1
l3 = 1
d6 = 1

def inversekinematics(x, y, z, roll, pitch, yaw):

    # Wrist center position (O3)
    wc_x = x - d6 * cos(yaw) * cos(pitch)
    wc_y = y - d6 * sin(yaw) * cos(pitch)
    wc_z = z + d6 * sin(pitch)

    theta1 = atan2(wc_y, wc_x)

    d = sqrt(wc_x**2 + wc_y**2 + (wc_z - d1)**2)
    a = (d**2 - l2**2 - l3**2) / (2 * l2 * l3)
    beta = atan2(sqrt(1 - a**2), a)

    theta3 = pi - beta - atan2(l3 * sin(beta), l2 + l3 * cos(beta))

    k1 = l2 + l3 * cos(beta)
    k2 = l3 * sin(beta)
    thetl2 = atan2(wc_z - d1, sqrt(wc_x**2 + wc_y**2)) - atan2(k2, k1)

    theta4 = roll - thetl2 - theta3

    theta4 = (theta4 + pi) % (2 * pi) - pi

    theta5 = pitch - thetl2 - theta3

    theta6 = yaw - theta1

    return theta4, theta5, theta6



x = int(input("x = "))                           #x coordinate of end-effector w.r.t. to base frame.
y = int(input("y = "))                           #y coordinate of end-effector w.r.t. to base frame.
z = int(input("z = "))                           #z coordinate of end-effector w.r.t. to base frame.

roll = radians(30)
pitch = radians(45)
yaw = radians(60)

theta4, theta5, theta6 = inversekinematics(x, y, z, roll, pitch, yaw)
print("θ4:", degrees(theta4))
print("θ5:", degrees(theta5))
print("θ6:", degrees(theta6))
