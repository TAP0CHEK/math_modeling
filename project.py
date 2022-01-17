import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
 
R1=float(input('Введите радиус окружности: '))
r=float(input('Введите угол: '))
L=r*R1
print('Длина пройденного пути:',(L))



fig, ax = plt.subplots()
line, = plt.plot([], [], '-', color='blue', label='line')
edge = 2000

plt.axis('equal')
 
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)
 
a, b = [], []
 
def animate(frame):
    t = frame

    alpha = np.arange(-2*np.pi, 2*np.pi, 0.1)
    R=1
    an = R * np.cos(alpha)
    bn = R * np.sin(alpha)

    a.append(an)
    b.append(bn)

    line.set_data(a, b)

    plt.scatter(0, 0, color='black')

    cn = np.sin(t)
    dn = np.cos(t)
    plt.plot((0, cn), (0, dn))
 
ani = animation.FuncAnimation(fig,
                        animate,
                        
                        frames=np.arange(0, 7, 1),
                        interval=300)
 
ani.save('sobaka.gif')
