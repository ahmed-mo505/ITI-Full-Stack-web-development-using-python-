import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do App")

        self.tasks = []

        self.task_entry = tk.Entry(root, width=50)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        self.add_task_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_task_button.grid(row=0, column=1, padx=10, pady=10)

        self.incomplete_tasks_listbox = tk.Listbox(root, width=50, height=10, selectmode=tk.SINGLE)
        self.incomplete_tasks_listbox.grid(row=1, column=0, padx=10, pady=10)

        self.complete_task_button = tk.Button(root, text="Mark as Completed", command=self.mark_task_completed)
        self.complete_task_button.grid(row=1, column=1, padx=10, pady=10)

        self.all_tasks_listbox = tk.Listbox(root, width=50, height=10)
        self.all_tasks_listbox.grid(row=2, column=0, padx=10, pady=10)

        self.view_all_tasks_button = tk.Button(root, text="View All Tasks", command=self.view_all_tasks)
        self.view_all_tasks_button.grid(row=2, column=1, padx=10, pady=10)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append({'task': task, 'completed': False})
            self.task_entry.delete(0, tk.END)
            self.update_incomplete_tasks_listbox()
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def update_incomplete_tasks_listbox(self):
        self.incomplete_tasks_listbox.delete(0, tk.END)
        for i, task in enumerate(self.tasks):
            if not task['completed']:
                self.incomplete_tasks_listbox.insert(tk.END, f"{i + 1}. {task['task']}")

    def mark_task_completed(self):
        selected_task_index = self.incomplete_tasks_listbox.curselection()
        if selected_task_index:
            task_index = selected_task_index[0]
            incomplete_task_indices = [i for i, task in enumerate(self.tasks) if not task['completed']]
            actual_task_index = incomplete_task_indices[task_index]
            self.tasks[actual_task_index]['completed'] = True
            self.update_incomplete_tasks_listbox()
        else:
            messagebox.showwarning("Warning", "You must select a task to mark as completed.")

    def view_all_tasks(self):
        self.all_tasks_listbox.delete(0, tk.END)
        for i, task in enumerate(self.tasks):
            status = 'Completed' if task['completed'] else 'Incomplete'
            self.all_tasks_listbox.insert(tk.END, f"{i + 1}. {task['task']} - {status}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
