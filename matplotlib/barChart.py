

#! barchart

# import
import matplotlib.pyplot as plt
import numpy as np

city = np.array( ['damietta' , 'mansoura' , 'caito' , 'aswan'] )
population = np.array( [2000 , 5000 , 80000, 6000] )

# plt.bar( city , population, color=['pink' , 'purple' , 'red'] )
plt.barh( city , population, color=['pink' , 'purple' , 'red'] )
plt.title('city population')
plt.xlabel('city')
plt.ylabel('population')


# output
plt.show()