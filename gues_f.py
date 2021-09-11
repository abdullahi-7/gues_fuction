import random
#abdullahi, 10, kenya

def gues():
    v = int(input("gues a number? "))
    var = random.randint(1,4) 
    if v != var:
        print("wrong")