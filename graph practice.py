import matplotlib.pyplot as plt
left = [1,2,3,4,5]
height = [5,24,45,32,15]
tick_label = ['Pune','Mumbai','Nagpur','Nashik','Satara']
plt.bar(left, height,tick_label = tick_label,
        width = 0.8, color = ['red','green'])
plt.xlabel('cities')
plt.ylabel('No of covid patients(in thousands)')
plt.title('Covid-19 data')
plt.show()
