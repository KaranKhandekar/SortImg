import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Todo List")
        self.root.geometry("400x500")
        
        # List to store todo items
        self.todos = []
        
        # Create main frame
        self.main_frame = ttk.Frame(self.root, padding="10")
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Add Todo button
        self.add_button = ttk.Button(self.main_frame, text="Add Todo", command=self.show_add_dialog)
        self.add_button.pack(pady=10)
        
        # Todo list frame
        self.todo_frame = ttk.Frame(self.main_frame)
        self.todo_frame.pack(fill=tk.BOTH, expand=True)

    def show_add_dialog(self):
        # Create dialog window
        dialog = tk.Toplevel(self.root)
        dialog.title("Add Todo")
        dialog.geometry("300x150")
        dialog.transient(self.root)
        
        # Add entry field
        ttk.Label(dialog, text="Enter todo item:").pack(pady=10)
        entry = ttk.Entry(dialog, width=40)
        entry.pack(pady=10)
        
        def add_todo():
            todo_text = entry.get().strip()
            if todo_text:
                self.add_todo_item(todo_text)
                dialog.destroy()
            else:
                messagebox.showwarning("Warning", "Please enter a todo item")
        
        # Add button
        ttk.Button(dialog, text="Add", command=add_todo).pack(pady=10)

    def add_todo_item(self, text):
        # Create frame for todo item
        item_frame = ttk.Frame(self.todo_frame)
        item_frame.pack(fill=tk.X, pady=2)
        
        # Create variable for checkbox
        var = tk.BooleanVar()
        
        # Create checkbox and label
        cb = ttk.Checkbutton(item_frame, variable=var, command=lambda: self.toggle_todo(label, var))
        cb.pack(side=tk.LEFT)
        
        label = ttk.Label(item_frame, text=text)
        label.pack(side=tk.LEFT)
        
        self.todos.append((item_frame, var, label, text))

    def toggle_todo(self, label, var):
        if var.get():
            label.configure(font=('TkDefaultFont', 9, 'overstrike'))
        else:
            label.configure(font=('TkDefaultFont', 9))

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
