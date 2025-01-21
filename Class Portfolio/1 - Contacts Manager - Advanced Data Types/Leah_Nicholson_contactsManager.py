# Assignment: Contacts Manager
# Class: DEV 128
# Date: January 16th, 2025
# Author: Leah Nicholson
# Description: Program helps users manage contact info. Supports listing all 
# contacts, view/add/delete contact, and print a given field for each contact. 
# Uses dictionary of dictionaries to hold contact info.


#!/usr/bin/env python3


def display_menu():
    '''
    Displays the menu for the user: list, view, add, del, field, exit.
    '''
    print()
    print('COMMAND MENU')
    print('\t list - Display all contacts')
    print('\t view - View a contact')
    print('\t add - Add a contact')
    print('\t del - Delete a contact')
    print('\t field - View field for all contacts')
    print('\t exit - Exit program')
    print()


def list_contacts(contacts):
    '''
    Takes contacts dictionary. 
    Displays first name of all contacts alphabetically with a number.
    '''
    name_list = []

    for name in contacts:      # For each key in contacts, add it to the name_list
        name_list.append(name)

    name_list.sort()                

    if name_list != []:
        counter = 1
        for item in name_list:  # For each name in name_list, print it with a number
            print("\t" + str(counter) + ". " + item)
            counter += 1
    else:
        print("No contacts to show.")


def view_contacts(contacts):
    '''
    Takes contacts dictionary. 
    Allows user to view all fields for a specified contact, case insensitive.
    '''
    selected_name = input("Enter the name: ").title()

    if selected_name in contacts:
        display_item = contacts.get(selected_name)  # get the Value for the Key "selected_name" (a sub-dictionary)

        print("Viewing contact for " + selected_name + ":")

        for key, value in sorted(display_item.items()):     # returns the key/value pairs alphabetically
            print("\t" + key + ": " + value)
    
    else:
        print("No contact found for that name.")


def add_contacts(contacts):
    '''
    Takes contacts dictionary. Allows user to add a new contact to the contacts 
    dictionary of dictionaries.
    '''
    added_name = input("Enter the name for the new contact: ").title()

    if added_name in contacts:
        print(added_name + " is already in the contacts.")  # To not overwrite existing data unknowningly
    
    else:

        sub_dict = {}       # collect new info in a sub-dictionary

        added_address = input("Enter the address for the new contact: ")
        added_mobile = input("Enter the mobile number for the new contact: ")
        added_company = input("Enter the company for the new contact: ")

        sub_dict["address"] = added_address
        sub_dict["mobile"] = added_mobile
        sub_dict["company"] = added_company

        contacts[added_name] = sub_dict     # add that info with the name as Key to the main contacts dictionary


def delete_contacts(contacts):
    '''
    Takes contacts dictionary. Allows user to delete a contact.
    '''
    to_delete = input("Enter the name to delete: ").title()

    if to_delete not in contacts:
        print("No contact found for that name.")
    
    else:
        del contacts[to_delete]
        print("Contact for " + to_delete + " deleted.")


def view_field(contacts):
    '''
    Takes contacts dictionary. 
    Allows user to view the same field for all contacts at once.
    '''
    field = input("Please enter the field you want to view: ").lower()
    status_list = []
    count_no_data = 0   

    # for each name in the dict
    for name in contacts.keys(): 

        info = contacts.get(name)                       # info is the sub-dict
        status = view_field_helper(name, field, info)   # send name, user's field, sub-dict
        
        status_list.append(status)  # add result to a list
        
    for item in status_list:

        if "**No Data**" in item:
            count_no_data += 1

    if count_no_data == len(status_list):   # if **No Data** appears as many times as names
            print("Field not found in any contact.")
    
    else:
        status_list.sort()
        print("Printing " + field + " for all contacts")
        for item in status_list:
            print(item)


def view_field_helper(name, field, info):
    '''
    Takes name, user's field, and info (sub-dict). 
    Checks if field present in info. 
    If no data found for that value, returns **No Data**.
    '''
    if field in info.keys():
        value = info.get(field)
        return (name + "\t" + ": " + value)
    else:
        return (name + "\t" + ": " + "**No Data**")


def main():
    '''
    Defines main program execution.
    '''
    contacts = {
        "Joel":
            {"address": "1500 Anystreet, San Francisco, 94110", "company":"A startup",
             "mobile": "555-555-1111"},
        "Anne":
            {"address": "1000 Somestreet, Fresno, CA 93704",
             "state": "California",
             "landline": "125-555-2222", "company": "Some Great Company"},
        "Sally":
            {"state": "Illinois", "landline":"217-555-1222", "company": "Illinois Technologies",
             "mobile": "217-333-2353"},
        "Ben":
            {"address": "1400 Another Street, Fresno CA 93704",
             "state": "California", "mobile": "125-555-4444"}             
    }

    # welcome user
    print()
    print()
    print("Welcome to contacts manager program")

    # display menu
    display_menu()

    while True:
        
        print()
        command = input("Please enter the command: ")
        command = command.lower()

        if command == 'list':
            list_contacts(contacts)

        elif command == 'view':
            view_contacts(contacts)

        elif command == 'add':
            add_contacts(contacts)

        elif command == 'del':
            delete_contacts(contacts)

        elif command == 'field':
            view_field(contacts)

        elif command == 'exit':
            print("Good bye")
            print()
            break

        else:
            print("Invalid command.")


if (__name__ == "__main__"):
    main()
