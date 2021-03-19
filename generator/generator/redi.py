def RotateArray(matrice, i):
    # This function allow to rotate a face of the cube (3x3) by 90° clockwise and i time
    if i != 0:
        copy = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for j in range(i):
        for x in range(len(copy)):
            for y in range(len(copy[x])):
                copy[x][y] = matrice[2 - y][x]
        for x in range(len(copy)):
            for y in range(len(copy[x])):
                matrice[x][y] = copy[x][y]
    return matrice


class Redi():
    def __init__(self, matrice=0):
        # if matrice is not define, we return a fully 'finished' cube.
        # color code : R for red, W for white, O for orange, Y for yellow, G for green, B for blue
        if matrice == 0:
            matrice = []
            for i in ('W', 'O', 'Y', 'R', 'G', 'B'):
                matrice.append([[i, i, i], [i, 'X', i], [i, i, i]])
        self.cube = matrice

    def _print(self):
        for i in range(len(self.cube)):
            print(f"Side number {i}")
            for j in range(len(self.cube[i])):
                x = 2 - j
                print(self.cube[i][0][x] + ' ' + self.cube[i][1][x] + ' ' + self.cube[i][2][x])

    def rotate(self, side, y, z):
        """
        to change a cube, you need to param the info about the corner to rotate : on which side it is located,
        we always talk about the right-hand corner.
        :param side: 0,1,2 or 3. it define on which face of the redik the corner we want to rotate is located on
        :param y: up or down, it define the location of the corner we want to move
        :param z: 1 or -1, it define in wich way we rotate the corner. 1 is clockwise and -1 is reverse
        """
        if (y == 'up'):
            nextside = (side + 1) % 4
            # we rotate the top side relatively to the side the corner we want to rotate is on
            # we will rotate the top side back after having rotated the corner
            topside = 4
            self.cube[topside] = RotateArray(self.cube[topside], side)

            if (z == 1):

                # first let's swap the corner piece
                a = self.cube[side][2][2]
                self.cube[side][2][2] = self.cube[nextside][0][2]
                self.cube[nextside][0][2] = self.cube[topside][2][0]
                self.cube[topside][2][0] = a

                # secondly we swap the middle righ piece
                a = self.cube[side][2][1]
                self.cube[side][2][1] = self.cube[nextside][1][2]
                self.cube[nextside][1][2] = self.cube[topside][1][0]
                self.cube[topside][1][0] = a

                # to finish we swap the middle top piece
                a = self.cube[side][1][2]
                self.cube[side][1][2] = self.cube[nextside][0][1]
                self.cube[nextside][0][1] = self.cube[topside][2][1]
                self.cube[topside][2][1] = a

            elif (z == -1):

                # first let's swap the corner piece
                a = self.cube[nextside][0][2]
                self.cube[nextside][0][2] = self.cube[side][2][2]
                self.cube[side][2][2] = self.cube[topside][2][0]
                self.cube[topside][2][0] = a

                # secondly we swap the middle righ piece
                a = self.cube[nextside][1][2]
                self.cube[nextside][1][2] = self.cube[side][2][1]
                self.cube[side][2][1] = self.cube[topside][1][0]
                self.cube[topside][1][0] = a

                # to finish we swap the middle top piece
                a = self.cube[nextside][0][1]
                self.cube[nextside][0][1] = self.cube[side][1][2]
                self.cube[side][1][2] = self.cube[topside][2][1]
                self.cube[topside][2][1] = a

            # we rotate back the top side
            self.cube[topside] = RotateArray(self.cube[topside], 4 - side)

        if y == 'down':
            nextside = (side + 1) % 4
            # we rotate the bpt side relatively to the side the corner we want to rotate is on
            # we will rotate the bot side back after having rotated the corner
            botside = 5
            self.cube[botside] = RotateArray(self.cube[botside], 4 - side)

            if z == 1:
                # first let's swap the corner piece
                a = self.cube[nextside][0][0]
                self.cube[nextside][0][0] = self.cube[side][2][0]
                self.cube[side][2][0] = self.cube[botside][2][2]
                self.cube[botside][2][2] = a

                # secondly we swap the middle righ piece
                a = self.cube[nextside][1][0]
                self.cube[nextside][1][0] = self.cube[side][2][1]
                self.cube[side][2][1] = self.cube[botside][1][2]
                self.cube[botside][1][2] = a

                # to finish we swap the middle bottom piece
                a = self.cube[nextside][0][1]
                self.cube[nextside][0][1] = self.cube[side][1][0]
                self.cube[side][1][0] = self.cube[botside][2][1]
                self.cube[botside][2][1] = a

            if z == -1:
                # first let's swap the corner piece
                a = self.cube[side][2][0]
                self.cube[side][2][0] = self.cube[nextside][0][0]
                self.cube[nextside][0][0] = self.cube[botside][2][2]
                self.cube[botside][2][2] = a

                # secondly we swap the middle righ piece
                a = self.cube[side][2][1]
                self.cube[side][2][1] = self.cube[nextside][1][0]
                self.cube[nextside][1][0] = self.cube[botside][1][2]
                self.cube[botside][1][2] = a

                # to finish we swap the middle bottom piece
                a = self.cube[side][1][0]
                self.cube[side][1][0] = self.cube[nextside][0][1]
                self.cube[nextside][0][1] = self.cube[botside][2][1]
                self.cube[botside][2][1] = a

            # we rotate back the bot side
            self.cube[botside] = RotateArray(self.cube[botside], side)