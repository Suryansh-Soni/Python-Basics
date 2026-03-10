#  Problem 2: take radius and return area and circumference 

import math ;
def circle_stats(r):
    area=int(math.pi*r*r)
    circum=int(math.pi*2*r)
    return area,circum
print(circle_stats(5)) 

