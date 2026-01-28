# Define el nombre del archivo
nombre_archivo = "enlace_github.txt"

# Define el contenido del archivo (el enlace de GitHub)
contenido_archivo = "https://github.com/alfachris090-blip/evaluaci-n-final-de-programaci-n-web"  # Reemplaza con tu enlace real

# Abre el archivo en modo escritura ("w")
with open(nombre_archivo, "w") as archivo:
    # Escribe el contenido en el archivo
    archivo.write(contenido_archivo)

# Imprime un mensaje de confirmación
print(f"Se ha creado el archivo '{nombre_archivo}' con el enlace de GitHub.")