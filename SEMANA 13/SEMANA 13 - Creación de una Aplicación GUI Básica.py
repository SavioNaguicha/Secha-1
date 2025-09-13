# aplicación de interfaz gráfica de usuario (GUI)

# Este código permite crear una ventana y agregarle una lista de datos. También se puede eliminar información de la lista, acceder a los datos
# que se han eliminado, insertar nuevos datos y modificar el color de la ventana.

# Mis datos

import tkinter as tk # Accedemos a la bibliotega de tkinter

ventana = tk.Tk()
ventana.title("Mis Datos")
ventana.geometry("400x500") # Establecer el tamaño de la ventana antes del mainloop

#Etiqueta de bienvenida
etiqueta = tk.Label(ventana, text="¡Bienvenido  Savio Naguicha!", font=("Arial", 20))
etiqueta.pack(pady=20)

# Lista (Listbox) - Usamos pack para ser consistentes en este contenedor
lista_datos = tk.Listbox(ventana, width=40, height=10)
lista_datos.pack(padx=10, pady=10)
lista_datos.insert(tk.END, "Dato 1")
lista_datos.insert(tk.END, "Dato 2")
lista_datos.insert(tk.END, "Dato 3")
lista_datos.insert(tk.END, "Dato 4")
lista_datos.insert(tk.END, "Dato 5")
lista_datos.insert(tk.END, "Dato 6")

lista_datos.delete(0, tk.END) # Eliminar todos los datos de la lista
lista_datos.delete(3, tk.END) # Accedemos a los datos eliminados de la lista

#Insertar los datos eliminados de la lista
lista_datos.insert(tk.END, " Dato 1")
lista_datos.insert(tk.END, " Dato 2")
lista_datos.insert(tk.END, " Dato 3")

ventana.color = "yellow" # Cambiamos el color de la ventana
ventana.config(bg=ventana.color)

#Iniciar el bucle principal una sola vez y al final
ventana.mainloop()
















