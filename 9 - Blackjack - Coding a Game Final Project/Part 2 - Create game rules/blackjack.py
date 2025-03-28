# Assignment: Project Part 2 - BlackJack Simulation
# Class: DEV 128
# Date: March 12th, 2025
# Author: Leah Nicholson
# Description: Simulates the card game BlackJack with simplified rules.


#!/usr/bin/env python3


from Leah_Nicholson_objects_topVersion2 import Card, Deck, Hand


class Blackjack:
    '''Allows the game of Blackjack to be played.'''


    def __init__(self, startingBalance):
            
        self.startingBalance = startingBalance  # self.startingBalance is the starting balance (doesn't change)
        self.bet = 0
        self.money = self.startingBalance       # self.money is the current available balance (money is basically money left)
        self.deck = None
        self.dealerHand = None
        self.playerHand = None
        

    def getBet(self):
        '''
        Method to update self.bet by prompting the user for the bet amount,
        making sure bet is less than self.startingBalance.
        '''

        while True:

            try:

                bet = int(input("Bet amount: "))

                if bet <= 0:
                    print("Invalid amount. Enter a positive number.")

                elif bet > self.money:
                    print("You don't have enough money to make that bet.")

                else: 
                    self.bet = bet
                    self.money -= self.bet
                    break
            
            except ValueError:

                print("Invalid input - please enter an integer.")


    def setupRound(self):
        ''' 
        Initializes self.deck to a new DECK object and shuffle it
        Initializes self.dealerHand and self.playerHand to new HAND objects
        Deals two cards to the playerHand, and one card to the dealerHand
        Prints dealerHand and playerHand using displayCards method
        '''
        # Initialize DECK object
        self.deck = Deck()
        self.deck.shuffle()

        # Initialize HAND objects
        self.playerHand = Hand()
        self.dealerHand = Hand()
        
        # Deal two cards out of deck object, and add it to playerHand
        for _ in range(0, 2):
            self.playerHand.addCard(self.deck.dealCard())
        
        # Deal a card out of deck object, and add it to dealerHand
        self.dealerHand.addCard(self.deck.dealCard())

        # Display the hands 
        self.displayCards(self.dealerHand, "DEALER'S SHOW CARD: ")
        self.displayCards(self.playerHand, "YOUR CARDS: ")



    def displayCards(self, hand, title):
        '''
        Print the title, cards, and points of the hand.
        '''
        print()
        print(title)
        print()
        print(hand)
        print("Points:", hand.points)


    def takePlayerTurn(self):
        ''' 
        Method to simulate player playing one turn by dealing a card
        to the player.
        '''
        self.playerHand.addCard(self.deck.dealCard())   # calls dealCard of Deck class on self.deck instance, takes card and addCard to playerHand Hand instance



def main():


    print()
    print()
    print("BLACKJACK!")
    print("Blackjack payout is 3:2")


    # initialize starting money
    money = 100
    print("Starting Balance:", money)

    # instantiate object of Blackjack class 
    blackjack1 = Blackjack(money)
    

    print("Setting up a round...")
    blackjack1.getBet()
    blackjack1.setupRound()
    print()


    print("Playing Player Hand...")

    while True:
        
        player_choice = input("Hit(h) or Stand(s)?: ").lower()

        if player_choice == 's':
            print(f"Points: {blackjack1.playerHand.points}")
            break

        elif player_choice == 'h':
            blackjack1.takePlayerTurn()             # deal a card to the player by calling takePlayerTurn method
            bust = blackjack1.playerHand.isBusted              # check if playerHand is busted

            blackjack1.displayCards(blackjack1.playerHand, "YOUR CARDS: ")
            print()


            if bust:                                # if True, print points and exit
                print(f"YOUR FINAL POINTS: {blackjack1.playerHand.points}")
                break

        else:
            print("Invalid command.")       # user did not enter 's' or 'h'
            

   
    print("Good bye!")
    


if __name__ == "__main__":
    main()
