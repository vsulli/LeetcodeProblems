numBottles = 9
numExchange = 3
max_drinks = 0


max_drinks = numBottles

while numBottles % numExchange == 0:
    max_drinks += numBottles // numExchange
    numBottles = numBottles // numExchange

print(max_drinks)



