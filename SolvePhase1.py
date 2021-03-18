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
    stuck_counter = 0
    # this for loop, loops trought all pieces that are not corner.
    while Redi.cube[5] != [['B', 'B', 'B'], ['B', 'X', 'B'], ['B', 'B', 'B']]:

        stuck_counter += 1

        for i, [x, y] in enumerate([[1, 2], [2, 1], [1, 0], [0, 1]]):
            # lets check the piece is not already is place
            print(f"for color {color[i]}")
            if Redi.cube[i][1][0] != color[i] or Redi.cube[5][x][y] != 'B':
                print('not fit')

                piece_in_bottom = False
                while not piece_in_bottom:
                    piece_in_bottom = True

                    # check if the piece we need is in the medium row
                    for side in [0, 1, 2, 3]:
                        if Redi.cube[side][2][1] in [color[i], 'B'] and Redi.cube[(side + 1) % 4][0][1] in [color[i],
                                                                                                            'B']:
                            piece_in_bottom = False
                            print('bingo midlle')
                            print(Redi.cube[side][2][1])
                            print(Redi.cube[(side + 1) % 4][0][1])
                            print(side)

                            # let's rotate the top right corner of this side clockwise
                            Redi.rotate(side, 'up', 1)
                            move.append([side, 'up', 1])

                    # if not correctly place but on the top layer, lets put it back on the medium layer
                    for side, [a, b] in enumerate([[1, 0], [2, 1], [1, 2], [0, 1]]):
                        if Redi.cube[side][1][2] in [color[i], 'B'] and Redi.cube[4][a][b] in [color[i], 'B']:

                            piece_in_bottom = False

                            if side == i:
                                print('parfaitement placé')
                                # let's place the piece
                                Redi.rotate(side, 'down', 1)
                                move.append([side, 'down', 1])

                                Redi.rotate(side, 'up', -1)
                                move.append([side, 'up', -1])

                                Redi.rotate(side, 'down', -1)
                                move.append([side, 'down', -1])
                                continue

                            print('bingo bingo top')
                            print(Redi.cube[side][1][2])
                            print(Redi.cube[4][a][b])
                            print(side)

                            # let's rotate the top left corner of this side counter-clockwise
                            Redi.rotate((side - 1) % 4, 'up', -1)
                            move.append([(side - 1) % 4, 'up', -1])
                Redi._print()
            elif stuck_counter > 100 and Redi.cube[5][x][y] != 'B':
                print('is stuck')
                print(f" x: {x} y: {y}")
                Redi.rotate(i, 'down', 1)
                move.append([i, 'down', 1])

                Redi.rotate(i, 'up', 1)
                move.append([i, 'up', 1])

                Redi.rotate(i, 'down', -1)
                move.append([i, 'down', -1])

    return move

def ReduceMove(list):
    for x in range(5):
        for i in range(len(list)-1):
            if list[i] == list[i+1]:
                list.pop(i+1)
                if list[i][2] == 1:
                    list[i][2] = -1
                elif list[i][2] == -1:
                    list[i][2]= 1
                break
    return list


def SolveStep1(Redi):
    a = SolverFirstPartBlue(Redi)
    Redi._print()
    b = SolveSecondPart(Redi)

    print(a + b)
    c = ReduceMove(a + b)
    print(c)
    return c