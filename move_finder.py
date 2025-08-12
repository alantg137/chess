from board_state import *
from move import *
class MoveFinder:
    def find_all(self,b):
        l = []
        for row in range(8,0,-1):
            for col in range(1,9):
                v = b.get(col,row)
                if v == (WHITE,PAWN):
                    m = Move(  (col,row),(col,row + 2)  )
                    l.append(m)
                    m = Move(  (col,row),(col,row + 1)  )
                    l.append(m)
        return l
