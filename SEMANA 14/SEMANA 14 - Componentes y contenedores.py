# Creación de una Aplicación de Agenda Personal

import tkinter as tk
from tkinter import ttk, messagebox
import datetime


ventana = tk.Tk()
ventana.title("Agenda Personal")
ventana.geometry("800x600")

etiqueta = tk.Label(ventana, text="Agenda Personal", font=("Arial 11", 20))
etiqueta.pack(pady=20)


class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")

        # Lista de eventos (inicialmente vacía)
        self.eventos = []

        # Configuración del TreeView
        self.tree = ttk.Treeview(root, columns=('Fecha', 'Hora', 'Descripción'), show='headings')
        self.tree.heading('Fecha', text='Fecha')
        self.tree.heading('Hora', text='Hora')
        self.tree.heading('Descripción', text='Descripción')
        self.tree.pack(pady=10, fill="both", expand=True)

        # Cargar nuevos eventos
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
        fecha = self.fecha_entry.get().strip()
        hora = self.hora_entry.get().strip()
        descripcion = self.descripcion_entry.get().strip()

        if not (fecha and hora and descripcion):
            messagebox.showwarning("Datos incompletos", "Complete todos los campos antes de agregar.")
            return

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

        # Eliminar desde el final para no desfasar índices
        indices = sorted((self.tree.index(item) for item in seleccion), reverse=True)
        for idx in indices:
            del self.eventos[idx]

        for item in seleccion:
            self.tree.delete(item)

    def actualizar_treeview(self):
        # Limpiar el TreeView
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Insertar los eventos
        for evento in self.eventos:
            self.tree.insert('', tk.END, values=evento)

    def cargar_eventos(self):
        # Eventos
        self.eventos = [
            ('15-09-2025', '10:00', 'Reunión con el equipo'),
            ('16-09-2025', '14:30', 'Presentación del proyecto'),
            ('17-09-2025', '09:00', 'Entrevista con el cliente'),
            ('18-09-2025', '07:30', 'Clases en la Universidad'),
            ('19-09-2025', '13:30', 'Examenes finales Fisica')


        ]
        self.actualizar_treeview()

        # Limpiar los campos por si tuvieran datos
        self.fecha_entry.delete(0, tk.END)
        self.hora_entry.delete(0, tk.END)
        self.descripcion_entry.delete(0, tk.END)

ventana.color = "green"
ventana.config(bg=ventana.color)



# Instanciar la aplicación y lanzar el bucle principal
app = AgendaApp(ventana)
ventana.mainloop()

































