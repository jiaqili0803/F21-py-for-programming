
#############################

rows = 296
cols = 3


def initialize():
    return [[None]*cols for x in range(rows)]








def readFile(this_file):
    # open the external file
    with open(this_file) as f:
    data = list(csv.reader(csvfile))
    print(data)

