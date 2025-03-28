# Assignment: Player Inheritance
# Class: DEV 128
# Date: February 17th, 2025
# Author: Leah Nicholson
# Description: Classes designed to handle baseball player data using inheritance.
# Pitcher and Batter objects are derived from Player superclass.


#!/usr/bin/env python3


class Player:
    '''
    Creates a Player object with player name and player position on team.
    '''

    # init with private attributes
    def __init__(self, name, position):

        # validate non-empty upon initialization
        if name == "":
            raise ValueError("name cannot be empty.")
        
        elif position == "":
            raise ValueError("position cannot be empty.")
        
        self.__name = name              # Player name - set
        self.__position = position      # Player position on team - set

    # getter method for name (read-only)
    @property
    def name(self):
        return self.__name
    
    # getter method for position (read-only)
    @property
    def position(self):
        return self.__position
    
    # returns stats string
    def getStats(self):
        '''Returns the player Name and Position in a string.'''
        return f"Name: {self.__name} Position: {self.__position}"
    

class Pitcher(Player):

    '''
    Creates Pitcher object derived from Player class.
    '''

    # init with public attributes
    def __init__(self, name, wins, losses):

        # validation for name, wins, losses
        if name == "":
            raise ValueError("name cannot be empty.")
        
        elif wins < 0:
            raise ValueError("wins cannot be negative.")
        
        elif losses < 0:
            raise ValueError("loss cannot be negative.")

        Player.__init__(self, name, position = "Pitcher")
        self.wins = wins        # public
        self.losses = losses    # public

    def getStats(self):
        '''Returns the player Name and Position in a string from Player superclass.
        Returns Pitcher-specific stats (wins and losses) from the Pitcher object.'''
        return Player.getStats(self) + f" {self.wins}-{self.losses} win-loss"


class Batter(Player):

    '''
    Creates Batter object derived from Player superclass.
    '''

    # init with public attributes
    def __init__(self, name, position, at_bats, hits):

        if name == "":
            raise ValueError("name cannot be empty.")
        
        elif position == "":
            raise ValueError("position cannot be empty.")
        
        elif at_bats < 0:       # at_bats - number of times Batter got turn against pitcher
            raise ValueError("at_bats cannot be negative.")
        
        elif hits < 0:          # hits - number of hits for the Batter
            raise ValueError("hits cannot be negative.")

        Player.__init__(self, name, position)    # include self
        self.at_bats = at_bats
        self.hits = hits

    @property   # read-only
    def average(self):

        if self.at_bats > 0:
            return self.hits / self.at_bats  
        
        else:
            return 0

    def getStats(self):
        '''Returns the player Name and Position in a string from Player superclass.
        Returns Batter-specific stats (Batting Avg) from the Batter object.
        '''
        return Player.getStats(self) + f" Batting Avg: {round(self.average, 3)}"
