#Write a Python program to reflect the line segment joining the points A[5, 3] and B[1, 4] t
#the line y = x + 1.

from sympy import*
x,y=symbols('x,y')
A = Point(5,3)
B = Point(1,4)
S = Segment(A,B)
S.reflect(Line(x-y+1))
