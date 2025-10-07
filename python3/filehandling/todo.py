"""
To-do List App
- create a file name todo.txt
 tasks:
 view tasks
 add tasks
 remove tasks
 exit tasks 
"""

def addTask(task):
    with open("todo.txt", 'a') as file:
        file.writelines(f"{str(task).strip()}\n")
    print(f"task: {task} added!")
    return


def viewTasks():
    with open("todo.txt", 'r') as file:
        task = file.readlines
        print("-" * 10)
        for index, task in enumerate(tasks, start=1):
            print(f"{index} . {task.strip()}")
        print("-" * 10)


def removeTask(task_number):
    with open("todo.txt", 'r') as file:
        tasks = file.readlines()

    with open("todo.txt", 'w') as file:
        if task_number < 1 or task_number > len(tasks):
            if len(tasks) == 0:
                print("No tasks!")
                return
        print("Invalid task number!")
        return
    
    
    removed = tasks[task_number - 1]
    tasks.pop(task_number - 1)
    with open("todo.txt", 'w') as file:
        file.writelines(tasks)
        print(f"{removed} removed!")
     

def exit():
    print("exiting....")
    exit(0)

def main():
    ## task inputs, logic check, etc
    while True:
        opt = input("Choose an option - add, view, remove, exit: ")
        if opt == "add":
            task = input("Enter a task: ")
            addTask(task)
        elif opt == "view":
            viewTasks()
        elif opt == "remove":
            task_number = int(input("Enter task number to remove: "))
            removeTask(task_number)
        elif opt == "exit":
            exit()
        else:
            print("Invalid option! Please try again.")

if __name__ == "__main__":
    main()