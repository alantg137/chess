from move import *
from board_state import *
b = BoardState()
while True:
    print("white's move")
    x = input()
    move = Move.parse(x)
    b.move(move)
    print(b)
    print("black's move")
    x = input()
    move = Move.parse(x)
    b.move(move)
    print(b)
