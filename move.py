class Move:
    def __init__(self,start,end):
        self._start = start
        self._end = end
    def pos1(self):
        return self._start
    def pos2(self):
        return self._end

