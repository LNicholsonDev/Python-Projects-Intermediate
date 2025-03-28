from furniture import FurnitureGallery, Furniture, Table, Bed
def main():
    
    TableData = [[100, "Pine"],
            [ 75, "Oak"],
            [-30, "Teak"],
            [50, 50]]
    BedData = [[200, "King"],
               [150,"Queen"],
               [95, "Twin"]]

    furn = FurnitureGallery()
    for k, row in enumerate(TableData):
        try:
            print("Adding...",k, end="  ")
            wt, wd = row
            s = Table(wt,wd)
            furn.addFurniture(s)
            print("....Success")
            print()
        except Exception as e:
                print()
                print(e)
    for k, row in enumerate(BedData):
        try:
            print("Adding...",k, end="  ")
            wt, sz = row
            s = Bed(wt,sz)
            furn.addFurniture(s)
            print("....Success")
            print()
        except Exception as e:
                print()
                print(e)

    for f in furn:
        print(f)

    print("After sorting")
    furn.sort()
    for f in furn:
        print(f)


if __name__ == "__main__":
    main()
    
