import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from speedingfine import SpeedingFineCalculator
#Class for the Presentation layer
class SpeedingFineFrame(ttk.Frame):
    def __init__(self, parent):

        ttk.Frame.__init__(self, parent,padding="10 10 10 10")
        # Business tier class
        self.speedingFineCalculator = SpeedingFineCalculator()

        #Save the parent so we can call destroy on the parent window
        self.parent = parent
        
        # Define variables for text entry fields
        self.speedLimit= tk.DoubleVar()
        self.clockedSpeed= tk.DoubleVar()
        self.speedingFine= tk.DoubleVar()
       
        self.initComponents()
        
    def initComponents(self):
        self.pack()
        self.initMainFrame()
        self.initButtonsFrame()
        
 
    def initMainFrame(self):
        #Add implementation:
        #Create a new Frame object and use grid method to add it to the parent frame (self).
        #Create and place the 6 labels and 3 text entry boxes.
        #Connect the DoubleVar attributes declared in the constructor to the text entry boxes.
        pass
        
    def initButtonsFrame(self):
        #Add implementation:
        #Creates a new Frame object and use grid method to add it to the parent frame (self).
        #Create and place three buttons to this frame using grid method.
        #Add the corresponding event-handlers to the buttons.    
        pass
        
    def calculateFine(self):
        #Add implementation
        # Event-handler for the ‘Calculate’ button.
        # Read the values of Entry boxes corresponding to the speeding limit and clocked speed.
        # call the calculateSpeedingFine method on self.speedingFineCalculator object to calculate the fine,
        # populate the text entry box with the fine. 
        pass

    def clear(self):
        # Add implementation: clear all the text entry boxes
        pass
    
    def exit(self):
        self.parent.destroy()

        

def main():
    root = tk.Tk()
    root.title("Speeding Fine Calculator of Funnyville")
    SpeedingFineFrame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
