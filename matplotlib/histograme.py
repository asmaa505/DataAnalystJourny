

#! histogram

#import
import matplotlib.pyplot as plt
import numpy as np




scores = np.random.normal( loc=80 , scale = 50 , size=100)
# range
scores = np.clip(scores, 0, 100)

# loc => location of the center
# scale => std

plt.hist(scores , bins = 15,
                color = 'lightgreen',
                edgecolor = 'black')


plt.title('exam score')
plt.xlabel('score')
plt.ylabel('num of students')

# output
plt.show()