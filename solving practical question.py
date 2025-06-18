#(c) Using python, represent the following information using a bar graph (in green color )
#Item clothing Food rent Petrol Misc.
#expenditure in Rs 600 4000 2000 1500 700


import matplotlib.pyplot as plt
import numpy as np
left = [1,2,3,4,5]
height = [600 ,4000, 2000, 1500, 700]
plt.bar(left,height,width = 0.4,color = 'g')
plt.ylabel('Expenditure')
plt.xlabel('clothing,food,rent,pertol,misc')
plt.title('The Graph')
plt.show()
