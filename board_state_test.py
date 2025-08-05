from board_state import *
b = BoardState()
value = b.get(1,1)
if value != (WHITE,ROOK):
    raise Exception(f' a1 was {value} expected 0')
value = b.get(8,8)
if value != (BLACK,ROOK):
    raise Exception(f' h1 was {value} expected 0')
print(b)


print("succes")
