import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Crear una figura y un eje 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Parámetros de la onda senoidal
amplitud = 1.0
frecuencia = 1.0
velocidad_fase = 0.1

# Valores iniciales
t = np.linspace(0, 2 * np.pi, 100)
x = amplitud * np.sin(frecuencia * t)
y = t
z = np.zeros_like(t)

# Crear un objeto de línea 3D que será animado
line, = ax.plot(x, y, z)

# Función de inicialización
def init():
    line.set_data([], [])
    line.set_3d_properties([])
    return line,

# Función de animación
def animate(i):
    x = amplitud * np.sin(frecuencia * t + velocidad_fase * i)
    line.set_data(x, y)
    line.set_3d_properties(z)
    return line,

# Crear la animación
ani = FuncAnimation(fig, animate, frames=100, init_func=init, blit=True)

plt.show()