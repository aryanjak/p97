import random
r = random.randint(1,10)
chance = 4

while(chance > 0):
    g = int(input("Enter Your Guess : "))
    if g == r:
        print("Congo!! You WON!!&^")
        break
    chance = chance-1

if chance <= 0 :
    print("You Lost!!:) HEHE!! The number is :::" , r , ":::")
    
   

