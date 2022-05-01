#
# Support functions for the 20 Questions problem
#
yesBag = ["Yes", 'yes', 'Y', 'y', 'Yup', 'yup', 'Sure', 'sure']

def printTree(tree, prefix = '', bend = '', answer = ''):
    """Recursively print a 20 Questions tree in a human-friendly form.
       TREE is the tree (or subtree) to be printed.
       PREFIX holds characters to be prepended to each printed line.
       BEND is a character string used to print the "corner" of a tree branch.
       ANSWER is a string giving "Yes" or "No" for the current branch."""
    text, left, right = tree
    if left is None  and  right is None:
        print(f'{prefix}{bend}{answer}It is {text}')
    else:
        print(f'{prefix}{bend}{answer}{text}')
        if bend == '+-':
            prefix = prefix + '| '
        elif bend == '`-':
            prefix = prefix + '  '
        printTree(left, prefix, '+-', "Yes: ")
        printTree(right, prefix, '`-', "No:  ")


def isLeaf(tree): #isAnswer
    text, left, right = tree
    if left is None  and  right is None:
        return True
    
    return False

def yes(prompt):
    ans = input(prompt + "  ") # doesnot consider the space, need to wipe it
    ans = ans.strip()
    if ans in yesBag:
        return True
    return False

def playLeaf(tree):
    if isLeaf(tree):
        ans = yes(tree[0])
        return ans

    text, left, right = tree
    ans = yes(text)
    if ans == True:
        playLeaf(left)
    else:
        playLeaf(right)
    
    return False


def playLeafLearningVersion(tree):
    if isLeaf(tree):
        newTree = tree
        ans = yes(tree[0])
        if ans:
            return newTree
        else:
            trueAns = input("Drats! What was it? ")
            diffQues = input("What's a question that distinguishes between " + trueAns + " and " + tree[0] + "?")
            ans2DiffQuesString = "And what's the answer for " + trueAns + " ?"
            ans2DiffQues = yes(ans2DiffQuesString)

            if ans2DiffQues:
                subNewTree = (diffQues, (trueAns, None, None), tree)
            else:
                subNewTree = (diffQues, tree, (trueAns, None, None))
            
            return subNewTree


    text, left, right = tree
    ans = yes(text)
    if ans == True:
        newLeft = playLeafLearningVersion(left)
        newRight = right
    else:
        newRight = playLeafLearningVersion(right)
        newLeft = left
    
    return (text, newLeft, newRight)


def printTreeLine(tree, file):
    text, left, right = tree
    if left is None  and  right is None:
        file.write("Leaf\n")
        file.write(text + '\n')
    else:
        file.write("Internal node\n")
        file.write(text + '\n')
        printTreeLine(left, file)
        printTreeLine(right, file)

def saveTree(tree, treeFileName):
    with open(treeFileName, "a") as f:
        printTreeLine(tree, f)
    f.close()


def loadTree(treeFileName):
    root = tuple()
    with open(treeFileName, "r") as f:
        line = f.readline()
        if not line:
            print("Not valid Tree! reopen a file!")

        if line.strip() == "Internal node":
            line = f.readline()
            root += (line.strip(), )
            root += (buildTree(f), )
            root += (buildTree(f), )

    return root

def buildTree(f):
    line = f.readline()
    if line.strip() == "Internal node":
        line = f.readline()
        newRoot = tuple()
        newRoot += (line.strip(),)
        newRoot += (buildTree(f),)
        newRoot += (buildTree(f),)
    if line.strip() == "Leaf":
        line = f.readline()
        newRoot = tuple()
        newRoot += (line.strip(),)
        newRoot += ((None), (None), )
    
    return newRoot
