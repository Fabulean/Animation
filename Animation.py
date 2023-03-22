import matplotlib.pyplot as plt
import matplotlib.animation as animation
import os
import time
start_time = time.time()


# Directorio que contiene las imágenes
img_dir = './Graphics/'

# Obtener lista de nombres de archivo (.png) de las imágenes ordenadas
img_files = sorted([f for f in os.listdir(img_dir) if f.endswith('.png')])

# Crear una función para mostrar cada imagen en la animación
def animate(i):
    img_path = os.path.join(img_dir, img_files[i]) # Une el directorio y el nombre de las imagenes
    img = plt.imread(img_path) # Lee la imagen a partir de la ruta y la guarda en img
    plt.imshow(img) # Muestra la imagen
    print("Progreso: ", 100*i/len(img_files), "%")

# Crear la animación
# Según lo que he entendido yo primero esta fución llama a la función animate la cual muestra la imagen. 
# la llama una vez por frame cambiando el valor de i (dentro de animate).
# Luego el primer argumento (gcf=get current figure) pilla la imagen que esta siendo mostrada para la animación.
# La tercera opción es el número de frames que es el número de imagenes y la cuarta el tiempo entre imágenes en milisegundos.

anim = animation.FuncAnimation(plt.gcf(), animate, frames=len(img_files))

# Guardar la animación como un archivo GIF
anim.save('./Animation/animation.gif', fps=5)

print(time.time() - start_time)