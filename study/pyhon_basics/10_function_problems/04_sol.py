import math

def circle(r):
    area = math.pi * r ** 2
    cir  = math.pi * 2 * r

    return area , cir


num = circle(56)
print(round(num[1],2)) 