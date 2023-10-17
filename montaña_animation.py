
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Crea una figura y un eje 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Define la función que crea la superficie
def create_surface(x, y, t):
    # Puedes personalizar esta función para definir tu superficie en evolución
    return np.sin(np.sqrt(x**2 + y**2) + t)

# Rango de valores para x e y
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)

# Configura la superficie inicial
Z = create_surface(X, Y, 0)
surface = [ax.plot_surface(X, Y, Z, cmap='viridis')]

# Función para actualizar la superficie en cada cuadro de la animación
def update(frame):
    ax.cla()
    Z = create_surface(X, Y, frame)
    surface[0] = ax.plot_surface(X, Y, Z, cmap='viridis')
    ax.set_zlim(-1, 1)  # Ajusta el rango de valores del eje z si es necesario
    ax.set_xlabel('Eje X')
    ax.set_ylabel('Eje Y')
    ax.set_zlabel('Eje Z')
    ax.set_title('Superficie 3D en Evolución (ponganos 10 inge)')

# Crea la animación
ani = FuncAnimation(fig, update, frames=range(100), repeat=False)

fig.colorbar(surface, shrink=1, aspect=5)

# Muestra la animación
plt.show()


