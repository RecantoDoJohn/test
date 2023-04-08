#the 'sleep' is just to make it mor pretty 
from random import randint
from time import sleep

#variables: kind obvius
numsrt = str(randint(100, 999))
numesc = 0
nmfinal = ('')
x = 0

#this is were magic happens, this can also work with bigger numbers.
while numsrt != nmfinal:
    for i in range (10):
        if str(i) != numsrt[x]:
            print(nmfinal + str(i))
            sleep(0.2)
        else:
            nmfinal += str(i)
            print(nmfinal, 'eche')
            sleep(0.2)
            break

    if numsrt[x] == nmfinal[-1]:
        x += 1
