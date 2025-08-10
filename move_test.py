from move import *
m = Move(  (5,2), (5,4) )
value = m.pos1()
if value != (5,2):
    raise Exception(f"start was {value}")
value = m.pos2()
if value != (5,4):
    raise Exception(f"end was {value}")
value = str(m)
if str(m) !=  "e2e4":
    raise Exception(f"str(m) was {value}")
m = Move.parse("d2d4")
value = m.pos1()
if value != (4, 2):
    raise Exception(f"parse(m) was {value}")
value = m.pos2()
if value != (4, 4):
    raise Exception(f"parse(m) was {value}")



print("success")
