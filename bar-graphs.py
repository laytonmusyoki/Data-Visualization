from matplotlib import pyplot as plt
x=['Information technology','Computer science','Bussiness with IT']
h=[300,110,240]
w=[0.4,0.5,0.6]
colors=['red','green','blue']
plt.bar(x,h,width=w,color=colors)
plt.title('Students enrolled at kabarak university 2023')
plt.xlabel('courses')
plt.ylabel('students enrolled')

plt.show()

# arguments plt.bar() takes x-axis values,height values, color,width