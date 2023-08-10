from collections import deque

class Task:    
    def __init__(self, name, has_priority=False):
        self.name = name
        self.has_priority = has_priority

tasks = deque()

def add_task(task):
    if task.has_priority:
        tasks.appendleft(task)
    else:
        tasks.append(task)

def print_tasks():
    for t in tasks:
        print(t.name)

def main():
    #add code here
    add_task(Task("new"))
    add_task(Task("high priority", True))
    add_task(Task("low priority"))
    add_task(Task("highest priority", True))
    print_tasks()
    return

if __name__ == "__main__":
    main()