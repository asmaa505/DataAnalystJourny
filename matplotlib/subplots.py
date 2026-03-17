

#

import matplotlib.pyplot as plt
import numpy as np

#! sub plots
figure , axes = plt.subplots( 2 , 2)
# plt.show()

x = np.array([1 , 2, 3, 4] )

axes[0,0].plot(x , x*2)

plt.show()
