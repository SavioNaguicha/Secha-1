# Sistema de Gestión de Inventario Mejorado

# Inventario de Productos Lacteos de la Pauterizadora Quito

#Este código ilustra cómo se pueden leer varios archivos de texto y añadir información a uno de ellos, lo que resulta
#bastante útil para manejar listas, inventarios o archivos de texto.


archivo = open("Leches.txt","r") # el codigo abre el archivo en modo lectura
print(archivo.read()) # cierra el archivo
archivo.close() # Esto permite mostrar en la pantalla el contenido del archivo
#
archivo = open("Quesos.txt","r") # el codigo abre el archivo en modo lectura
print(archivo.read()) # cierra el archivo
archivo.close() # Esto permite mostrar en la pantalla el contenido del archivo
#
archivo = open("Avena.txt","r") # el codigo abre el archivo en modo lectura
print(archivo.read()) # cierra el archivo
archivo.close() # Esto permite mostrar en la pantalla el contenido del archivo
#
archivo = open("Mantequilla.txt","r")# el codigo abre el archivo en modo lectura
print(archivo.read()) # cierra el archivo
archivo.close() # Esto permite mostrar en la pantalla el contenido del archivo
#
archivo = open("Yogur.txt","r") # el codigo abre el archivo en modo lectura
print(archivo.read())  # cierra el archivo
archivo.close() # Esto permite mostrar en la pantalla el contenido del archivo
#
archivo = open("Otros productos.txt","a") # permite agregar contenido sin borrar lo que ya existe
archivo.write("\nvita crema de leche.") # cierra el archivo y añade un nuevo producto a la lista de otros productos sin modificarlas.
archivo.close()

























































