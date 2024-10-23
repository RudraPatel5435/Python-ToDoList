tasks = {}
ask = 0
num1 = 1


def add():
    global num1
    name = input("Enter task name: ")
    des = input("Enter task Description: ")
    date = input("Enter task due date (YYYY-MM-DD): ")
    tasks[num1] = {
        "name": name,
        "des": des,
        "date": date,
        "status": "Pending"
    }
    num1 += 1
    print("Task added successfully!")


def display():
    if len(tasks) == 0:
        print("No tasks to display!")
    else:
        for i in range(1, len(tasks) + 1):
            print(str(i) + ".",
                  tasks[i]["name"] + " (" + tasks[i]["status"] + ") - Due: " + tasks[i]["date"] + "\nDescription: " +
                  tasks[i]["des"])


def exit():
    print("Exiting program, Bye!")
    repeat = 6


def delete():
    if len(tasks) == 0:
        print("No tasks to delete!")
    else:
        print("Tasks:")
        for i in range(1, len(tasks) + 1):
            print(str(i) + ". " + tasks[i]["name"])
        delNum = int(input("Enter the task number to delete: "))
        for j in range(delNum, len(tasks)):
            tasks[j] = tasks[j + 1]
        del tasks[len(tasks)]
        print("Task deleted successfully!")


def complete():
    if len(tasks) == 0:
        print("No tasks to mark as completed!")
    else:
        print("Tasks:")
        for i in range(1, len(tasks) + 1):
            print(str(i) + ". " + tasks[i]["name"])

        comp = int(input("Enter the task number to mark as completed: "))
        tasks[comp]['status'] = "Completed"
        print("Task marked as completed!")


def edit():
    if len(tasks) == 0:
        print("No tasks to edit!")
    else:
        print("Tasks:")

        for i in range(1, len(tasks) + 1):
            print(str(i) + ". " + tasks[i]["name"])

        editNum = int(input("Enter the task number to edit: "))
        editName = input("Enter new task name (current: " + tasks[editNum]["name"] + "): ")
        editDes = input("Enter new task description (current: " + tasks[editNum]["des"] + "): ")
        editDate = input("Enter new task due date (current: " + tasks[editNum]["date"] + "): ")
        tasks[editNum]["name"] = editName
        tasks[editNum]["des"] = editDes
        tasks[editNum]["date"] = editDate
        print("Task updated successfully!")


while ask != 6:
    print("---------- To-Do List Menu -----------")
    print("1. Add Task")
    print("2. Delete Task")
    print("3. Display Task")
    print("4. Mark Task as Completed")
    print("5. Edit Task")
    print("6. Exit")
    print("-----------------------------------------")
    ask = int(input("Enter your choice: "))

    if ask == 1:
        add()
    elif ask == 2:
        delete()
    elif ask == 3:
        display()
    elif ask == 4:
        complete()
    elif ask == 5:
        edit()
    elif ask == 6:
        exit()
    else:
        print("Enter a valid Choice!")
