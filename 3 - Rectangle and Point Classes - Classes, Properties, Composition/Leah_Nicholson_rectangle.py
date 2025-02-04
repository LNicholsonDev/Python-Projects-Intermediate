# Assignment: Rectangle and Point Classes
# Class: DEV 128
# Date: January 29th, 2025
# Author: Leah Nicholson
# Description: Two classes which represent a point and a rectangle 
# in a 2-dimensional coordinate space designed to run with provided client code.


#!/usr/bin/env python3


class Point:
    '''
    Defines the point object with x- and y-coordinates.
    '''
    # Takes required attributes and makes them private
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    # Getter method for x (read-only)
    @property
    def x(self):
        return self.__x

    # Getter method for y (read-only)
    @property
    def y(self):
        return self.__y

    # Required method
    def translate(self, dx, dy):
        '''
        Moves the point by dx in x-direction,
        and moves by dy in y-direction.
        '''
        self.__x += dx
        self.__y += dy


class Rectangle: 
    '''
    Defines the rectangle.
    '''
    # Static attributes defined for all instances of Rectangle
    DEFAULT_WIDTH = 1
    DEFAULT_HEIGHT = 1
    rectangleCount = 0  # count of Rectangles instantiated so far

    def __init__(self, topLeft, width, height):
        '''
        topLeft is an instance of Point class (top left corner of rectangle).
        width and height of Rectangle cannot be negative or zero. 
        '''
        self.__topLeft = topLeft        # topLeft is a point object
        self.width = width              # refers to the width setter (its without __)
        self.height = height            # refers to the height setter (its without __)

        Rectangle.rectangleCount += 1

    # Define getters for Rectangle class
    @property
    def topLeft(self):
        return self.__topLeft

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    # Define setters for Rectangle class
    @topLeft.setter
    def topLeft(self, new_topLeft):
        '''
        Updates the topLeft attribute.
        '''
        self.__topLeft = new_topLeft

    @width.setter
    def width(self, new_width):
        '''
        Checks client code for invalid width values.
        If valid, updates self.__width attribute.
        '''
        if (new_width <= 0):
            print("Width cannot be negative or zero. Setting it to the default value of 1")
            new_width = Rectangle.DEFAULT_WIDTH     # utilizing the static attribute
            self.__width = new_width # setting width to this static attribute
        else:
            self.__width = new_width

    @height.setter
    def height(self, new_height):
        '''
        Checks client code for invalid height values.
        If valid, updates self.__height attribute.
        '''
        if (new_height <= 0):
            print("Height cannot be negative or zero. Setting it to default value of 1")
            new_height = Rectangle.DEFAULT_HEIGHT   # utilizing the static attribute
            self.__height = new_height  # setting height to this static attribute
        else: 
            self.__height = new_height

    # bottomRight, area, and permimeter are derived from the object
    # therefore, since the states of object are unchanged,
    # can use @property 
    @property
    def bottomRight(self):
        point_width = self.topLeft.x + self.width
        point_height = self.topLeft.y + self.height
        return Point(point_width, point_height) # Returns a Point object

    @property
    def area(self):
        return (self.width * self.height)

    @property
    def perimeter(self):
        return ((self.width * 2) + (self.height * 2))

    # any method (like translate) in Point is accessible on topLeft
    # because topLeft is a Point object -this updates the object's state
    # rather than returning a value:
    def translate(self, dx, dy):
        self.topLeft.translate(dx, dy)  
