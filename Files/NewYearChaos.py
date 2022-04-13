#!/bin/python

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    size = len(q)
    n_bribes = 0
    for i in range(size):
        real_idx = i+1
        if q[i]-real_idx >0:
            if q[i]-real_idx <=2:
                n_bribes += q[i]-real_idx
            else:
                print("Too chaotic")
                return
    return
    
if __name__ == '__main__':
    t = int(raw_input())

    for t_itr in xrange(t):
        n = int(raw_input())

        q = map(int, raw_input().rstrip().split())

        minimumBribes(q)
