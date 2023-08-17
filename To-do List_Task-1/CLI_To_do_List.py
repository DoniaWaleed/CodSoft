
def addTask(List, task):
    List.append(str(task))
    print("Task added Successfully")


def editTask(List, TaskNumber, edited):
    List[TaskNumber-1] = str(edited)
    print("Task edited Successfully")


def deleteTask(List, TaskNumber):
    NewList = []
    Num_of_Tasks = int(len(List))
    for i in range(Num_of_Tasks):
        if i + 1 == TaskNumber:
            continue
        else:
            NewList.append(List[i])

    print("Task deleted Successfully")
    return NewList


def showList(List):
    Num_of_Tasks = int(len(List))
    if Num_of_Tasks == 0:
        print("Your List Is Empty")
    else:
        for i in range(Num_of_Tasks):
            print(i+1, ') ', List[i])


if __name__ == '__main__':
    MyList = []
    choice = None
    while choice != 0:
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("To-do List:\n1) Add Task\n2) Edit Task\n3) Delete Task\n4) Show My List\n0) Exit")

        choice = int(input("\nEnter Choice Please: "))
        if choice not in range(0, 5):
            print("Enter Correct Number Please!!")
        elif choice == 1:
            newTask = str(input("Enter the new task please: "))
            addTask(MyList, newTask)
        elif choice == 2:
            Num_of_Tasks = int(len(MyList))
            if Num_of_Tasks == 0:
                print("Your List Is Empty")
            else:
                taskNumber = int(input("Enter the task's number you want to edit please: "))
                editedTask = str(input("Enter the edited task please: "))
                editTask(MyList, taskNumber, editedTask)
        elif choice == 3:
            Num_of_Tasks = int(len(MyList))
            if Num_of_Tasks == 0:
                print("Your List Is Empty")
            else:
                taskNumber = int(input("Enter the task's number you want to delete please: "))
                MyList = deleteTask(MyList, taskNumber)
        elif choice == 4:
            showList(MyList)
