
#! pie chart

# import
import matplotlib.pyplot as plt
import numpy as np

city = np.array( ['damietta' , 'mansoura' , 'caito' , 'aswan'] )
population = np.array( [2000 , 5000 , 80000, 6000] )

plt.pie(population , labels = population , explode = [0 , 0 , 0, 0.2] , shadow = True)

# output
plt.show()
