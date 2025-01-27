# Assignment: Dog class and its client code
# Class: DEV 128
# Date: January 24th, 2025
# Author: Leah Nicholson
# Description: A dog Class which allows user to interact with a dog.


#!/usr/bin/env python3


class Dog:
    '''
    A dog class to represent a pet dog.
    '''

    def __init__(self, name, color, weight = 10):
        '''
        Initialize a new dog instance. 
        Takes two required arguments (name and color), 
        and one optional argument (weight in kg).
        '''
        self.name = name
        self.color = color
        self.weight = weight

        self.isHungry = True

        # Initial greeting
        print()
        print()
        print(self.name, " welcomes you! Woof woof!")

    def bark(self):
        '''Initial greeting. 
        Takes no parameters. 
        Prints a string of the form "name: Woof Woof."
        '''
        print()
        print(self.name + ": Woof woof")

    def eat(self):
        '''
        Takes no parameters.
        Sets dog isHungry to False.
        Adds 100 gms (0.1 kg) weight to dog.
        '''
        self.isHungry = False
        self.weight += 0.10
        print(self.name, ": Chomp Chomp")

    def walk(self):
        '''
        Takes no parameters.
        Checks if dog is hungry.
        If hungry - calls bark() method.
        If not hungry - takes dog for walk and decreases weight.
        '''
        if self.isHungry:
            self.bark()         # not my_dog.bark() - use self inside classes to keep generic template structure
        else:
            self.weight -= 0.1
            self.isHungry = True
            print(self.name, ": Step Step")

    def printStatus(self):
        '''
        Takes no parameters. Prints string with status.
        '''
        if self.isHungry:
            print(self.name, "is", self.color, "in color, weighs", 
                  round(self.weight, 1), "kgs, and is hungry.")

        else:
            print(self.name, "is", self.color, "in color, weighs", 
                  round(self.weight, 1), "kgs, and is not hungry.")


def main():
    '''
    Provides main program functionality.
    '''
    my_dog = Dog("Willie", "Brown", 15)     # Create object from class
    
    while True:

        print("-" * 40)
        command = input("Enter the command \n"
                        "'S' to get Status enquiry, \t 'F' to feed the dog, \n"
                        "'W' to take it for a walk, \t 'Q' to exit: \n").lower()
        
        if command == 's':
            my_dog.printStatus()

        elif command == 'w':
            my_dog.walk()

        elif command == 'f':
            my_dog.eat()

        elif command == 'q':
            print("Good bye! Woof woof")
            print()
            break

        else:
            print("Invalid command.")


if (__name__ == "__main__"):
    main()
