import json
import puzzles

def loadPuzzle(filename):
    with open('puzzles/' + filename) as json_file:
        data = json.load(json_file)
        puzzle = data['bottles']
        return puzzle


def isValidPuzzle(puzzle): 
    # To check if the puzzle is valid.
    numBottles = len(puzzle)
    bottleHeight = max(len(t) for t in puzzle)
    numWaters = sum(len(t) for t in puzzle)
    numWatersRequired = (numBottles-2)*bottleHeight
    if (numWaters != numWatersRequired):
        print("Puzzle has incorrect number of waters")
        return False
    freq = dict()
    for bottle in puzzle:
        for water in bottle:
            if water not in freq:
                freq[water] = 1
            else:
                freq[water] += 1
    for color,count in freq.items():
        if count != bottleHeight:
            print("Expected "+str(bottleHeight)+" "+color+" waters, found "+str(count))
            return False
    return True

def isSolved(puzzle):
    bottleHeight = max(len(t) for t in puzzle)
    for tube in puzzle:
        if(len(tube) == 0): 
            # There are 2 bottles must be empty when puzzle is solved.
            continue
        elif(len(tube) < bottleHeight):
            # If there is a bottle is not full then the puzzle is not solved.
            return False
        elif(tube.count(tube[0]) != bottleHeight): 
            # If the number of the same color is not equal to bottle's height then the puzzle is not solved.
            return False
    return True

def isMoveValid(bottleHeight, fromBottle, candidateBottle):
    # Move is valid if the source bottle isn't empty, the destination isn't full, 
    # and the water at the end of the source bottle is the same as the water at the end of the destination.
    if len(fromBottle) == 0 or len(candidateBottle) == bottleHeight:
        return False
    numFirstColor = fromBottle.count(fromBottle[0])
    if numFirstColor == bottleHeight: # Bottle is full of same color, don't touch it.
        return False
    if len(candidateBottle) == 0:
        if numFirstColor == len(fromBottle): # Source bottle has all waters with the same color, so pointless moving to empty bottle.
            return False
        return True
    return fromBottle[-1] == candidateBottle[-1]

def printPuzzleToString(puzzle): 
    # To print bottles.
    lines = []
    for bottle in puzzle:
        lines.append(''.join(bottle))
    return("\n".join(lines))

def puzzleToCanonicalString(puzzle):
    bottleStrings = []
    for bottle in puzzle:
        bottleStrings.append(','.join(bottle))
    sortedBottleStrings = sorted(bottleStrings)
    return ';'.join(sortedBottleStrings)
