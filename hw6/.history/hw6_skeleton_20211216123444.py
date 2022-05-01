#########################################
##### Name:  Jiaqi Li                       #####
##### Uniqname:   ellali                  #####
#########################################

from hw6_tree import *

#
# The following two trees are useful for testing.
#
smallTree = \
    ("Is it bigger than a breadbox?",
        ("an elephant", None, None),
        ("a mouse", None, None))
mediumTree = \
    ("Is it bigger than a breadbox?",
        ("Is it gray?",
            ("an elephant", None, None),
            ("a tiger", None, None)),
        ("a mouse", None, None))

def main():

    print("Welcome to 20 Questions!")
    playAgain = True
    while playAgain:
        if yes("Would you like to load a tree from a file?"):
            filename = input("What's the name of the file? ")
            startTree = loadTree(filename)
        else:
            startTree = mediumTree
        newTree = play(startTree)
        print("I got it!")
        playAgain = yes("Would you like to play again? ")

    
    if yes("Would you like to save this tree for later? "):
        filename = input("Please enter a file name: ")
        saveTree(newTree, "filename")
        print("Thank you!  The file has been saved.")
    
    print("In case I don't see you, good afternoon, good evening, and good night!")


    # Write the "main" function for 20 Questions here.  Although
    # main() is traditionally placed at the top of a file, it is the
    # last function you will write.

def simplePlay(tree):
    return playLeaf(tree)

def play(tree):
    return playLeafLearningVersion(tree)
    
#
# The following two-line "magic sequence" must be the last thing in
# your file.  After you write the main() function, this line it will
# cause the program to automatically play 20 Questions when you run
# it.
#
if __name__ == '__main__':
    main()
