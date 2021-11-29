import matplotlib.pyplot as plt
import numpy as np

x = [1, 1, 5, 5, 1]
y = [1, 5, 5, 1, 1]

plt.plot(x, y, color='g', label='luchte', marker='>', ms=5)

plt.xlabel('Coord: x')
plt.ylabel('Coord: y')
plt.legend()
plt.title('Base')
plt.grid()
plt.show()
