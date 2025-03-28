# Assignment: GUI Application Assignment
# Class: DEV 128
# Date: March 17th, 2025
# Author: Leah Nicholson
# Description: Creation of Presentation Layer for a speeding fine calculator with a GUI.

# SPECIAL NOTES: The instructions state "Assume user will enter valid numbers in the text entry boxes. 
# No need for input validation and error checking." 
# However, there is discussion of error checking # in calculateFine method. 
# Therefore, I included error checking to be safe.


#!/usr/bin/env python3


import tkinter as tk                                # Tkinter library (GUI toolkit)
from tkinter import ttk                             # Imports themed widgets
from tkinter import messagebox                      # Adds functionality for popups
from speedingfine import SpeedingFineCalculator     # Imports business logic from speedingfine.py


class SpeedingFineFrame(ttk.Frame):
    '''
    Creates the main frame for the GUI.
    '''

    def __init__(self, parent):

        # Initializes the base Frame with padding
        ttk.Frame.__init__(self, parent, padding = "10 10 10 10")      # Calls the superclass (ttk.Frame) constructor

        # Instantiate the business class object:
        self.speedingFineCalculator = SpeedingFineCalculator()       

        # Save reference to parent window so we can call destroy on it later
        self.parent = parent
        
        # Define GUI variables to be used with text entry fields
        self.speedLimit = tk.DoubleVar()        # Holds speed limit input
        self.clockedSpeed = tk.DoubleVar()      # Holds clocked speed limit input
        self.speedingFine = tk.DoubleVar()      # Holds calculated fine
       
        self.initComponents()                   # Calls initComponents() method to initialize the GUI components


    def initComponents(self):
        '''
        Initializes the GUI components.
        Calls initMainFrame and initButtonsFrame to add the GUI components and set them up.
        '''
        self.pack()                             # Packs the frame into the parent window
        self.initMainFrame()                    # Calls initMainFrame() to initialize the main content frame
        self.initButtonsFrame()                 # Calls initButtonsFrame() to initialize the buttons frame


    def initMainFrame(self):
        
        # Add implementation:
        # Create a new Frame object and use grid method to add it to the parent frame (self).
        # Create and place the 6 labels and 3 text entry boxes.
        # Connect the DoubleVar attributes declared in the constructor to the text entry boxes.
        
        # Frame Object 
        main_frame = ttk.Frame(self)                            # New Frame object called main_frame
        main_frame.grid(row = 0, column = 0, sticky = 'w')      # Use grid method

        # 6 Labels
        ttk.Label(main_frame, text = f"Minimum Fine: ${self.speedingFineCalculator.minimumFine}").grid(row = 0, column = 0, sticky = 'w')
        ttk.Label(main_frame, text = f"Penalty per MPH over limit: ${self.speedingFineCalculator.penaltyPerMPH}").grid(row = 1, column = 0, sticky = 'w')
        ttk.Label(main_frame, text = f"Penalty for 50 MPH over limit: ${self.speedingFineCalculator.penalty50BeyondLimit}").grid(row = 2, column = 0, sticky = 'w')

        ttk.Label(main_frame, text = "Speed Limit: ").grid(row = 3, column = 0, sticky = 'w')
        ttk.Label(main_frame, text = "Clocked Speed: ").grid(row = 4, column = 0, sticky = 'w')
        ttk.Label(main_frame, text = "Speeding Fine: ").grid(row = 5, column = 0, sticky = 'w')

        # 3 Text Entry Boxes with Connection to DoubleVar (speedingFine is readonly)
        ttk.Entry(main_frame, width = 25, textvariable = self.speedLimit).grid(row = 3, column = 1, sticky = 'w')
        ttk.Entry(main_frame, width = 25, textvariable = self.clockedSpeed).grid(row = 4, column = 1, sticky = 'w')
        ttk.Entry(main_frame, width = 25, textvariable = self.speedingFine, state = 'readonly').grid(row = 5, column = 1, sticky = 'w')

        # Padding
        for child in main_frame.winfo_children():
            child.grid_configure(padx = 5, pady = 5)


    def initButtonsFrame(self):
        # Add implementation:
        # Creates a new Frame object and use grid method to add it to the parent frame (self).
        # Create and place three buttons to this frame using grid method.
        # Add the corresponding event-handlers to the buttons.    

        # Frame Object 
        buttons_frame = ttk.Frame(self)                              # New Frame object called buttons_frame
        buttons_frame.grid(row = 6, column = 0, columnspan = 2)      # Use grid method to position buttons_frame section in window

        # Three buttons using grid 
        # The command is the event handler
        # The index is relative to the buttons_frame, not the parent(self), therefore use buttons_frame as self
        ttk.Button(buttons_frame, text = "Calculate", command = self.calculateFine).grid(column = 0, row = 0, sticky = 'w', padx = 5, pady = 5)
        ttk.Button(buttons_frame, text = "Clear", command = self.clear).grid(column = 1, row = 0, sticky = 'w', padx = 5, pady = 5)
        ttk.Button(buttons_frame, text = "Exit", command = self.exit).grid(column = 2, row = 0, sticky = 'w', padx = 5, pady = 5)

        
    def calculateFine(self):
        # Add implementation: Event-handler for the ‘Calculate’ button.
        # Read the values of Entry boxes corresponding to the speeding limit and clocked speed.
        # Call the calculateSpeedingFine method on self.speedingFineCalculator object to calculate the fine,
        # populate the text entry box with the fine. 
        

        try:

            # Read values of Entry boxes and validate they are floats and not str (if str, triggers Exception)
            speed_limit = float(self.speedLimit.get())
            clocked_speed = float(self.clockedSpeed.get())

            # Validate values of Entry boxes are above 0
            if speed_limit <= 0 or clocked_speed <= 0:
                raise ValueError

            # Set the speedingLimit in speedingfine.py to be the speed_limit defined by user (not default 25)
            self.speedingFineCalculator.speedingLimit = speed_limit

            # Call calculateSpeedingFine from speedingfine.py 
            speed_fine = self.speedingFineCalculator.calculateSpeedingFine(clocked_speed)

            # Populate the Text Entry box with the fine
            formatted_fine = f"{speed_fine:.2f}"         # Two decimal places
            self.speedingFine.set(formatted_fine)

        except ValueError:

            messagebox.showerror("Error", "Please enter valid positive numbers - not 0 or negatives.")
            self.clear()

        except Exception:

            messagebox.showerror("Error", "Please enter valid positive numbers - not strings.")
            self.clear()


    def clear(self):
        # Add implementation: clear all the text entry boxes
        self.speedLimit.set("0.0")
        self.clockedSpeed.set("0.0")
        self.speedingFine.set("0.0")
    

    def exit(self):
        '''
        The event handler for the exit button.
        '''
        self.parent.destroy()                   # Destroys (exits) the program through parent frame
   

def main():
    '''
    Creates a root window, 
    creates and initializes SpeedingFindFrame class object, 
    and starts mainloop.
    '''

    root = tk.Tk()                                          # Creates main application window
    root.title("Speeding Fine Calculator of Funnyville")    # Sets the title of the window
    SpeedingFineFrame(root)                                 # Creates and packs the main frame
    root.mainloop()                                         # Starts event loop (makes it go)


if __name__ == "__main__":
    main()
