WHITE = 1
BLACK = 2
EMPTY = 0
PAWN = 15
KNIGHT = 14
BISHOP = 13
ROOK = 12
QUEEN = 11
KING = 10
class BoardState():
    def get(self,col,row):
        return self.state[(row-1) * 8 + col - 1]
    def __init__(self):
        self.state = [(EMPTY,EMPTY)] * 64
        self.state[0] = (WHITE,ROOK)
        self.state[1] = (WHITE,KNIGHT)
        self.state[2] = (WHITE,BISHOP)
        self.state[3] = (WHITE,QUEEN)
        self.state[4] = (WHITE,KING)
        self.state[5] = (WHITE,BISHOP)
        self.state[6] = (WHITE,KNIGHT)
        self.state[7] = (WHITE,ROOK)

        self.state[8] = (WHITE,PAWN)
        self.state[9] = (WHITE,PAWN)
        self.state[10] = (WHITE,PAWN)
        self.state[11] = (WHITE,PAWN)
        self.state[12] = (WHITE,PAWN)
        self.state[13] = (WHITE,PAWN)
        self.state[14] = (WHITE,PAWN)
        self.state[15] = (WHITE,PAWN)

        self.state[48] = (BLACK,PAWN)
        self.state[49] = (BLACK,PAWN)
        self.state[50] = (BLACK,PAWN)
        self.state[51] = (BLACK,PAWN)
        self.state[52] = (BLACK,PAWN)
        self.state[53] = (BLACK,PAWN)
        self.state[54] = (BLACK,PAWN)
        self.state[55] = (BLACK,PAWN)

        self.state[56] = (BLACK,ROOK)
        self.state[57] = (BLACK,KNIGHT)
        self.state[58] = (BLACK,BISHOP)
        self.state[59] = (BLACK,QUEEN)
        self.state[60] = (BLACK,KING)
        self.state[61] = (BLACK,BISHOP)
        self.state[62] = (BLACK,KNIGHT)
        self.state[63] = (BLACK,ROOK)
    def __str__(self):
        s = ""
        for row in range(8,0,-1):
            s = s + f"{row} "
            bl = "\033[30m"
            wh = "\033[97m"
            for col in range(1,9):
                v = self.get(col,row)

                if(row + col) %2:
                    s += "\033[100m"
                else:
                    s += "\033[44m"

                if v == (WHITE,ROOK):
                    s = s + wh + "♖"
                if v == (WHITE,KNIGHT):
                    s = s +  wh + "♘"
                if v == (WHITE,BISHOP):
                    s = s + wh +"♗"
                if v == (WHITE,QUEEN):
                    s = s + wh +"♕"
                if v == (WHITE,KING):
                    s = s + wh +"♔"
                if v == (WHITE,PAWN):
                    s = s + wh + "♙"
                if v == (EMPTY,EMPTY):
                    s = s + " "
                if v == (BLACK,ROOK):
                    s = s + bl + "♜"
                if v == (BLACK,KNIGHT):
                    s = s +bl + "♞"
                if v == (BLACK,BISHOP):
                    s = s +bl + "♝"
                if v == (BLACK,QUEEN):
                    s = s + bl + "♛"
                if v == (BLACK,KING):
                    s = s + bl + "♚"
                if v == (BLACK,PAWN):
                    s = s + bl + "♙"
                s = s + " "
            s = s + "\033[0m\n"
        return s
