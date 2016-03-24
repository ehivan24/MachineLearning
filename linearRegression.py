__author__ = 'edwingsantos'
from scipy import stats
import numpy as np
from matplotlib import pyplot as plt

x = np.array([112, 345, 198, 306, 372, 660, 302, 420, 678])
y = np.array([1120,1623, 2102, 2230, 2600, 3200, 3409, 3685, 4460 ])

slope, intercept, r_value, p_value, std_error = stats.linregress(x, y)
plt.plot(x,y, 'ro', color='black')
plt.ylabel('Price')
plt.xlabel('Size of House')
plt.axis([0,600,0,5000])

plt.plot(x, x*slope+intercept, 'b')#y=b0+b1*x

#y=a*x+b
newX = 150
newY = newX*slope+intercept

print(newY) 
plt.plot(newX, newY, 'ro', color='red') #house price
plt.show()