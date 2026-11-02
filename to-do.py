FILENAME = "tasks.txt"

def load_tasks():
    try:
        with open(FILENAME, "r", encoding="utf-8") as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        return []

def save_tasks(task_list):
    with open(FILENAME, "w", encoding="utf-8") as file:
        for item in task_list:
            file.write(item + "\n")

tasks = load_tasks()

while True:
    print("---Menu---")
    print("1. Show tasks")
    print("2. Add a task")
    print("3. Mark task as done")
    print("4. Delete a task")
    print("5. Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        if len(tasks) == 0:
            print("No tasks yet")
        else:
            for number, task in enumerate(tasks, start=1):
                print(f"{number}. {task}")
    elif choice == "2":
        new_task = input("Enter your new task: ")
        tasks.append("[ ] " + new_task)
        save_tasks(tasks)
        print("Task added!")
    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks yet")
        else:
            for number, task in enumerate(tasks, start=1):
                print(f"{number}. {task}")
            mark = input(f"Which task would you like to mark(1 - {len(tasks)}): ")
            if mark.isdigit() and 1 <= int(mark) <= len(tasks):
                position = int(mark) - 1
                if tasks[position].startswith("[x] "):
                    print("Already done")
                else:
                    tasks_marked = tasks[position][4:]
                    tasks[position] = "[x] " + tasks_marked
                    save_tasks(tasks)
                    print(f"Task marked successfully: {tasks_marked}")
            else:
                print("Invalid number")
    elif choice == "4":
        if len(tasks) == 0:
            print("Nothing to delete")
        else:
            for number, task in enumerate(tasks, start=1):
                print(f"{number}. {task}")
            answer = input(f"Which task would you like to delete? (1 - {len(tasks)}): ")
            if answer.isdigit() and 1 <= int(answer) <= len(tasks):
                removed = tasks.pop(int(answer) - 1)
                save_tasks(tasks)
                print(f"Deleted - '{removed}'")
            else:
                print("Invalid number")
    elif choice == "5":
        print("Bye")
        break
    else:
        print("Invalid choice, please try again")

