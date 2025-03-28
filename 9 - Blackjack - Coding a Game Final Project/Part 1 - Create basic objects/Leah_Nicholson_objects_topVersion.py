# Assignment: Project Part 1 - BlackJack Simulation
# Class: DEV 128
# Date: February 26th, 2025
# Author: Leah Nicholson
# Description: Classes designed to handle Cards, Decks, and Hands.
# Simulates the card game BlackJack with simplified rules.


#!/usr/bin/env python3


import random
CARDS_CHARACTERS = {"Spades": "♠", "Hearts": "♥", "Diamonds": "♦", "Clubs": "♣"}


class Card:

    '''
    Creates a playing card with suit and rank attributes.
    '''
    def __init__(self, rank, suit):

        self.rank = rank       # public
        
        if suit not in CARDS_CHARACTERS:
            raise ValueError("Not a possible card.")
        
        self.suit = suit        # public


    @property
    def value(self):
        '''
        Represents points value of the card.
        '''

        # Rank checks and value assignments

        face_values = ['Jack', 'Queen', 'King']

        if self.rank in face_values:
            return 10
            
        elif self.rank == 'Ace':
            return 11     
        
        else:
            return int(self.rank)        # For numerical cards


    def displayCard(self):
        '''
        Takes no parameters. 
        Returns string in the form: "rank of suit suitsymbol."
        Eg - King of Hearts ♥
        '''
        return f'{self.rank} of {self.suit} {CARDS_CHARACTERS[self.suit]}'


    def __str__(self):
        '''
        Returns string for Card object with rank and suit value.
        '''
        return f"Suit: {self.suit}, Rank: {self.rank}"


class Deck:
    '''
    Represents a Deck of cards.
    Calls Card class 52 times to make 52 cards.
    Stores these cards in a private list called __deck.
    '''
    
    def __init__(self):

        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        self.__deck = []

        for suit in suits:          # Refers to suits list                       
            for rank in ranks:      # Refers to ranks list
                self.__deck.append(Card(rank, suit))  # Call Card class with each rank and suit to make a card, and append it self.__deck list (52x)   


    @property
    def count(self):
        '''Provides count of cards in the deck.'''
        return len(self.__deck)


    def __str__(self):

        card_list = []

        for item in self.__deck:
            card_list.append(str(item))         # creates a card_list containing Card instances

        deck_string = ' \n'.join(card_list)     # creates deck_string which allows single line printing

        return f'START OF DECK: {deck_string}'
    

    def shuffle(self):
        random.shuffle(self.__deck)     # accesses import, calls shuffle function on the deck of cards


    def dealCard(self):

        # if self.__deck != []:
        #     return self.__deck.pop()        # takes last item in the list by default
        # else:
        #     return None

        if self.__deck:
            return self.__deck.pop()        # takes last item in the shuffled deck
        else:
            return None                      # simpler way; lists evaluate to False if empty


class Hand:
    '''
    Representation of dealer's hand or player's hand.
    '''

    def __init__(self):

        self.__cards = []       # Holds card objects (rank, suit)

    @property
    def count(self):
        '''Provides the count of the cards in the hand.'''
        return len(self.__cards)
    
    @property
    def points(self):
        '''Provides the points value of the hand.'''

        total_points = 0
        aces_count = 0

        for card in self.__cards:
            total_points += card.value

        # # Accomodating for ACES being 1 or 11
        #     if card.rank == 'Ace':
        #         aces_count += 1

        # while total_points > 21 and aces_count > 0:     # When total points exceeds 21 and there's an Ace in hand
        #     total_points -10                            # Reduce total points so that Ace = 1
        #     aces_count -= 1                             # Take away that used Ace to leave the while loop

        return total_points



    def addCard(self, new_card):
        '''Takes a Card object and appends it to __cards list (dealer/player's hand).'''

        self.__cards.append(new_card)

    
    def displayHand(self):
        '''
        Prints the hand by printing displayCard method (from Card class) 
        of each card in the __cards list.
        '''

        for card in self.__cards:
            print(card.displayCard())





##########################################################################
# TESTING Card, Deck, and Hand
##########################################################################

        
def main():

    print()
    print("TEST: CARDS")
    print()

    # Define the card variables with Card instances
    card1 = Card("King", "Hearts")  # 10
    card2 = Card("7", "Spades")     # 7
    card3 = Card("Queen", "Hearts") # 10
    card4 = Card("Ace", "Hearts")   # 11
    card5 = Card("Jack", "Hearts")  # 10
    card6 = Card("1", "Hearts")     # 1
    card7 = Card("2", "Hearts")     # 2
    card8 = Card("3", "Hearts")     # 3


    print(card1.displayCard())      # Don't forget parens, or it prints <>
    print(card1)                    # accesses __str__(self) as defined in Card class
    print(card2.displayCard())
    print(card2) 
    print("**********")


    print("Test of values:")
    print(f"Card 1 - value: {card1.value}")
    print(f"Card 2 - value: {card2.value}")
    print(f"Card 3 - value: {card3.value}")
    print(f"Card 4 - value: {card4.value}")
    print(f"Card 5 - value: {card5.value}")
    print(f"Card 6 - value: {card6.value}")
    print(f"Card 7 - value: {card7.value}")
    print(f"Card 8 - value: {card8.value}")
    print()

    print("TEST: DECK")
    print()
    print("UNSHUFFLED Deck: ")
    deck1 = Deck()                   # variable deck1 holds the instance of Deck
    print(deck1)                     # accesses __str__(self) in deck
    print()

    print("SHUFFLED Deck: ")
    deck1.shuffle()                  # can call methods on deck1
    print(deck1)
    print()

    print("Deck created.")
    print()

    print("TEST: DEALING A CARD --")
    print()

    for _ in range(53):

        dealt_card = deck1.dealCard()       # deal a card (pops from self.__deck in deck1 instance)

        if dealt_card is None:
            print("No more cards!")         # Will show 1 time, because range is 53, but there are 52 cards

        else:
            print(f"Dealt card | {dealt_card}")



    print()
    print("TEST: CARD COUNTS --")
    print("Deck1 count:", deck1.count)

    deck2 = Deck()
    deck2.shuffle()    

    print("Deck2 count:", deck2.count)
    print()



    print("TEST: HAND")
    
    hand1 = Hand()                          # create a hand instance in variable hand1

    for _ in range(4):                      # loops 0, 1, 2, 3 times (total 4)
        hand1.addCard(deck2.dealCard())     # creates hand1 holding 4 cards from deck2 (deck2.dealCard is new_card in addCard function of Hand class)

    hand1.displayHand()
    print()

    print("Hand points:", hand1.points)
    print("Hand count:", hand1.count)
    print("Deck count:", deck2.count)
    print()

if __name__ == "__main__":
    main()
