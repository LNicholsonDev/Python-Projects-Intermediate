# Import the Task and TaskList classes
from Leah_Nicholson_task_list_objects import Task, TaskList

def main():
    # Create a TaskList
    task_list = TaskList()

    # Add tasks
    task_list.add_task("Call editor")
    task_list.add_task("Edit chapter 1")
    task_list.add_task("Edit chapter 2")

    # Display tasks
    print("Initial Task List:")
    print(task_list.list_tasks())

    # Mark a task as complete
    task_list.complete_task(2)  # Mark "Edit chapter 1" as DONE
    print("\nAfter Completing Task 2:")
    print(task_list.list_tasks())

    # Edit a task description
    task_list.edit_task(3, "Brainstorm chapter 3")  # Change task 3 description
    print("\nAfter Editing Task 3:")
    print(task_list.list_tasks())

    # Delete a task
    task_list.delete_task(1)  # Remove "Call editor"
    print("\nAfter Deleting Task 1:")
    print(task_list.list_tasks())

if __name__ == "__main__":
    main()