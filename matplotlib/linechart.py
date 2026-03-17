

#! line chart

import matplotlib.pyplot as plt
import numpy as np

x = np.array([2024 , 2025, 2026])
y = np.array([19   , 50  , 21])
y2 = np.array([50 , 30 , 40 ])


# plot custimization
plot_custimization = dict(  color = "black",
                            linestyle = "dashed",
                            linewidth = 2,
                            marker = ".",
                            markersize = 20,
                            markerfacecolor = "red",
                            markeredgecolor = "black" )



# ** to deal with dictionary argument
plt.plot(x , y ,**plot_custimization)
plt.plot(x, y2 , **plot_custimization)


# title
title = dict(   fontfamily="Arial", 
                fontsize = 18, 
                color= "purple",
                fontweight = 'bold')

plt.title('class size' , **title)


plt.xlabel('year')
plt.ylabel('class')
# to remove additions in values
plt.xticks(x)


# grid
plt.grid(axis = 'y', linestyle = "dotted" , color = "red" , linewidth = 2)
# plt.grid()


# output
plt.show()


