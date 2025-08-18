from board_state import *
from move import *

class MoveFinder:
    def find_all(self,b,color):

        l = []
        if color == BLACK:
            dir = -1
            pawn_row = 7
        else:
            dir = 1
            pawn_row = 2
        for row in range(8,0,-1):
            for col in range(1,9):
                v = b.get(col,row)
                if v == (color,PAWN):
                    if b.get((col),(row + dir)) == (EMPTY,EMPTY):
                        m = Move(  (col,row),(col,row + dir)  )
                        l.append(m)
                        if row == pawn_row:
                            if b.get((col),(row + 2 * dir)) == (EMPTY,EMPTY):
                                m = Move(  (col,row),(col,row + 2 * dir)  )
                                l.append(m)
        return l
