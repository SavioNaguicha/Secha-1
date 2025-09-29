#Aplicación GUI de Lista de Tareas
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplicación de Lista de Tareas")

        self.tasks = []

        # Campo de entrada para nuevas tareas
        self.task_entry = ttk.Entry(root, width=40)
        self.task_entry.pack(pady=10)

        # Botones
        self.add_button = ttk.Button(root, text="Añadir Tarea", command=self.add_task)
        self.add_button.pack()

        self.complete_button = ttk.Button(root, text="Marcar como Completada", command=self.mark_complete)
        self.complete_button.pack()

        self.delete_button = ttk.Button(root, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.pack()

        # Lista de tareas
        self.task_listbox = tk.Listbox(root, width=50, height=10)
        self.task_listbox.pack(pady=10)

        self.update_listbox()

    def add_task(self):
        task_text = self.task_entry.get()
        if task_text:
            self.tasks.append({"text": task_text, "complete": False})
            self.update_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Por favor, introduce una tarea.")

    def mark_complete(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.tasks[selected_index]["complete"] = True
            self.update_listbox()
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea para marcar como completada.")

    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            del self.tasks[selected_index]
            self.update_listbox()
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea para eliminar.")

    def update_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for i, task in enumerate(self.tasks):
            task_text = task["text"]
            if task["complete"]:
                task_text = "[COMPLETADA] " + task_text
            self.task_listbox.insert(tk.END, task_text)
            if task["complete"]:
                self.task_listbox.itemconfig(i, foreground="gray")
            else:
                self.task_listbox.itemconfig(i, foreground="black")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()

