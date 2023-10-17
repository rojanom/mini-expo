import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Crear datos de ejemplo
theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
z = np.linspace(-2, 2, 100)
r = z**2 + 1
x = r * np.sin(theta)
y = r * np.cos(theta)

# Configurar la figura y el eje 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

line, = ax.plot(x, y, z)
# Función de inicialización para la animación
def init():
    line, = ax.plot([], [], [], lw=2)
    return line,

# Función de actualización para la animación
def animate(i):
    line.set_data(x[:i], y[:i])
    line.set_3d_properties(z[:i])
    return line,

# Crear la animación
ani = FuncAnimation(fig, animate, init_func=init, frames=len(x), interval=20, blit=True)

# Mostrar la animación
plt.show()
