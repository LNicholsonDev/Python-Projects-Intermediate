###########################################################################
#Speeding fine calculator program
# Define a class that represents the speeding limit for a town with
# predefined minimumFine, penaltyPerMPH and penalty50BeyondLimit values
# Once you have completed the SpeedingFineCalculator class, uncomment the code
# in main() and make sure the program runs as expected for valid and invalid
# inputs.
###########################################################################

class SpeedingFineCalculator:

    minimumFine = 50
    penaltyPerMPH = 5
    penalty50BeyondLimit = 200


    def __init__(self, limit=25):
        self.speedingLimit = limit


    @property
    def speedingLimit(self):
        return self.__speedingLimit


    @speedingLimit.setter
    def speedingLimit(self, newLimit):

        if (newLimit <= 0 ) :
            raise ValueError("Speed Limit cannot be negative.")
        
        self.__speedingLimit = newLimit


    def calculateSpeedingFine(self, clockedSpeed):

        if (clockedSpeed < 0):
            raise ValueError("Clocked speed cannot be negative.")
        
        if (clockedSpeed <= self.__speedingLimit):
            return 0
        
        else:

            diff = (clockedSpeed - self.__speedingLimit)
            fine = SpeedingFineCalculator.minimumFine + diff *SpeedingFineCalculator.penaltyPerMPH

            if (diff >= 50):
                fine += SpeedingFineCalculator.penalty50BeyondLimit

            return fine


def main():

    sep = "-"*80
    print(sep)
    print("Welcome to the Speeding Fine Calculator in Funnyville.")
    print(sep)
    print("Current MinimumFine = ${0}".format(SpeedingFineCalculator.minimumFine))
    print("Current penalty for each one mph over the limit = ${0}".format(SpeedingFineCalculator.penaltyPerMPH))
    print("Current penalty for going more than 50 mph over the limit = ${0}".format(SpeedingFineCalculator.penalty50BeyondLimit))
    print(sep)

    spFineCalc = SpeedingFineCalculator()
    ans = 'y'

    while (ans == 'y'):

        try:
          
          limit = int(input("Please enter the speed limit: "))
          spFineCalc.speedingLimit = limit
          speed = int(input("Please enter the clocked speed: "))
          fine = spFineCalc.calculateSpeedingFine(speed)
          print("Speeding fine for speed of "+str(speed) + " is $"+ str(fine))

        except Exception as e:
          
          print("Something went wrong ", e)
          
        print(sep)

        ans = input("Continue?(y/n) ").lower()


if __name__ == "__main__":
    main()
