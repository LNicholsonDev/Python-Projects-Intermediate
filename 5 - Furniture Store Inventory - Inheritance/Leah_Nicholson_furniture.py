# Assignment: Furniture Inheritance
# Class: DEV 128
# Date: February 17th, 2025
# Author: Leah Nicholson
# Description: Classes designed to handle store inventory data using inheritance.
# Bed and Table objects are derived from Furniture superclass.


#!/usr/bin/env python3


class Furniture:
    '''
    Creates a Furniture item with a weight in pounds.
    '''

    def __init__(self, weight):

        if weight <= 0:
            raise ValueError("Weight must be positive.")
        
        self.__weight = weight      # weight set


    @property
    def weight(self):
        return self.__weight
    
    @weight.setter
    def weight(self, new_weight):

        if new_weight <= 0:
            raise ValueError("Weight must be positive.")
        
        else:
            self.__weight = new_weight

    def __str__(self):
        '''
        Returns string for Furniture object with class name and identifier.
        '''
        return f"Item Weight: {self.weight} lbs"
    
    # Rich Comparison Methods - comparison based on Weight property:

    def __eq__(self, other):         
        return ((self.weight) == (other.weight))

    def __ne__(self, other):         
        return ((self.weight) != (other.weight))

    def __lt__(self, other):         
        return ((self.weight) < (other.weight))

    def __le__(self, other):         
        return ((self.weight) <= (other.weight))

    def __gt__(self, other):         
        return ((self.weight) > (other.weight))

    def __ge__(self, other):         
        return ((self.weight) >= (other.weight))


class Table(Furniture):
    '''
    Creates a Table object derived from Furniture superclass.
    '''

    def __init__(self, weight, wood):
        
        if not isinstance(wood, str):
            raise TypeError("Wood should be of type string")
        
        Furniture.__init__(self, weight)
        self.wood = wood        # public

    def __str__(self):
        '''
        Returns string for Table object with Table name and wood.
        '''
        return f"Table {Furniture.__str__(self)} Made of: {self.wood}"


class Bed(Furniture):
    '''
    Creates a Bed object derived from Furniture superclass.
    '''

    def __init__(self, weight, size):
        
        # Check size value
        allowed_sizes = ['Twin', 'Full', 'Queen', 'King']

        if size not in allowed_sizes:
            raise ValueError("Size not an allowed value.")

        Furniture.__init__(self, weight)
        self.size = size
        
    def __str__(self):
        '''
        Returns string for Bed object with Bed name and weight.
        '''
        return f"Bed {Furniture.__str__(self)} Size: {self.size}"


class FurnitureGallery:

    def __init__(self):
        self.__furnList = []                    # holds furniture items

    def addFurniture(self, FurnItem):           # FurnItem is a potential Furniture (or derived) object
        
        if isinstance(FurnItem, Furniture):     # Base class Furniture used, it covers all derived objects too since they inherit
            self.__furnList.append(FurnItem)   

        else:
            raise TypeError("Item should be an instance of Furniture.")

    # Sort uses Rich Comparison methods in Furniture superclass
    def sort(self):
        self.__furnList.sort()    

    # Python calls this for the For-loop in client code
    # Returns iterator object for the __furnList

    def __iter__(self):
        for item in self.__furnList:
            yield item
