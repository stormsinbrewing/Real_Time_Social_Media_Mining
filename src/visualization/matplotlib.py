import matplotlib.pyplot as plt

print("1. Simple Graph")
print("2. Bar Graph")
print("3. Histogram")
print("4. Pie Chart")
print("5. Stack Plot")
g=int(input("Enter your choice : "))
def choice(x):
	if(x==1):
	    x = [5,2,7]
	    y = [2,16,4]
	    plt.plot(x,y)
	    plt.title('DATA')
	    plt.ylabel('Y axis')	
	    plt.xlabel('X axis')
	    plt.show()
	elif(x==2):
		plt.bar([0.25,1.25,2.25,3.25,4.25],[50,40,70,80,20],label="BMW",width=.5)
		plt.bar([.75,1.75,2.75,3.75,4.75],[80,20,20,50,60],label="Audi", color='r',width=.5)
		plt.legend()
		plt.xlabel('Days')
		plt.ylabel('Distance (kms)')
		plt.title('Information')
		plt.show()
	elif(x==3):
		population_age = [22,55,62,45,21,22,34,42,42,4,2,102,95,85,55,110,120,70,65,55,111,115,80,75,65,54,44,43,42,48]
		bins = [0,10,20,30,40,50,60,70,80,90,100]
		plt.hist(population_age, bins, histtype='bar', rwidth=0.8)
		plt.xlabel('age groups')
		plt.ylabel('Number of people')
		plt.title('Histogram')
		plt.show()
	elif(x==4):
		days = [1,2,3,4,5]
		sleeping =[7,8,6,11,7]
		eating = [2,3,4,3,2]
		working =[7,8,7,2,2]
		playing = [8,5,7,8,13]
		slices = [7,2,2,13]
		activities = ['sleeping','eating','working','playing']
		cols = ['c','m','r','b']
		plt.pie(slices,labels=activities,colors=cols,startangle=90,shadow= True,explode=(0,0.1,0,0),autopct='%1.1f%%')
		plt.title('Pie Plot')
		plt.show()
	else:
		days = [1,2,3,4,5]
		sleeping =[7,8,6,11,7]
		eating = [2,3,4,3,2]
		working =[7,8,7,2,2]
		playing = [8,5,7,8,13]
		plt.plot([],[],color='m', label='Sleeping', linewidth=5)
		plt.plot([],[],color='c', label='Eating', linewidth=5)
		plt.plot([],[],color='r', label='Working', linewidth=5)
		plt.plot([],[],color='k', label='Playing', linewidth=5)
		plt.stackplot(days, sleeping,eating,working,playing, colors=['m','c','r','k'])
		plt.xlabel('x')
		plt.ylabel('y')
		plt.title('Stack Plot')
		plt.legend()
		plt.show()
if(g<=5 and g>=1):
	choice(g)
else:
	print("Choose correct choice")
