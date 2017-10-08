from Spot import Spot

# done
class Board:
    w = 8
    h = 8
    spots = [[0 for x in range(8)] for y in range(8)]

    def __init__(self):
        for i in range(self.h):
            for j in range(self.w):
                self.spots[i][j] = Spot(i, j, '.')

    def getSpot(self, x, y):
        return self.spots[x][y]

    def printBoard(self):
        for i in range(self.h):
            print(8 - i, '\t', end='')
            for j in range(self.w):
                piece = self.spots[i][j].piece
                if piece.name == '.':
                    print(u'\uFE63' + '\t', end='')
                else:
                    print(piece.unicode() + '\t', end='')
            print()
        print(u'\t\u0041\t\u0042\t\u0043\t\u0044\t\u0045\t\u0046\t\u0047\t\u0048')

        # for i in range(self.h):
        #     print(8 - i, '\t', end='')
        #     for j in range(self.w):
        #         piece = self.spots[i][j].piece
        #         if piece.name == '.':
        #             print(u'\uFE63' + '\t', end='')
        #         else:
        #             print(str(piece.moved) + '\t', end='')
        #     print()
        # print(u'\t\u0041\t\u0042\t\u0043\t\u0044\t\u0045\t\u0046\t\u0047\t\u0048')

    def getPiece(self, x, y):
        # print(self.spots[x][y].piece.name)
        return self.spots[x][y].piece.name

    def getPieceObject(self, x, y):
        return self.spots[x][y].piece

    def isSpotVacant(self, x, y):
        if self.spots[x][y].piece.name == '.':
            return True
        return False

    def isSpotOfSameTeam(self, x1, y1, x2, y2):
        if self.spots[x1][y1].piece.name[0] == self.spots[x2][y2].piece.name[0]:
            return True
        return False

    def isChecked(self, color, x, y):
        if color == 'W':
            adver = 'B'
        else:
            adver = 'W'

        # by pawn
        try:
            p1 = self.spots[x - 1][y - 1].piece.name
        except IndexError:
            p1 = '.'
        try:
            p2 = self.spots[x - 1][y + 1].piece.name
        except IndexError:
            p2 = '.'
        if p1 == adver + 'pawn' or p2 == adver + 'pawn':
            return True

        # by knight
        try:
            p1 = self.spots[x - 1][y - 2].piece.name
        except IndexError:
            p1 = '.'
        try:
            p2 = self.spots[x - 1][y + 2].piece.name
        except IndexError:
            p2 = '.'
        try:
            p3 = self.spots[x + 1][y - 2].piece.name
        except IndexError:
            p3 = '.'
        try:
            p4 = self.spots[x + 1][y + 2].piece.name
        except IndexError:
            p4 = '.'
        try:
            p5 = self.spots[x - 2][y - 1].piece.name
        except IndexError:
            p5 = '.'
        try:
            p6 = self.spots[x - 2][y + 1].piece.name
        except IndexError:
            p6 = '.'
        try:
            p7 = self.spots[x + 2][y - 1].piece.name
        except IndexError:
            p7 = '.'
        try:
            p8 = self.spots[x + 2][y + 1].piece.name
        except IndexError:
            p8 = '.'
        if p1 == adver + 'knight' or p2 == adver + 'knight' or p3 == adver + 'knight' \
                or p4 == adver + 'knight' or p5 == adver + 'knight' or p6 == adver + 'knight' \
                or p7 == adver + 'knight' or p8 == adver + 'knight':
            return True

        # by king
        try:
            p1 = self.spots[x - 1][y - 1].piece.name
        except IndexError:
            p1 = '.'
        try:
            p2 = self.spots[x - 1][y + 1].piece.name
        except IndexError:
            p2 = '.'
        try:
            p3 = self.spots[x - 1][y].piece.name
        except IndexError:
            p3 = '.'
        try:
            p4 = self.spots[x + 1][y].piece.name
        except IndexError:
            p4 = '.'
        try:
            p5 = self.spots[x + 1][y - 1].piece.name
        except IndexError:
            p5 = '.'
        try:
            p6 = self.spots[x + 1][y + 1].piece.name
        except IndexError:
            p6 = '.'
        try:
            p7 = self.spots[x][y - 1].piece.name
        except IndexError:
            p7 = '.'
        try:
            p8 = self.spots[x][y + 1].piece.name
        except IndexError:
            p8 = '.'
        if p1 == adver + 'king' or p2 == adver + 'king' or p3 == adver + 'king' \
                or p4 == adver + 'king' or p5 == adver + 'king' or p6 == adver + 'king' \
                or p7 == adver + 'king' or p8 == adver + 'king':
            return True

        # by rook/queen
        i = x - 1
        j = y
        while i >= 0:
            p = self.spots[i][j].piece.name
            if p == adver + 'rook' or p == adver + 'queen':
                return True
            elif not p == '.':
                break

            i = i - 1
        i = x + 1
        j = y
        while i <= 7:
            p = self.spots[i][j].piece.name
            if p == adver + 'rook' or p == adver + 'queen':
                return True
            elif not p == '.':
                break
            i = i + 1
        i = x
        j = y - 1
        while j >= 0:
            p = self.spots[i][j].piece.name
            if p == adver + 'rook' or p == adver + 'queen':
                return True
            elif not p == '.':
                break
            j = j - 1
        i = x
        j = y + 1
        while j <= 7:
            p = self.spots[i][j].piece.name
            if p == adver + 'rook' or p == adver + 'queen':
                return True
            elif not p == '.':
                break
            j = j + 1

        # by bishop/queen
        i = x - 1
        j = y - 1
        while i >= 0 and j >= 0:
            p = self.spots[i][j].piece.name
            if p == adver + 'bishop' or p == adver + 'queen':
                return True
            elif not p == '.':
                break
            i = i - 1
            j = j - 1
        i = x + 1
        j = y - 1
        while i <= 7 and j >= 0:
            p = self.spots[i][j].piece.name
            if p == adver + 'bishop' or p == adver + 'queen':
                return True
            elif not p == '.':
                break
            i = i + 1
            j = j - 1
        i = x - 1
        j = y + 1
        while i >= 0 and j <= 7:
            p = self.spots[i][j].piece.name
            if p == adver + 'bishop' or p == adver + 'queen':
                return True
            elif not p == '.':
                break
            i = i - 1
            j = j + 1
        i = x + 1
        j = y + 1
        while i <= 7 and j <= 7:
            p = self.spots[i][j].piece.name
            if p == adver + 'bishop' or p == adver + 'queen':
                return True
            elif not p == '.':
                break
            i = i + 1
            j = j + 1

        return False

    def analyse(self):
        pass

    def init(self, color):
        if color == 'B':
            opponent_color = 'W'
            special = {0: 'rook', 1: 'knight', 2: 'bishop', 3: 'queen', 4: 'king', 5: 'bishop', 6: 'knight', 7: 'rook'}
        else:
            opponent_color = 'B'
            special = {0: 'rook', 1: 'knight', 2: 'bishop', 3: 'king', 4: 'queen', 5: 'bishop', 6: 'knight', 7: 'rook'}
        for i in range(self.h):
            self.spots[7][i] = Spot(0, i, opponent_color + special[i])
            self.spots[6][i] = Spot(1, i, opponent_color + 'pawn')
            self.spots[0][i] = Spot(0, i, color + special[i])
            self.spots[1][i] = Spot(1, i, color + 'pawn')

    def updateBoard(self, move):
        move = str(move)
        x1 = move[0]
        y1 = move[1]
        x2 = move[2]
        y2 = move[3]
        x1 = x1.upper()
        x2 = x2.upper()
        x1 = ord(x1)
        y1 = int(y1)
        x2 = ord(x2)
        y2 = int(y2)
        x1 = x1 - 65
        y1 = 8 - y1
        x2 = x2 - 65
        y2 = 8 - y2
        x1, y1 = y1, x1
        x2, y2 = y2, x2

        self.spots[x2][y2] = Spot(x2, y2, self.spots[x1][y1].piece.name, True)
        self.spots[x1][y1] = Spot(x1, y1, '.')
