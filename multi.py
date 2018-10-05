from pylab import *
import multiprocess as mp
import time as t


def function(N):
    total = 0
    for i in arange(N):
        for j in arange(N):
            total += i / ((j + 1) ** 2)
    return total


if __name__ == '__main__':

    K = 100

    t0 = t.time()

    # Code for Serial (classical approach)
    totals = zeros(K)
    for i in arange(K):
        totals[i] = function(i)

    tElapsed = t.time() - t0
    print('Time for serial version is {}'.format(tElapsed))

    t0 = t.time()

    # Code for Pool
    nProcs = mp.cpu_count()  # Number of processors (cores).
    print('Now Pool')
    p = mp.Pool(processes=nProcs)
    results = p.map(function, [n for n in range(K)])  # Maps the argument to the function named.
    p.close()  # Says we are done making processes to send.
    p.join()  # Blocks until we finish the entirety of the multiprocessing (on all procs).

    tElapsed = t.time() - t0
    print('Time for pool version is {}'.format(tElapsed))
