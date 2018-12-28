import sys

# define class point, containing:
# x-position
# y-position
# occupied with a stone or not
class Point(object):
    def __init__(self, xPosition, yPosition, occupied):
        self.xPosition = xPosition
        self.yPosition = yPosition
        self.occupied = occupied

# define placeStone function, which player uses to place a stone
def placeStone(x, y):
    # TODO
    return 0

# define main play function
def singlePlayerPlay():
    # initialize 2-d array of points to make the board (19 x 19
    # classic Go board)
    board = []
    for x in range(19):
        board.append([])
        for y in range(19):
            board[x].append(Point(x, y, False))
    print()
    print('Welcome to Andrew\'s Go Engine! Give the coordinates for your next move below: ')
    print('Type your x, then y-coordinate that you would like to place a stone in.')
    print()
    # game state
    gameOver = False
    # while the game is not over yet, keep allowing the player to input
    # x and y coordinates for their stones
    while gameOver == False:
        # get their input
        nextMove = input('Format: "x y" (without parentheses) > ')
        # check if that input is valid
        if len(nextMove.split(' ')) != 2: #or nextMove.split(' ')[0].isdigit() == False or nextMove.split(' ')[1].isdigit() == False:
            print('Sorry, please give an x then a y in the format below (these must be integers).')
            continue
        xMove = int(nextMove.split(' ')[0])
        yMove = int(nextMove.split(' ')[1])
        if xMove > 18 or xMove < 0:
            print('Please enter a number from 0 through 18 for your x position.')
            continue
        if yMove > 18 or yMove < 0:
            print('Please enter a number from 0 through 18 fo your y position.')
            continue
        if board[xMove][yMove].occupied == True:
            print('Sorry, that spot is occupied! Try another position.')
            continue
        # TODO: test for at least 1 liberty
        # Now that we know input is valid, we can change the occupied field in
        # the appropriate x and y position on the board point class array
        # to True
        print('Moved a stone onto position {}, {}.'.format(xMove, yMove))
        board[xMove][yMove].occupied = True

if __name__ == '__main__':
    singlePlayerPlay()
