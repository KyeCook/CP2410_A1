from time import clock
import random

for q in range(3,9):
    print("")
    n = 10**q
    print("n: " + n)
    array = [None]*n
    Ms = []
    for f in range(0,q):
        if f < 8:
            Ms.append(10 ** f)

    #         todo speak about how f must be under < 8 as **9 and above = 1 billion and python cant handle

    for m in Ms:
        print("m: " + m)
        for o in range(1, m):
            numer = random.randint(0, n - 1)
            array[numer] = 3
        num = random.randint(0, n - 1)
        start = clock()
        array[num] = 3
        end = clock()
        print("Set: {0:.5f} ms".format((end - start)*1000))
        num = random.randint(0, n - 1)
        start = clock()
        array[num]
        end = clock()
        print("Get: {0:.5f} ms".format((end - start)*1000))
