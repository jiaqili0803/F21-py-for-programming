rows = 296
cols = 3


def initialize():
    return [[None]*cols for x in range(rows)]

def readFile():
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