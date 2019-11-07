
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,5,11)
y = x ** 2

plt.plot(x,y, 'r-')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('A main title')
# plt.show()


# making two subplots
plt.subplot(1,2,1)
plt.plot(x,y,'b-')

plt.subplot(1,2,2)
plt.plot(x,y,'r-')

plt.show()