"""
Implementation of testing the functions contained within SparseArray.

Sets/gets elements from SparseArray with varying sizes, values of n and a changing number of non-empty elements.

**** NB MemoryError prevents tests > m^9  ****
"""


from SparseArray import SparseArray
import random
from time import clock
for q in range(3,13):
    print("")
    n = 10**q
    print("n: " + n)
    array = SparseArray(n)
    Ms = []
    for f in range(0,q):
        if f < 8:
            Ms.append(10 ** f)

    for m in Ms:
        print("m: " + m)
        for m in range(1, m):
            num = random.randint(0, n-1)
            array[num] = 3
        numer = random.randint(0, n-1)
        start = clock()
        array[numer] = 3
        end = clock()
        print("Set: {0:.5f} ms".format((end - start)*1000))
        numer = random.randint(0, n-1)
        start = clock()
        array[numer]
        end = clock()
        print("Get: {0:.5f} ms".format((end - start)*1000))
