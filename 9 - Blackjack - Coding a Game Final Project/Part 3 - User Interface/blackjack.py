# Assignment: Project Part 2 - BlackJack Simulation
# Class: DEV 128
# Date: March 12th, 2025
# Author: Leah Nicholson
# Description: Simulates the card game BlackJack with simplified rules.


#!/usr/bin/env python3


from Leah_Nicholson_objects import Card, Deck, Hand


class Blackjack:
    '''Allows the game of Blackjack to be played.'''


    def __init__(self, startingBalance):
            
        self.startingBalance = startingBalance  # self.startingBalance is the starting balance (doesn't change)
        self.bet = 0
        self.money = self.startingBalance       # self.money is the current available balance (money is basically money left)
        self.deck = None
        self.dealerHand = None
        self.playerHand = None
        

    def getBet(self):       # Does this method get used in gui?
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


    def takeDealerTurn(self):
        '''
        Method to play Dealer's turn.
        Dealer draws one more card.
        Then, deals cards until points total 17 or more. 
        '''
        
        # Draws one more card
        self.dealerHand.addCard(self.deck.dealCard())   

        if self.dealerHand.hasBlackjack:
            return

        # Draws cards until points total 17 or more

        while self.dealerHand.points < 17:

            self.dealerHand.addCard(self.deck.dealCard()) 



    def determineOutcome(self):
        '''
        Method to determine the winner.
        Looks at playerHand and dealerHand.
        Updates self.money accordingly.
        Returns a string giving details of the resulting outcome.'''

       
        # Busted

        if self.dealerHand.isBusted:

            if self.playerHand.hasBlackjack:
                new_money = self.money + (self.bet + (1.5 * self.bet))
                self.money = new_money
                return "Blackjack! You win!"    # Display blackjack message if dealer busts and player has blackjack
            
            else:   # Treat like a regular win
                new_money = (self.money + self.bet) + self.bet
                self.money = new_money
                return "Yay! The dealer busted. You win!"
        

        elif self.playerHand.isBusted:
            return "Sorry. You busted. You lose."
        
        # Blackjacks 

        elif self.playerHand.hasBlackjack:
            new_money = self.money + (self.bet + (1.5 * self.bet))
            self.money = new_money
            return "Blackjack! You win!"
        
        elif self.dealerHand.hasBlackjack:
            return "Sorry. Dealer has blackjack. You lose."
        
        # Push (dealer and player have same points)
        elif self.dealerHand.points == self.playerHand.points:
            new_money = self.money + self.bet       # Add back the bet
            self.money = new_money
            return "You push."
        
        # Player win
        elif self.dealerHand.points < self.playerHand.points and self.playerHand.points <= 21:
            new_money = (self.money + self.bet) + self.bet
            self.money = new_money
            return "Hooray! You win!"
        
        # Player lose
        elif self.dealerHand.points > self.playerHand.points and self.dealerHand.points <= 21:
            return "Sorry. Dealer wins."





def main():


    print()
    print()
    print("BLACKJACK!")
    print("Blackjack payout is 3:2")


    # initialize starting money
    print("Starting Balance: 100")

    # instantiate object of Blackjack class 
    blackjack1 = Blackjack(100)
    

    print("Setting up a round...")
    blackjack1.getBet()
    blackjack1.setupRound()
    print()


    print("Playing Player Hand...")

    while True:
        
        player_choice = input("Hit(h) or Stand(s)?: ").lower()



        if player_choice == 's':
            
            print(f"Points: {blackjack1.playerHand.points}")

            if blackjack1.playerHand.hasBlackjack:
                print(blackjack1.determineOutcome())
            
            else:
                blackjack1.takeDealerTurn()
                blackjack1.displayCards(blackjack1.dealerHand, "AFTER DEALER CALL")
                print(blackjack1.determineOutcome())
                print("Money total for player: ", blackjack1.money)

            break



        elif player_choice == 'h':

            blackjack1.takePlayerTurn()             # deal a card to the player by calling takePlayerTurn method
            bust = blackjack1.playerHand.isBusted              # check if playerHand is busted

            blackjack1.displayCards(blackjack1.playerHand, "YOUR CARDS")
            print()

            if bust:                                # if True, print points and exit
                print(f"YOUR FINAL POINTS: {blackjack1.playerHand.points}")
                print(blackjack1.determineOutcome())
                print("Money total for player: ", blackjack1.money)
                break

        
        else:
            print("Invalid command.")       # user did not enter 's' or 'h'
            

   
    print("Good bye!")
    


if __name__ == "__main__":
    main()
