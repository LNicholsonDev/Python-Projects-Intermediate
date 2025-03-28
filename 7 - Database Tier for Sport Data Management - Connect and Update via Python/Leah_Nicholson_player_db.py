# Assignment: Database Assignment
# Class: DEV 128
# Date: Monday March 10th, 2025
# Author: Leah Nicholson
# Description: Functions designed to support operations in provided Business/Presentation Tiers.
# This is the Database Tier for the Players' data manager program.


import sqlite3
from contextlib import closing
from player_objects import Player

conn = None


def connect():
    '''
    Establishes database connection.
    '''

    global conn

    if not conn:

        DB_FILE = "player_db.sqlite"
        conn = sqlite3.connect(DB_FILE)
        conn.row_factory = sqlite3.Row


def close():
    '''
    Closes the database connection.
    '''

    if conn:
        conn.close()


def get_players():
    ''' 
    Method to execute a query to 
    get the list of all players ordered by wins - player with the most wins first.
    Returns a list of Player class objects.
    '''

    with closing (conn.cursor()) as curr: 

        curr.execute("SELECT name, wins, losses, ties, playerID FROM Player ORDER BY wins DESC;")   
        players = []

        for row in curr.fetchall():     # fetchall since we are dealing with all players

            player = Player(row["name"], row["wins"], row["losses"], row["ties"], row["playerID"])  # call Player class
            players.append(player)

    return players


def get_player(name):
    '''
    Method to execute a query to 
    get all the data for the player with the given name. 
    Returns a Player class object with that data.
    '''
    
    with closing(conn.cursor()) as curr:

        curr.execute("SELECT name, wins, losses, ties, playerID FROM Player WHERE name = ?;", (name,))
        row = curr.fetchone()   # fetchone since we are dealing with one name
        
        if row:
            return Player(row["name"], row["wins"], row["losses"], row["ties"], row["playerID"])    # call Player class
        
    return None


def add_player(player):
    ''' 
    Method to execute a query to 
    add a new row in the database with the data of the player.
    '''

    with closing(conn.cursor()) as curr:

        curr.execute("INSERT INTO Player (name, wins, losses, ties) VALUES (?, ?, ?, ?);", (player.name, player.wins, player.losses, player.ties))
        conn.commit()


def delete_player(name):
    '''
    Method to execute a query to 
    delete the data in the database for the player with given name. 
    '''

    with closing(conn.cursor()) as curr:

        curr.execute("DELETE FROM Player WHERE name = ?;", (name,))
        conn.commit()


def main():

    connect()
    players = get_players()

    print()
    print()

    # Test all players:

    for player in players:
        print(player.name, player.id, player.wins, player.losses, player.ties, player.games)

    print()
    print()
    

    # Test player "Mike":

    player = get_player("Mike")

    if (player):
        print(player.name, player.id, player.wins, player.losses, player.ties, player.games)
    
    else:
        print(f"Player not found.")

    close()


if __name__ == "__main__":
    main()
