import random
import math

flag = 0
fo = open("vf.txt", "r+")
vf = int(fo.read(5))
#vf = 20
time = 0

xf = random.randint(1, 1001)
yf = random.randint(1, 1001)
xb = random.randint(1, 1000)
yb = random.randint(1, 1001)

while flag == 0:
    distance = math.sqrt((xf - xb)**2 + (yf - yb)**2)
    print("time =", time, "xf =", xf, "yf =", yf, "xb =", xb, "yb =", yb, "distance =", distance)
    if distance <= 100:
        print("The Bomber Plane Shot Down at time", time)
        flag = 1
    elif distance > 900:
        print("The Bomber Plane Escape at time ", time)
        flag = 1
    else:
        xf = xf + vf * (xb - xf) / distance
        yf = yf + vf * (yb - yf) / distance
        xb = random.randint(1, 1001)
        yb = random.randint(1, 1001)
        time += 1
