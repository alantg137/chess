from move_finder import *
from board_state import *
from move import *
b = BoardState()
move_finder = MoveFinder()
value = move_finder.find_all(b, WHITE)
m = Move.parse("e2e4")
if not (m in value):
    raise Exception(f'm was not in {" ".join(map(str, value))}')
m = Move.parse("e1e8")
if m in value:
    raise Exception(f'm is an illegal move')
m = Move.parse("e2e3")
if not (m in value):
    raise Exception(f'm was actually not in {" ".join(map(str, value))}')
b.set(5,3,(BLACK,PAWN))
m = Move.parse("e2e3")
value = move_finder.find_all(b, WHITE)
if m in value:
    raise Exception(f'm is not an legal move')
print(" ".join(map(str, value)))

b.set(5,6,(WHITE,PAWN))
print(b)
m = Move.parse("e7e5")
value = move_finder.find_all(b, BLACK)
if m in value:
    raise Exception(f'm is not an legal move')


print("success")

