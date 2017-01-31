#Author -Wekesa Victor
#import regex library
import re

DATA_FILENAME = "weather.dat"
class WeatherSpread:
    def __init__(self):
        print "This program finds the row with the maximum spread in the weather.dat file, \n where spread is defined as the difference between MxT and MnT \n"
        #logic to open the file and read the contents
        with open(DATA_FILENAME) as fileContents:
        	 #Loop to get values and store them in a list of lists
             lines = [line.split() for line in fileContents]
        # remove empty lists 
        lines2 = filter(None, lines)
        #Get the first 3 columns required to get the maximum spread
        newList = [ [row[0], row[1], row[2]] for row in lines2 ]
        #remove the first row used for column names
        newList.pop(0)
        #remove the last row used for average calculations is not useful for now
        newList.pop(-1)
        # log newList
        #print newList
        newerList = self.calculate_spread(newList)

        # Log
        # print newerList
        # Get the spread
        tempItem = self.get_max_spread_list(newerList)

        # Log
        #print "Got item"
        #print tempItem
        #Log
        #Prints the final result
        print "The day: " + str(tempItem[0]) + " The Spread: " + str(tempItem[-1])
        # print tempItem[0]

        # print "The Spread: "
        # print tempItem[-1]


    # Function to calculate the spread 
    #It also removes special characters and converts string values to float
    def calculate_spread(self,items):
        # Calculate the spread
        return [[item[0], item[1], item[2], float(re.sub('\D', "", item[1]))
          - float(re.sub('\D', "", item[2]))] for item in items]

    # A custom function to get the list with the maximum spread value
    #return a list with maximum spread
    def get_max_spread_list(self,items):
        # Calculate the largest spread and return the list
        return_item = []
        for item in items:
           if len(return_item) < 1:
              return_item = item
           elif return_item[3] > item[3]:
              continue
           else:
              return_item = item
        return return_item
#create an instance of this class
weatherSpread = WeatherSpread()