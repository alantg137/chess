class Move:
    def __init__(self,start,end):
        self._start = start
        self._end = end
    def pos1(self):
        return self._start
    def pos2(self):
        return self._end
    def __str__(self):
        return(f"{chr(self.pos1()[0]+96)}{self.pos1()[1]}{chr(self.pos2()[0]+96)}{self.pos2()[1]}")
    def parse(s):
        m = Move((ord(s[0])-96,int(s[1])), (ord(s[2])-96,int(s[3])))
        return m
    def __eq__(self,other):
        return self.pos1() == other.pos1() and self.pos2() == other.pos2()
