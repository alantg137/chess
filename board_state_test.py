from board_state import *
from move import *

b = BoardState()
value = b.get(1,1)
if value != (WHITE,ROOK):
    raise Exception(f' a1 was {value} expected 0')

value = b.get(8,8)
if value != (BLACK,ROOK):
    raise Exception(f' h1 was {value} expected 0')
print(b)

b.set( 4, 4, (WHITE,PAWN) )
value = b.get(4,4)
if value != (WHITE,PAWN):
    raise Exception(f' d4 was {value} expected (WHITE,PAWN)')
b.set(4, 4, (EMPTY,EMPTY))


m = Move(  (2,1), (3,3) )
b2 = b.move(m)
value = b2.get(3,3)
if value != (WHITE,KNIGHT):
    raise Exception(f' c3 was {value} expected (WHITE,KNIGHT)')
print(b2)
print("success")
