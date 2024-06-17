class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        return task

    def view_tasks(self):
        return self.tasks

    def delete_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            return task
        return None

if __name__ == "__main__":
    todo_list = TodoList()
    while True:
        print("\nTodo List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
            print(f"Task '{task}' added.")
        elif choice == '2':
            tasks = todo_list.view_tasks()
            print("Tasks:")
            for idx, task in enumerate(tasks, start=1):
                print(f"{idx}. {task}")
        elif choice == '3':
            task = input("Enter the task to delete: ")
            deleted_task = todo_list.delete_task(task)
            if deleted_task:
                print(f"Task '{task}' deleted.")
            else:
                print(f"Task '{task}' not found.")
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

