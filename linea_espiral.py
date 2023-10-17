import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Crear una figura 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Datos iniciales
x = np.linspace(0, 10, 100)
y = np.sin(x)
z = np.cos(x)

# Inicialización de la línea
line, = ax.plot(x, y, z)

# Función para actualizar la línea en cada fotograma
def update(frame):
    # Actualizar los datos de la línea
    line.set_data(x[:frame], y[:frame])
    line.set_3d_properties(z[:frame])
    return line,

# Crear la animación
ani = FuncAnimation(fig, update, frames=len(x), interval=100)

plt.show()


