import os

def crear_carpetas():
    # Pedimos el número de carpetas que se desean crear
    num_carpetas = int(input("Ingrese el número de carpetas que desea crear: "))
    
    # Creamos una lista para almacenar los nombres de las carpetas
    nombres_carpetas = []

    # Obtenemos los nombres de las carpetas
    for i in range(num_carpetas):
        nombre = input(f"Ingrese el nombre de la carpeta {i + 1}: ")
        nombres_carpetas.append(nombre)

    # Creamos las carpetas
    for nombre in nombres_carpetas:
        try:
            os.makedirs(nombre)
            print(f"Carpeta '{nombre}' creada exitosamente.")
        except FileExistsError:
            print(f"La carpeta '{nombre}' ya existe.")
        except Exception as e:
            print(f"Ocurrió un error al crear la carpeta '{nombre}': {e}")

# Llamar a la función
if __name__ == "__main__":
    crear_carpetas()
