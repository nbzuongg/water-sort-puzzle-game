import argparse
import copy
import time
import someConditions



def solvePuzzle(puzzle, bottleHeight=None, visitedPositions=set(), answer=[]):
    if bottleHeight is None:
        bottleHeight = max(len(t) for t in puzzle)
    # visitedPositions keeps track of all the states of the grid we have considered
    # to make sure we don't go round in circles
    # canonical (ordered) string representation of the grid means
    # that two grids that differ only by the order of the tubes are
    # considered as the same position
    visitedPositions.add(someConditions.puzzleToCanonicalString(puzzle))
    for i in range(len(puzzle)):
        bottle = puzzle[i]
        for j in range(len(puzzle)):
            if i == j:
                continue
            candidateBottle = puzzle[j]
            if someConditions.isMoveValid(bottleHeight, bottle, candidateBottle):
                grid2 = copy.deepcopy(puzzle)
                grid2[j].append(grid2[i].pop())
                if(someConditions.isSolved(grid2, bottleHeight)):
                    answer.append(someConditions.printPuzzleToString(grid2))
                    return True
                if(someConditions.puzzleToCanonicalString(grid2) not in visitedPositions):
                    solved = solvePuzzle(grid2, bottleHeight, visitedPositions, answer)
                    if solved:
                        answer.append(someConditions.printPuzzleToString(grid2))
                        return True
    return False



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="(Attempt to) solve a water sort puzzle")
    parser.add_argument("json",help="filename of input file (in JSON format)")
    parser.add_argument("--show-working", dest="working", help="Print out the steps to the solution", action='store_true')
    args = parser.parse_args()
    puzzle = someConditions.loadPuzzle(args.json)
    start = time.time()
    if not someConditions.isValidPuzzle(puzzle):
        exit("Invalid puzzle")
    if someConditions.isSolved(puzzle):
        print("Puzzle is already solved")
        exit()
    print(someConditions.printPuzzleToString(puzzle))
    print("--")
    answer = []
    visitedPositions = set()
    solved = solvePuzzle(puzzle, visitedPositions=visitedPositions, answer=answer)
    end = time.time()
    print("Visited "+str(len(visitedPositions))+" positions in "+str(round(end-start, 3))+" seconds")
    if not solved:
        print("No solution")
    else:
        print("Solved in "+str(len(answer))+" moves")
        if(args.working):
            answer.reverse()
            for step in answer:
                print(step)
                print('--')



