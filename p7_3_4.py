import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
 
fig, ax = plt.subplots()
line, = plt.plot([], [], '--', color='red', label='line')
 
edge = 25
 
plt.axis('equal')
 
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)
 
x, y = [], []
 
def animate(frame):
    t = np.arange(-10, 10, 0.01)
  
    xn = 12*np.cos(t)+8*np.cos(1.5*t)

    yn = 12*np.sin(t)-8*np.sin(1.5*t)
 
    x.append(xn)
    y.append(yn)
    line.set_data(x, y)
 
ani = animation.FuncAnimation(fig,
                        animate,
                        frames=np.arange(0, 10, 0.1),
                        interval=30)
 
ani.save('my_anim.gif')