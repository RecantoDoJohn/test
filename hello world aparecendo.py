from time import sleep

alfa = ' abcdefghijklmnopqrstuvwxyz'
numsrt = 'hello world'
nmfinal = ('')
x = 0

while numsrt != nmfinal:
    for letra in alfa:
        if letra != numsrt[x]:
            print(nmfinal + letra)
            sleep(0.05)
        else:
            nmfinal += letra
            print(nmfinal)
            sleep(0.05)
            break

    if numsrt[x] == nmfinal[-1]:
        x += 1
        