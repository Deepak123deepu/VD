


"""

 hep mem -> | a | -> add(325718688)


bitwise opr -> (and, or, not)




task 1:

number -> 
check if that number is div by 3 
    -> deep 
check if that number is div by 5    
    -> jeep
both 
    -> deep jeep



task 2 :

userinout -> cir 

cir,      rec,       sq
radus     len,brth   side len 
pi(r*r)   


"""


import math 



onTable1 = "apple"
onTable2 = "org"
    # condi expree (ope)
if onTable1 == "apple":
    print("you need to clean the room")
    if onTable2 == "org":
        print("you need to pay my rent")
    else:
        print("i will pay your rent")
else:
    print("i will buy apples for you")


if onTable1 == "apple":
    print("you need to clean the room")
elif onTable2 == "org":
        print("you need to pay my rent")
else:
    print("i will buy apples for you and i will pay your rent")



if onTable1 == "apple" and onTable2 == "org":
    print("you need to clean the room and you need to pay my rent")
else:
    print("i will buy apples for you and i will pay your rent")





"""

 loops 

  - conter var (iter)
  - cond (false statem)
  - incre / decre


1   2   3    4     5   6   7   8   9   10
lr      l          r       l        r      

"""

# for ( i =1   ; i<10   ; i--   )

for i in range(1, 11, 2):
    print(i, end = " ")


i = 0 # conter var
while i <= 11: # conde 0 le 11 
    print(i)
    # i = i + 1  # incre / decre 
    i += 1 











