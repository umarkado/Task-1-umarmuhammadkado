
# DECODELABS INTERNSHIP
# PROJECT 1: TO-DO -LIST
# Umar-M-Kado's Project'

my_tasks = []

while True:

    print("\n================================")
    print("       MY TO-DO LIST APP")
    print("================================")
    print("1. Add a New Task")
    print("2. View All Tasks")
    print("3. Delete a Task")
    print("4. Exit")
    print("================================")

    choice = input("Choose an option (1-4): ")

    # ADD TASK
    if choice == "1":

        task = input("Enter your task: ").strip()

        if task:
            my_tasks.append(task)
            print("\nTask added successfully!")

        else:
            print("\nYou cannot add an empty task.")

    # VIEW TASKS
    elif choice == "2":

        print("\n========== YOUR TASKS ==========")

        if not my_tasks:
            print("You have no tasks yet.")

        else:
            for number, task in enumerate(my_tasks, start=1):
                print(f"{number}. {task}")

    # DELETE TASK
    elif choice == "3":

        if not my_tasks:
            print("\nThere are no tasks to delete.")

        else:
            print("\n========== YOUR TASKS ==========")

            for number, task in enumerate(my_tasks, start=1):
                print(f"{number}. {task}")

            try:
                task_number = int(input("Enter task number to delete: "))

                if 1 <= task_number <= len(my_tasks):

                    deleted_task = my_tasks.pop(task_number - 1)

                    print(f"\nDeleted successfully: {deleted_task}")

                else:
                    print("\nInvalid task number.")

            except ValueError:
                print("\nPlease enter a valid number.")

    # EXIT
    elif choice == "4":

        print("\nThank you for using My To-Do List!")
        print("Goodbye!")
        break

    else:
        print("\nInvalid option. Please choose 1-4.")