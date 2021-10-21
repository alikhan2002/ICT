import math

t1 = int(input())
g1 = int(input())

t2 = int(input())
g2 = int(input())

t1 *= (math.pi/180)
t2 *= (math.pi/180)
g1 *= (math.pi/180)
g2 *= (math.pi/180)
distance = 6371.01 *math.acos(math.sin(t1) * math.sin(t2) + math.cos(t1) * math.cos(t2)*math.cos(g1 - g2))
print("distance is", "%.5f" % distance)
