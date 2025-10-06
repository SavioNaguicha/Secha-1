# Aplicación GUI para Gestión de Tareas con Atajos de Teclado

#Utilizar Tkinter para crear la interfaz de usuario.
#Implementar un campo de entrada (Entry) para añadir nuevas tareas.
#Incluir botones para añadir tareas, marcar como completadas, y eliminar tareas.
#Mostrar las tareas en una lista o algún componente adecuado.

import tkinter as tk
from functools import total_ordering  # Not used in this snippet
from tkinter import ttk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")
        self.tasks = []

        # Campo de entrada para añadir tareas
        self.task_entry = ttk.Entry(root, width=40)
        self.task_entry.pack(pady=10)
        self.task_entry.bind("<Return>", self.add_task)

        # Botones
        self.add_button = ttk.Button(root, text="Añadir Tarea", command=self.add_task)
        self.add_button.pack()
        self.complete_button = ttk.Button(root, text="Marcar como Completada", command=self.complete_task)
        self.complete_button.pack()
        self.delete_button = ttk.Button(root, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.pack()

        # Lista de tareas
        self.task_listbox = tk.Listbox(root, width=50, height=10)
        self.task_listbox.pack(pady=10)

        # Atajos de teclado
        root.bind("<c>", self.complete_task)
        root.bind("<Delete>", self.delete_task)
        root.bind("<d>", self.delete_task)
        root.bind("<Escape>", self.close_app)

        self.update_listbox()

    def add_task(self, event=None):
        task_text = self.task_entry.get()
        if task_text:
            self.tasks.append({"text": task_text, "completed": False})
            self.task_entry.delete(0, tk.END)
            self.update_listbox()

    def complete_task(self, event=None):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.tasks[selected_task_index]["completed"] = True
            self.update_listbox()
        except IndexError:
            messagebox.showinfo("Selección", "Por favor, selecciona una tarea para marcar como completada.")

    def delete_task(self, event=None):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            del self.tasks[selected_task_index]
            self.update_listbox()
        except IndexError:
            messagebox.showinfo("Selección", "Por favor, selecciona una tarea para eliminar.")

    def update_listbox(self):
        self.task_listbox.delete(0, tk.END)  # Clear current listbox content
        for i, task in enumerate(self.tasks):
            display_text = task["text"]
            if task["completed"]:
                display_text += " (Completada)"
            self.task_listbox.insert(tk.END, display_text)
            if task["completed"]:
                self.task_listbox.itemconfig(i, fg="gray", selectbackground="gray", selectforeground="white")

    def close_app(self, event=None):
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()









