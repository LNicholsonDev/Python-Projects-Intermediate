
#!/usr/bin/env python3

from Leah_Nicholson_objects_topVersion2 import Card, Deck, Hand

import random

CARDS_CHARACTERS = {"Spades": "♠", "Hearts": "♥", "Diamonds": "♦", "Clubs": "♣"}

##########################################################################
## Definitions for the classes: Card, Deck and Hand
##########################################################################

def main():

    print("Cards - Tester")
    print()

    # test deck
    print("DECK")
    deck = Deck()

    print("Deck created.")
    deck.shuffle()    
    
    print("Deck shuffled.")
    print("Deck count:", deck.count)
    print()

    # test hand
    print("HAND")
    hand = Hand()

    for i in range(4):
        hand.addCard(deck.dealCard())

    hand.displayHand()

    print()
    print("Hand points:", hand.points)
    print("Hand count:", hand.count)
    print("Deck count:", deck.count)

if __name__ == "__main__":
    main()
