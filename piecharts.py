from matplotlib import pyplot as plt

plt.title('My first Piechart')
slices=[60,30,54,88]
labels=['oranges','mangoes','lemons','bananas']
colors=['orange','green','red','yellow']
# explode used to emphasize
explode=[0,0,0.1,0]  
# to plot a pie chart use plt.pie()
plt.pie(slices,labels=labels,colors=colors,autopct='%1.1f%%',shadow=True,explode=explode,startangle=90,wedgeprops={'edgecolor':'#fff'})
# to show it out use plt.show()
plt.show()
# wedgeprops used to separate each slice by specifying a color
#to display percentage use autopct='%1.1f%%'