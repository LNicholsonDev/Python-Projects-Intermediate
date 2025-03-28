# Assignment: Project Part 2 - BlackJack Simulation
# Class: DEV 128
# Date: March 12th, 2025
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

    SUIT_ORDER = {'Clubs': 1, 'Diamonds': 2, 'Hearts': 3, 'Spades': 4}

    RANK_ORDER = {'2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7, 
    '9': 8, '10': 9, 'Jack': 10, 'Queen': 11, 'King': 12, 'Ace': 13}


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


    def __str__(self):
        '''
        Takes no parameters. 
        Returns string in the form: "rank of suit suitsymbol."
        Eg - King of Hearts ♥
        '''
        return f'{self.rank} of {self.suit}{CARDS_CHARACTERS[self.suit]} '
    

    # Rich Comparison
    def __lt__(self, other):

        if self.suit == other.suit:             # If suits are the same rank (eg, both cards spades)

            return self.RANK_ORDER[self.rank] < self.RANK_ORDER[other.rank]
        
        return self.SUIT_ORDER[self.suit] < self.SUIT_ORDER[other.suit]
    

    def __le__(self, other):

        if self.suit == other.suit:             # If suits are the same rank (eg, both cards spades)

            return self.RANK_ORDER[self.rank] <= self.RANK_ORDER[other.rank]
        
        return self.SUIT_ORDER[self.suit] <= self.SUIT_ORDER[other.suit]


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

        if self.__deck:
            return self.__deck.pop()        # takes last item in the shuffled deck
        
        else:
            return None                     # lists evaluate to False if empty
        
    
    def __iter__(self):
        for card in self.__deck:
            yield card


    def __len__(self):
        '''
        Returns number of cards in self.__deck (the deck of cards.)
        '''
        return len(self.__deck)


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
            
            if card.rank == 'Ace':
                aces_count += 1

            total_points += card.value

        while total_points > 21 and aces_count > 0:     # When total points exceeds 21 and there's an Ace in hand
            total_points -= 10                          # Reduce total points by 10 so that Ace = 1
            aces_count -= 1                             # Take away that used Ace to leave the while loop

        return total_points


    @property
    def isBusted(self):
        '''
        Returns True if points exceed 21.
        '''
        return self.points > 21         # returns boolean False if points greater than 21


    @property
    def hasBlackjack(self):
        '''
        Returns True if player has a hand equal to 21.
        '''
        return len(self.__cards) == 2 and self.points == 21        # returns boolean True only if both conditions met
    

    def addCard(self, new_card):
        '''Takes a Card object and appends it to __cards list (dealer/player's hand).'''

        self.__cards.append(new_card)

    
    def __str__(self):
        '''
        Prints the hand by printing displayCard method (from Card class) 
        of each card in the __cards list.
        '''

        self.sort()  # Ensure cards are sorted
        hand_string = []

        for card in self.__cards:
            hand_string.append(card.__str__())

        return '\n'.join(hand_string)


    def sort(self):
        '''
        Sorts the hand based on Rich Comparisons in Card.
        '''
        self.__cards.sort()   

    
    def shortDisplay(self):
        '''
        Returns a short string representation of the sorted hand cards.
        '''
        self.__cards.sort()
        card_string = []

        for card in self.__cards:
            card_string.append(f"{card.rank}{CARDS_CHARACTERS[card.suit]} ")
        
        return " ".join(card_string)
    

    def __iter__(self):
        for card in self.__cards:
            yield card

    
    def __len__(self):
        '''
        Returns the length of self.__cards (number of cards in hand).
        '''
        return len(self.__cards)


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

    print(hand1)
    print()

    print("Hand points:", hand1.points)
    print("Hand count:", hand1.count)
    print("Deck count:", deck2.count)
    print()

    print("TEST - Sorting hand: ")
    hand1.sort()
    print(hand1)

    print()
    print("TEST - shortDisplay of Hand:")
    print(hand1.shortDisplay())

    print()
    print("TEST - is hand busted?")
    print(f"Is busted: {hand1.isBusted}")       # @property do not get called with parens; access like attribute

    print()
    print("TEST - Is the hand blackjack?")
    print(f"Is blackjack: {hand1.hasBlackjack}")

    print()
    print("TEST - is Deck and Hand Iterable?")

    # print("Deck:")
    # for card in deck2:
    #     print(card)

    print("Hand:")      # Would produce TypeError if no __iter__ in Hand
    for card in hand1:
        print(card)


if __name__ == "__main__":
    main()
