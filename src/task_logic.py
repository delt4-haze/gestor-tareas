class Task:
    def __init__(self, title, description, status="Pendiente"):
        self.title = title
        self.description = description
        self.status = status

    def __str__(self):
        return f"[{self.status}] {self.title}: {self.description}"

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description):
        new_task = Task(title, description)
        self.tasks.append(new_task)
        print(f"Tarea '{title}' agregada correctamente.")

    # ¡ESTA ES LA PARTE QUE DEBE ESTAR!
    def get_all_tasks(self):
        return self.tasks

