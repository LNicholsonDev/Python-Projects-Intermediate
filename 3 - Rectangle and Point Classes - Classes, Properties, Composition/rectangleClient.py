############################################################################
##Client code to test the Rectangle and Point classes
## 1. Creates 4 rectangles:
##      two with valid arguments
##      two with invalid arguments
## 2. Verifies that Rectangle.rectangleCount is correct
## 3. Doubles width and height of Rectngles[0], prints the rectangle before and after
## 4. Translates Rectngles[1], prints the rectangle before and after
## 5. Attempts to set width of -2 on Rectangles[2]
## 6. Updates width and height of Rectangles[3] successfully
############################################################################
from Leah_Nicholson_rectangle import Rectangle, Point

##Variable to enable/disable assert checks
# Set this to False, if you don't want the checkRectangle and checkValue to be called.
checkAll = False

def printRectangle(rect):
    ''' Function to print all the properties of a Rectangle object'''
    print(f'Top: {rect.topLeft.y}, Left: {rect.topLeft.x}, Width: {rect.width}, Height: {rect.height}, ' +
          f'Bottom: {rect.bottomRight.y}, Right: {rect.bottomRight.x}, Area: {rect.area}, Perimeter: {rect.perimeter}')

def checkRectangle(rect, expected):
    ''' Function to check all the properties of a Rectangle object against the list of values
provided in the second parameter (expected)'''
    if (checkAll):
        actual = [rect.topLeft.y, rect.topLeft.x, rect.width, rect.height,
                  rect.bottomRight.y,rect.bottomRight.x, rect.area, rect.perimeter]
        for a, b in zip(actual, expected):
            assert(a == b)
    
def checkValue(x, y):
    if (checkAll):
        assert(x == y)
def main():
    starline = "*"*50
    dashline = "-"*50
    print(starline+"\nTesting Rectangle and Point classes.")
    print(starline)
    
    ############################################################################    
    #data used to create 4 rectangles
    # [left,top,width,height]
    rawData = [[1,2,3,4],[5,6,7,8],[9,10,0,12],[13,14,15,-4]]

    #Create 4 Rectangle objects using rawData
    rectangles = []

    for k, d in enumerate(rawData):
            print(f"Creating Rectangle {k}")
            r = Rectangle(Point(d[0],d[1]),d[2],d[3])
            rectangles.append(r)
    ############################################################################

    print(starline)
    print("Checking rectangle count, should be 4.")
    print("Rectangle count: ", Rectangle.rectangleCount)
    checkValue(Rectangle.rectangleCount, 4)
    print(starline)

    ############################################################################
    #Process Rectangles one by one and print the properties before and after
    ############################################################################

    print("Rectangles[0] before processing.")
    printRectangle(rectangles[0])
    checkRectangle(rectangles[0], [2,1,3,4,6,4,12,14])
    print(dashline)
    #Change the width and height of rectagnles[0]
    rectangles[0].width *= 2
    rectangles[0].height *= 2
    print("Rectangles[0] after doubling width and height.")
    printRectangle(rectangles[0]) # Should show width and height doubled
    checkRectangle(rectangles[0],[2,1,6,8,10,7,48,28])
    print(starline)

    ############################################################################

    #Translate rectangles[1]
    print("Rectangles[1] before processing.")
    printRectangle(rectangles[1])
    checkRectangle(rectangles[1], [6,5,7,8,14,12,56,30])
    print(dashline)
    rectangles[1].translate(10,10)
    print("Rectangles[1] after translating by (10,10).")
    printRectangle(rectangles[1])# Should show rectangle top-left is moved
    checkRectangle(rectangles[1], [16,15,7,8,24,22,56,30])
    print(starline)

    ############################################################################
    print("Rectangles[2] before processing.")
    printRectangle(rectangles[2])
    checkRectangle(rectangles[2],[10,9,1,12,22,10,12,26])
    print(dashline)

    #Attempt to set the width of rectagnles[2] to -2
    rectangles[2].width = -2
    print("Rectangles[2] after attempting to set width to -2.")
    printRectangle(rectangles[2])# Should show error message and width should be unchanged
    checkRectangle(rectangles[2],[10,9,1,12,22,10,12,26])
    print(starline)
    ############################################################################

    # Reset width and height of Rectangle[3] to 15 and 16
    print("Rectangles[3] before processing.")
    printRectangle(rectangles[3])
    checkRectangle(rectangles[3], [14,13,15,1,15,28,15,32])
    print(dashline)
    rectangles[3].width = 15
    rectangles[3].height = 16
    print("Rectangles[3] after resetting width and height to 15 and 16.")
    printRectangle(rectangles[3])# Should show width of 15 and height of 16
    checkRectangle(rectangles[3],[14,13,15,16,30,28,240,62])
    print(starline)
    ############################################################################

    print("Thanks for your patience! Goodbye")
    ############################################################################

if (__name__ == "__main__"):
    main()
