import math as m
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
 
fig, ax = plt.subplots()
line, = plt.plot([], [], '-', color='black', label='line')
edge = 3

plt.axis('equal')
 
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)
 

 
def animate(frame):
    t = frame
  
    plt.scatter(0, 0, color='black')
    cn = np.sin(t)
    dn = np.cos(t)
    plt.plot((0, cn), (0, dn))
 
    



ani = animation.FuncAnimation(fig,
                        animate,
                        
                        frames=np.arange(0, 7, 1),
                        interval=300)
 
ani.save('my_anim.gif')