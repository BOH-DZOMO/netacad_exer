def task_display(tasks):
    for x,y in enumerate(tasks):
            if y.priority == "urgent":
               print(f"{x+1}: [{y.priority}] (due: {y.due_date}) {y.title}") 
               continue
            print(f"{x+1}: [{y.priority}] {y.title}")

class Task():
    def __init__(self,title: str,priority: str="normal",done: bool=False):
        self.title = title
        self.priority = priority
        self.done = done

    def mark_done(self):
        self.done = True

    @classmethod
    def from_string(cls,text: str) -> "Task":
        text = text.split("|")
        if len(text) == 2:
            return cls(text[0],text[1])
        elif len(text) == 3:
            return cls(text[0],text[1],text[2])
        else:
            raise NotImplementedError("More than 3 arguments used")

    @staticmethod
    def is_valid_priority(p: str) -> bool:
        if p not in ["title","normal","urgent"]:
            return False
        return True

class UrgentTask(Task):
    def __init__(self, title: str, due_date: str, priority: str ="urgent", done: bool=False, ):
        super().__init__(title, priority, done)
        self.due_date = due_date

    @classmethod
    def from_string(cls, text: str) -> "Task":
        text = text.split("|")
        if len(text) == 2:
            return cls(text[0],text[1])
        elif len(text) == 3:
            return cls(text[0],text[1],text[2])
        elif len(text) == 4:
            return cls(text[0],text[1],text[2],text[3])
        else:
            raise NotImplementedError("More than 4 arguments used")

class TaskManager(Task):
    def __init__(self):
        self.tasks = list()
        self.total = 0

    def add(self,task: object):
        self.tasks.append(task)
        self.total+=1
        
    def remove(self, id: int):
        self.tasks.pop(id-1)

    def list_all(self):
        task_display(self.tasks)

    def filter_by_priority(self,):
        priority_order = {
            "urgent": 1,
            "normal": 2,
            "low": 3
        }
        sorted_task = sorted(self.tasks, key=lambda x: priority_order.get(x.priority))
        task_display(sorted_task)
# 1: use inheritamce and try to build all in the task manager passing through the init
# 2: use composition and add the task in initb and store staight if its first possible


task1 = Task("clean my room")

task2 = UrgentTask("clean the car","07-05-2026")

manager1 = TaskManager()
manager1.add(Task("clean my room"))
manager1.add(UrgentTask("clean the car","07-05-2026"))
manager1.add(UrgentTask.from_string("clean the cooker|06-05-2026"))
# manager1.remove(0)
manager1.filter_by_priority()

