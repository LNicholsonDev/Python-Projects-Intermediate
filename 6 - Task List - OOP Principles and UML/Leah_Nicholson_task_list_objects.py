# Assignment: Design and Implement Business Tier Classes
# Class: DEV 128
# Date: February 28th, 2025
# Author: Leah Nicholson
# Description: Classes designed to support operations in a provided UI design.
# Supports a program that stores one or more task lists.


#!/usr/bin/env python3


class Task: 
    '''Defines the operation for a SINGLE Task.'''

    def __init__(self, task_description):

        if not task_description:                     # Same as: if task_desc == '' 
            raise ValueError("Task description cannot be empty.")
        
        self.task_description = task_description
        self.task_status = False                     # intialize to incomplete task status


    def change_status_to_complete(self):
        self.task_status = True


    def change_status_to_incomplete(self):
        self.task_status = False
    

    def edit_task(self, new_description):

        if not new_description:                    
            raise ValueError("Task description cannot be empty.")
        
        self.task_description = new_description


    def __str__(self):
        
        if self.task_status == True:
            status = "(DONE!)"
        else:
            status = ""
    
        return (f'{self.task_description} {status}')        # The formatted string for printing a Task


class TaskList:
    '''Creates a TaskList (a COLLECION of Task objects).'''

    def __init__(self, tasklist_name):          
        self.tasklist_name = tasklist_name       
        self.tasks = []


    def add_task(self, task_desc):

        if not task_desc:                
            raise ValueError("Task description cannot be empty.")

        task_instance = Task(task_desc)
        self.tasks.append(task_instance)


    def delete_task(self, deleted_task_number):

        if 0 <= deleted_task_number < len(self.tasks):
            del self.tasks[deleted_task_number]

        else:
            raise IndexError("Invalid task number.")


    def list_tasks(self):
        return self.tasks


def main():


    # Create test TaskLists
    print()
    print()
    tasklist1 = TaskList("Personal")    
    tasklist2 = TaskList("Work")

    # Add Task objects
    tasklist1.add_task("Pet cat")
    tasklist1.add_task("Brush cat")
    tasklist1.add_task("Feed cat")

    # Display the created "Personal" TaskList
    print("**DISPLAY 1: CREATE/ADD tasks in Personal**")
    counter = 1
    for task in tasklist1.list_tasks():     # task is an instance of Task
        print(f'{counter}. {task}')         # SPECIAL note: counter can be removed if part of Presentation Tier instead
        counter += 1                        # Was unsure if Business Tier responsible for it
    print()


    # Mark a Task as complete 
    tasklist1.list_tasks()[1].change_status_to_complete()       # index of 1 for item 2 in the list

    # Display list again to see completed task
    print("**DISPLAY 2: COMPLETE tasks: ")
    counter = 1
    for task in tasklist1.list_tasks():     
        print(f'{counter}. {task}')         
        counter += 1                        
    print()


    # Attempt to set an empty description -- this should fail
    print("**DISPLAY 3: EDIT first Task to an empty description:**")
    try: 
        tasklist1.list_tasks()[0].edit_task("")   # edit_task takes new description

    except ValueError as e:
        print("ValueError occurred: ", e)


    # Delete a task
    tasklist1.delete_task(0)                # delete_task takes index of deleted task
    print()

    # Display tasks again to ensure item deleted
    print("**DISPLAY 4: DELETION of first task (index of 0):**")
    counter = 1
    for task in tasklist1.list_tasks():     
        print(f'{counter}. {task}')         
        counter += 1                        
    print()


    # Edit existing task
    tasklist1.list_tasks()[0].edit_task("Water cat")

    # Display tasks again to check edit:
    print("**DISPLAY 5: EDIT existing task (with non-empty string):**")
    counter = 1
    for task in tasklist1.list_tasks():     
        print(f'{counter}. {task}')         
        counter += 1                        
    print()


    # Mark a completed task as incomplete:
    tasklist1.list_tasks()[0].change_status_to_incomplete()


    # Display tasks again to check updated status:
    print("**DISPLAY 6: INCOMPLETE an item:**")
    counter = 1
    for task in tasklist1.list_tasks():     
        print(f'{counter}. {task}')         
        counter += 1                        
    print()


if __name__ == '__main__':
    main()
