import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Datos de ejemplo
x = np.arange(20)
y = np.arange(20)
z = np.zeros(20)

# Configura la figura y el eje 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Función para actualizar el gráfico en cada cuadro de la animación
def update(frame):
    ax.cla()
    z = np.random.rand(20)  # Actualiza los datos de manera aleatoria
    ax.bar(x, y, z, zdir='y', color='b', alpha=0.7)
    ax.set_xlabel('Eje X')
    ax.set_ylabel('Eje Y')
    ax.set_zlabel('Eje Z')
    ax.set_title('Gráfico de Barras 3D Animado')

# Crea la animación
ani = FuncAnimation(fig, update, frames=100, repeat=False)

# Muestra el gráfico animado
plt.show()
