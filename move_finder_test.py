from move_finder import *
from board_state import *
from move import *
b = BoardState()
move_finder = MoveFinder()
value = move_finder.find_all(b)
m = Move.parse("e2e4")
if not (m in value):
    raise Exception(f'm was not in {" ".join(map(str, value))}')
m = Move.parse("e1e8")
if m in value:
    raise Exception(f'm is an illegal move')
m = Move.parse("e2e3")
if not (m in value):
    raise Exception(f'm was not in {" ".join(map(str, value))}')




print("success")
