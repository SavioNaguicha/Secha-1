# Creación de una Aplicación de Agenda Personal

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import datetime

class AgendaApp:
    def _init_(self, root):
        self.root = root
        self.root.title("Agenda Personal")

        # Lista de eventos (inicialmente vacía)
        self.eventos = []

        # Configuración del TreeView
        self.tree = ttk.Treeview(root, columns=('Fecha', 'Hora', 'Descripción'), show='headings')
        self.tree.heading('Fecha', text='Fecha')
        self.tree.heading('Hora', text='Hora')
        self.tree.heading('Descripción', text='Descripción')
        self.tree.pack(pady=10)

        # Campos de entrada para nuevos eventos
        self.fecha_label = tk.Label(root, text="Fecha (YYYY-MM-DD):")
        self.fecha_label.pack()
        self.fecha_entry = tk.Entry(root)
        self.fecha_entry.pack()

        self.hora_label = tk.Label(root, text="Hora (HH:MM):")
        self.hora_label.pack()
        self.hora_entry = tk.Entry(root)
        self.hora_entry.pack()

        self.descripcion_label = tk.Label(root, text="Descripción:")
        self.descripcion_label.pack()
        self.descripcion_entry = tk.Entry(root)
        self.descripcion_entry.pack()

        # Botones de acción
        self.agregar_button = tk.Button(root, text="Agregar Evento", command=self.agregar_evento)
        self.agregar_button.pack(pady=5)

        self.eliminar_button = tk.Button(root, text="Eliminar Evento Seleccionado", command=self.eliminar_evento)
        self.eliminar_button.pack(pady=5)

        self.salir_button = tk.Button(root, text="Salir", command=root.quit)
        self.salir_button.pack(pady=5)

        # Cargar eventos iniciales (si los hay)
        self.cargar_eventos()

    def agregar_evento(self):
        fecha = self.fecha_entry.get()
        hora = self.hora_entry.get()
        descripcion = self.descripcion_entry.get()

        try:
            datetime.datetime.strptime(fecha, '%Y-%m-%d')
            datetime.datetime.strptime(hora, '%H:%M')
        except ValueError:
            messagebox.showerror("Error", "Formato de fecha u hora incorrecto. Use YYYY-MM-DD y HH:MM.")
            return

        self.eventos.append((fecha, hora, descripcion))
        self.actualizar_treeview()

        # Limpiar los campos de entrada
        self.fecha_entry.delete(0, tk.END)
        self.hora_entry.delete(0, tk.END)
        self.descripcion_entry.delete(0, tk.END)

    def eliminar_evento(self):
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showinfo("Info", "Por favor, seleccione un evento para eliminar.")
            return

        for item in seleccion:
            index = self.tree.index(item)
            del self.eventos[index]
            self.tree.delete(item)

    def actualizar_treeview(self):
        # Limpiar el TreeView
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Insertar los eventos en el TreeView
        for evento in self.eventos:
            self.tree.insert('', tk.END, values=evento)

    def cargar_eventos(self):
        # Aquí puedes implementar la lógica para cargar eventos desde un archivo o base de datos
        # Por ahora, se agregan algunos eventos de ejemplo
        self.eventos = [
            ('2024-07-15', '10:00', 'Reunión con el equipo'),
            ('2024-07-16', '14:30', 'Presentación del proyecto'),
            ('2024-07-17', '09:00', 'Entrevista con el cliente')
        ]
        self.actualizar_treeview()

if _name_ == "_main_":
    root = tk.Tk()
    app = AgendaApp(root)
    root.main
loop()
    print("eliminar eventos")


