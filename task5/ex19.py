from math import sqrt
acceleration = 9.8
height = float(input())

velocity = sqrt(2*acceleration*height)

print("the final speed:","%.2f"% velocity)