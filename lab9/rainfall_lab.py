
'''
create two global variables 'rows' and 'cols' and assign the correct values to them
'''

rows = # check csv
cols = # check csv

'''
create a function to initialize and return a suitable 2-d array
'''

def initialize():
    pass # replace pass with your code; refer to Activity 1 for help

'''
the function below reads the contents of the 'rainfall.csv' file, stores its data
into the array, and returns it. this function is complete - please read the comments
carefully. you will need to do something similar in your project.
'''

def readFile(array, filePath):
    # open the external file
    with open(filePath) as rf:
        # store the contents of a line in the file
        line = rf.readline().rstrip('\n')
        # reset row counter
        rowCounter = 0
        # loop until all lines of the data have been read
        while line:
            # split up and store the line data into an array called 'line'
            items = line.split(",")
            # reset the column counter
            colCounter = 0
            # loop through each column
            for col in range(cols):
                # store each column item into the 2D array
                array[rowCounter][colCounter] = int(items[colCounter])
                # increment counter for the next column
                colCounter += 1
            # increment counter for the next row
            rowCounter += 1
            # read and store the next line to be used
            line = rf.readline().rstrip('\n')
        return array

'''
create a procedure called 'yearly' that traverses every row and column of the
array, incrementing a total for the year as it passes through every value
'''

def yearly(array):
    pass # replace pass with your code

'''
create a procedure called 'weekly' that will increment and print the total
amount of rainfall for each week
'''

# your code here

'''
modify 'weekly' so that it also prints the smallest and largest amounts of
rainfall for each week (there should not be a second iteratoin through the array
'''

# your code here


if __name__=="__main__":

    # initialize
    # read file
    # print yearly total
    # print weekly totals, max, min