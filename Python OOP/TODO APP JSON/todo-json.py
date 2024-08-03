import json
import os

class ToDoApp:
    def __init__(self, filename='tasks.json'):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as file:
                    data = file.read()
                    if data:
                        return json.loads(data)
            except json.JSONDecodeError:
                print("Error decoding JSON file. Starting with an empty task list.")
        return []

    def save_tasks(self):
        with open(self.filename, 'w') as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self, task):
        self.tasks.append({'task': task, 'completed': False})
        self.save_tasks()

    def view_incomplete_tasks(self):
        for i, task in enumerate(self.tasks):
            if not task['completed']:
                print(f"{i + 1}. {task['task']}")

    def mark_task_completed(self, task_number):
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1]['completed'] = True
            self.save_tasks()
        else:
            print("Invalid task number")

    def view_all_tasks(self):
        for i, task in enumerate(self.tasks):
            status = 'Completed' if task['completed'] else 'Incomplete'
            print(f"{i + 1}. {task['task']} - {status}")

    def run(self):
        while True:
            print("\nTo-Do App")
            print("1. Add a new task")
            print("2. View incomplete tasks")
            print("3. Mark a task as completed")
            print("4. View all tasks")
            print("5. Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                task = input("Enter the task: ")
                self.add_task(task)
                print("Task added.")
            elif choice == '2':
                print("Incomplete Tasks:")
                self.view_incomplete_tasks()
            elif choice == '3':
                task_number = int(input("Enter the task number to mark as completed: "))
                self.mark_task_completed(task_number)
                print("Task marked as completed.")
            elif choice == '4':
                print("All Tasks:")
                self.view_all_tasks()
            elif choice == '5':
                print("Exiting the app. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    app = ToDoApp()
    app.run()
