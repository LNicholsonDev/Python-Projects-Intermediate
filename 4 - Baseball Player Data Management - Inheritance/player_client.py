from Leah_Nicholson_player import Batter, Pitcher
# Client code to build a Base ball team with players at
# different positions using the Batter and Pitcher classes.

def main():
    
    PlayerData = [
        ["Tommy La Stella", "3B", 1316, 360],
        ["Mike Yastrzemski", "RF", 563, 168],
        ["", "2B", 1473, 407],
        ["Donovan Solano", "", 1473, 407],
        ["Donovan Solano", "2B", -3, 407 ],
        ["Donovan Solano", "2B", 1473, -4],
        ["Donovan Solano", "2B", 1473, 407],
        ["Buster Posey", "C", 4575, 1380 ],
        ["Brandon Belt", "1B",  3811, 1003],
        ["Brandon Crawford", "SS",  4402, 1099],
        ["Alex Dickerson", "LF",  586, 160],
        ["Austin Slater", "CF",  569, 147 ]]
    
    PitcherData = [
        ["", 12,10],
        ["Kevin Gausman", -12,10],
        ["Kevin Gausman", 12,-10],        
        ["Kevin Gausman", 12,10]]
    
    team = []

    print("Welcome")
    print("Building the team ...")
    print("Adding batters...")

    for k, row in enumerate(PlayerData):
        try:
            print("Adding...",k, end="  ")
            name, pos, at_bats, hits = row
            b = Batter(name, pos, at_bats, hits)
            team.append(b)
            print("....Success")

        except Exception as e:
            print(".....Failure: ", e)

    print("Adding a Pitcher...")

    for k, row in enumerate(PitcherData):

        try:
            print("Adding...",k, end="  ")
            name, w, l = row
            p = Pitcher(name,w, l)
            team.append(p)
            print("....Success")

        except Exception as e:
            print(".....Failure: ", e)
            
    try:
        print("Setting properties...", end="  ")
        team[2].at_Bats = 600
        team[8].wins += 1
        print("....Success")
        
    except Exception as e:
            print(".....Failure: ", e)
        
    print("Getting stats")
    for k in team:
        print(k.getStats())


if __name__ == "__main__":
    main()
    

