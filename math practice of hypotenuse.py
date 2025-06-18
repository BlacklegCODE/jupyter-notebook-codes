import math

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
def distance(q1, q2):
    return math.hypot(q2.x-q1.x,q2.y-q1.y)
q1=Point(10,1)
q2= Point(12,1)
res = distance(q1,q2)
print(res)
