from rule_book import *
from move import *
r = RuleBook()
m = Move( 2,2 ), ( 2,4 )
value = r.legal(m)
if value != True:
    raise Exception(f' m is {value}')




print("success")
