
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Crea una figura y un eje 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Datos de ejemplo
n = 100
x = np.random.rand(n)
y = np.random.rand(n)
z = np.random.rand(n)
colors = np.random.rand(n)

# Configura la dispersión inicial
scatter = ax.scatter(x, y, z, c=colors, cmap='viridis')

# Función para actualizar la dispersión en cada cuadro de la animación
def update(frame):
    ax.cla()
    new_x = np.random.rand(n)
    new_y = np.random.rand(n)
    new_z = np.random.rand(n)
    new_colors = np.random.rand(n)

    scatter = ax.scatter(new_x, new_y, new_z, c=new_colors, cmap='viridis')
    ax.set_xlabel('Eje X')
    ax.set_ylabel('Eje Y')
    ax.set_zlabel('Eje Z')
    ax.set_title('Gráfico de Dispersión 3D Animado')

# Crea la animación
ani = FuncAnimation(fig, update, frames=range(100), repeat=False)

# Muestra la animación
plt.show()
