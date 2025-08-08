from move import *
m = Move(  (5,2), (5,4) )
value = m.pos1()
if value != (5,2):
    raise Exception(f"start was {value}")
value = m.pos2()
if value != (5,4):
    raise Exception(f"end was {value}")



print("success")
