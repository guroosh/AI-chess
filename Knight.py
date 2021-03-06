from Piece import Piece, encoded


def isDestinationEmpty(board, fromX, fromY, toX, toY):
    piece_name = board.getPiece(fromX, fromY)
    piece_name1 = board.getPiece(toX, toY)
    if piece_name1[0] == '.':
        return True
    if piece_name[0] is not piece_name1[0]:
        return True
    return False


class Knight(Piece):
    def __init__(self, name, moved):
        super().__init__(name, moved)

    def isValid(self, board, fromX, fromY, toX, toY):
        if not super().isValid(board, fromX, fromY, toX, toY):
            return False

        if abs(toX - fromX) == 2:
            if abs(toY - fromY) is not 1:
                return False
            else:
                if isDestinationEmpty(board, fromX, fromY, toX, toY):
                    return True
                else:
                    return False
        elif abs(toX - fromX) == 1:
            if abs(toY - fromY) is not 2:
                return False
            else:
                if isDestinationEmpty(board, fromX, fromY, toX, toY):
                    return True
                else:
                    return False
        else:
            return False

    def getPossibleMoves(self, board, color, i, j):
        ret_list = []
        physical_moves = []
        move = encoded(i, j, i - 1, j - 2)
        physical_moves.append(move)
        move = encoded(i, j, i - 2, j - 1)
        physical_moves.append(move)
        move = encoded(i, j, i + 1, j + 2)
        physical_moves.append(move)
        move = encoded(i, j, i + 2, j + 1)
        physical_moves.append(move)
        move = encoded(i, j, i - 1, j + 2)
        physical_moves.append(move)
        move = encoded(i, j, i - 2, j + 1)
        physical_moves.append(move)
        move = encoded(i, j, i + 1, j - 2)
        physical_moves.append(move)
        move = encoded(i, j, i + 2, j - 1)
        physical_moves.append(move)
        if color == 'B':
            turn = 'BLACK'
        else:
            turn = 'WHITE'
        for m in physical_moves:
            from Move import Move
            move = Move(m)
            if move.isValidRule(board, turn):
                ret_list.append(move.coded)
        return ret_list
