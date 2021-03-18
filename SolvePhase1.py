from RediClass import Redi


def SolverFirstPartBlue(Redi):
    """
    this function return a list of move.
    It solve the 4 corner of the blue side which is the bottom side
    """
    move = []
    for i, [x, y] in enumerate([[2, 2], [2, 0], [0, 0], [0, 2]]):
        while Redi.cube[5][x][y] != 'B':
            Redi.rotate(i, 'down', 1)
            move.append([i, 'down', 1])
    return move


def SolveSecondPart(Redi):
    """
    this function return a list of move
    it solve all the blue side which is the bottome side
    """
    move = []
    color = ['W', 'O', 'Y', 'R']
    # this for loop, loops trought all pieces that are not corner.
    while Redi.cube[5] != [['B', 'B', 'B'], ['B', 'X', 'B'], ['B', 'B', 'B']]:
        for i, [x, y] in enumerate([[1, 2], [2, 1], [1, 0], [0, 1]]):
            # lets check the piece is not already is place
            print(f"for color {color[i]}")
            if Redi.cube[i][1][0] != color[i] or Redi.cube[5][x][y] != 'B':

                # check if the piece we need is in the medium row
                for side in [0, 1, 2, 3]:
                    if Redi.cube[side][2][1] in [color[i], 'B'] and Redi.cube[(side + 1) % 4][0][1] in [color[i], 'B']:

                        # let's rotate the top right corner of this side clockwise
                        Redi.rotate(side, 'up', 1)
                        move.append([side, 'up', 1])

                # if not correctly place but on the top layer, lets put it back on the medium layer
                for side, [a, b] in enumerate([[1, 0], [2, 1], [1, 2], [0, 1]]):
                    if Redi.cube[side][1][2] in [color[i], 'B'] and Redi.cube[4][a][b] in [color[i], 'B']:

                        if side == i:
                            # let's place the piece
                            Redi.rotate(side, 'down', 1)
                            move.append([side, 'down', 1])

                            Redi.rotate(side, 'up', -1)
                            move.append([side, 'up', -1])

                            Redi.rotate(side, 'down', -1)
                            move.append([side, 'down', -1])
                            continue

                        # let's rotate the top left corner of this side counter-clockwise
                        Redi.rotate((side - 1) % 4, 'up', -1)
                        move.append([(side - 1) % 4, 'up', -1])

    return move

    # CHECK IF DONE IS CORRECTLY PLACE

def SolveStep1(Redi):
    a = SolverFirstPartBlue(Redi)
    Redi._print()
    b = SolveSecondPart(Redi)
    return a+b