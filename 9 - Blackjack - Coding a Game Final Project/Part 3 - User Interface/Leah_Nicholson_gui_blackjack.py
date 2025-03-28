# Assignment: Project Part 3 - BlackJack Simulation
# Class: DEV 128
# Date: March 18th, 2025
# Author: Leah Nicholson
# Description: Presentation tier GUI for the Blackjack game.
# Simulates the card game BlackJack with simplified rules.


#!/usr/bin/env python3


# Implement playerCanPlayTurn method and play, hit, and stand event handlers

import tkinter as tk
from tkinter import ttk
from blackjack import Blackjack
from Leah_Nicholson_objects import Card, Hand, Deck

STARTING_BALANCE = 100


class BlackjackFrame(ttk.Frame):

    def __init__(self, parent):

        '''
        Initializes the frame for the Blackjack game.
        '''

        ttk.Frame.__init__(self, parent, padding="10 10 10 10")        # Creates new Frame object
        self.parent = parent                                           # Stores reference to parent attribute

        # Instantiate the business class object
        self.game = Blackjack(STARTING_BALANCE)         # Blackjack instance "game" is called, receives start balance (100)
        self.gameOver = True                            # Initialized to a not-in-progress game





        # Define GUI string variables to be used with text entry fields
        # These help connect attributes of Blackjack object to values stored in text boxes

        self.money = tk.StringVar()                 # self.money is UI VARIABLE - It is starting money/updates as time goes
        self.bet = tk.StringVar()

        self.dealerCards = tk.StringVar()
        self.dealerPoints = tk.StringVar()

        self.playerCards = tk.StringVar()
        self.playerPoints = tk.StringVar()

        self.result = tk.StringVar()



        # Inititalize components
        self.initComponents()                           # Calls initComponents() to set up GUI window labels/entry/buttons


        # Display current money amount
        self.money.set("$" + str(self.game.money))      # self.game.money = current amount of money in the game instance. we set self.money (ui display) to this value
        

        #Initialize bet to 0
        self.bet.set("0")






    def initComponents(self):
        '''
        Initializes the components of the GUI window.
        '''

        self.pack()                 # self is the Blackjack Frame (a ttk.Frame). This line makes it visible inside parent(the Tk window in root = tk.Tk())
        
        # Display the grid of labels and text entry fields

        # Money and Bet
        ttk.Label(self, text = "Money:").grid(column = 0, row = 0, sticky = tk.E)
        ttk.Entry(self, width = 25, textvariable = self.money, state = "readonly").grid(column = 1, row = 0, sticky = tk.W)
        
        ttk.Label(self, text = "Bet:").grid(column = 0, row = 1, sticky = tk.E)
        ttk.Entry(self, width = 25, textvariable = self.bet).grid(column = 1, row = 1, sticky = tk.W)
        

        # Dealer Cards and Points
        ttk.Label(self, text = "DEALER").grid(column = 0, row = 2, sticky = tk.E)
        
        ttk.Label(self, text = "Cards:").grid(column = 0, row = 3, sticky = tk.E)
        ttk.Entry(self, width = 50, textvariable = self.dealerCards, state = "readonly").grid(column = 1, row = 3, sticky = tk.W)
        
        ttk.Label(self, text = "Points:").grid(column = 0, row = 4, sticky = tk.E)
        ttk.Entry(self, width = 25, textvariable = self.dealerPoints, state = "readonly").grid(column = 1, row = 4, sticky = tk.W)
        

        # YOU (Player) Cards and Points
        ttk.Label(self, text = "YOU").grid(column = 0, row = 5, sticky = tk.E)
        
        ttk.Label(self, text = "Cards:").grid(column = 0, row = 6, sticky = tk.E)
        ttk.Entry(self, width = 50, textvariable = self.playerCards,state = "readonly").grid(column = 1, row = 6, sticky = tk.W)
        
        ttk.Label(self, text = "Points:").grid(column = 0, row = 7, sticky = tk.E)
        ttk.Entry(self, width = 25, textvariable = self.playerPoints, state = "readonly").grid(column = 1, row = 7, sticky = tk.W)


        # Make Hit and Stand Buttons
        self.makeButtons1()


        # Result
        ttk.Label(self, text = "RESULT:").grid(column = 0, row = 9, sticky = tk.E)
        ttk.Entry(self, width = 50, textvariable = self.result, state = "readonly").grid(column = 1, row = 9, sticky = tk.W)


        # Make Play and Exit Buttons
        self.makeButtons2()


        # Padding
        for child in self.winfo_children():
            child.grid_configure(padx = 5, pady = 3)



    def makeButtons1(self):
        '''
        Makes the first set of buttons: Hit and Stand.
        '''

        # Create a frame to store the two buttons
        buttonFrame = ttk.Frame(self)

        # Add the button frame to the bottom row of the main grid
        buttonFrame.grid(column = 1, row = 8, sticky = tk.W)

        # Add two buttons to the button frame
        ttk.Button(buttonFrame, text = "Hit", command = self.hit).grid(column = 0, row = 0)
        ttk.Button(buttonFrame, text = "Stand", command = self.stand).grid(column = 1, row = 0)



    def makeButtons2(self):
        '''
        Makes the second set of buttons: Play and Exit.
        '''

        # Create a frame to store the two buttons
        buttonFrame = ttk.Frame(self)

        # Add the button frame to the bottom row of the main grid
        buttonFrame.grid(column = 1, row = 10, sticky = tk.W)

        # Add two buttons to the button frame
        ttk.Button(buttonFrame, text = "Play", command = self.play).grid(column = 0, row = 0)
        ttk.Button(buttonFrame, text = "Exit", command = self.exit).grid(column = 1, row = 0)



    def displayDealer(self):
        ''' 
        Method to update dealer hand and the dealer points in the GUI
        '''

        # get the values of dealerhand and dealer points from the game instance
        dealer_hand = self.game.dealerHand.shortDisplay()        
        dealer_points = self.game.dealerHand.points

        # update the GUI values with SET
        self.dealerCards.set(dealer_hand)
        self.dealerPoints.set(dealer_points)    
    

    def displayPlayer(self):
        '''
        Method to update the player hand 
        and the player points in the GUI
        '''
        # get the values of playerhand and player points from the game instance
        player_hand = self.game.playerHand.shortDisplay()          # DONT use GET with the game instance
        player_points = self.game.playerHand.points

        # update the GUI values with SET
        self.playerCards.set(player_hand)
        self.playerPoints.set(player_points)

    

    def displayResult(self):
        ''' Method to update the result of the game
        Calls determineOutcome to decide what the outcome of the game is
        Updates the result and the money
        '''

        self.result.set(self.game.determineOutcome())
        self.money.set(f"${self.game.money}")


    def playerCanPlayTurn(self):
        ''' Method confirms that the game is underway 
        sets result to blank,
        and returns True indicating that player can play a turn 
        (i.e. can select hit or stand)
        
        otherwise if game in not underway, 
        updates result with correct feedback, 
        and returns False
        '''
            
        if self.gameOver:               # If True that the game is over
            self.result.set("Game not in progress.")
            return False
        
        else:                           # If gameOver is False, a game is in progress     
            self.result.set("")         # set result to blank
            return True



    def hit(self):
        '''
        Method to implement user selecting to hit.

        Method confirms that user can play a turn, 
        if not returns 

        else calls the takePlayerTurn 
        and reports the player state by calling displayPlayer.

        Next checks if player is busted, 
        if so ends the game 
        and updates the result by calling displayResult.
        '''

        if self.playerCanPlayTurn():

            self.result.set("")                     # remove text
            self.game.takePlayerTurn()              # Good for checking: self.result.set("You can play a turn!")
            self.displayPlayer()

            if self.game.playerHand.isBusted:       # Bool objects not callable (don't use parentheses)
                self.gameOver = True
                self.displayResult()

        else:
            return




    def stand(self):
        ''' 
        Method to implement user selecting to stand.
        Method confirms that user can play a turn, 
        if not returns 
        else ends the game and has the dealer play his turn 
        and reports the dealer state by calling displayDealer.
        Finally updates the result by calling displayResult.        
        '''


        if self.playerCanPlayTurn():     # Call as a function so Stand button won't work if game is over
            self.gameOver = True         # Player can no longer play
            self.game.takeDealerTurn()   # Dealer takes their turn
            self.displayDealer()         # Report the dealer's state (hand)
            self.displayResult()         # Display game results
        else:
            return

            

    def play(self):
        '''
        Method to start a new game.

        Method checks that the game is not already underway
        if game underway: gives feedback in results and returns

        Else
        First reads the bet amount and verifies that it is valid
        If not valid, gives feedback by updating the result textEntry and returns

        Next starts the game by updating gameover,
        setting the bet on the game,
        calling setupRound 
        and 
        displaying player's & dealer's card and points.

        It should also check for a blackjack and take needed actions. 
        '''
        
        if self.gameOver:

            # get the bet value from the textbox            
            bet = float(self.bet.get().replace("$", ""))        # Take out dollar sign for float conversions
            monies = float(self.money.get().replace("$", ""))

            # verify bet value and set it in the game instance
            if bet > monies:
                self.result.set("You don't have enough money to make that bet.")
                return

            if bet <= 0:
                self.result.set("Invalid amount. Enter a positive number.")
                return
            
            self.game.bet = bet         # send value from textbox to game instance
            self.game.money -= bet      # subtract bet from money
      
 
            self.result.set("")         # remove results box text
            self.gameOver = False       # update gamestatus - game is not over, game now in play
            self.game.setupRound()

            # update the GUI with the dealer and player cards and points
            self.displayDealer()
            self.displayPlayer()
            
            # check for blackjack
            if self.game.playerHand.hasBlackjack:
                self.game.takeDealerTurn()          # Dealer still takes a turn to see if they reach 21, causing a push
                self.displayDealer()                # Display that additional turn
                self.displayResult()                # Display the result
                self.gameOver = True


        else:
            self.result.set("The game is already in play.")
            return




    def exit(self):
        '''
        Allows user to exit the game.
        '''

        self.parent.destroy()


if __name__ == "__main__":

    root = tk.Tk()
    root.title("Blackjack")
    BlackjackFrame(root)
    root.mainloop()
