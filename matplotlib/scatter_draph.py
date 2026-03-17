
#! scatter graph

#import
import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3, 4, 5])
y = np.array([10, 20, 30, 40, 50])

plt.scatter(x , y , label = 'class A')

x2 = np.array([5, 3, 4, 9, 6])
y2 = np.array([10, 20, 30, 40, 50])

plt.scatter(x2 , y2 , label = 'class B' , color="red")

plt.xlabel('days')
plt.ylabel('size')
plt.title('size of the plant')

plt.legend()

plt.show()

