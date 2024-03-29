'''

A fermionic system with  energy levels that isn't in superposition can be represented simply as a bitstring of length , because of the Pauli Exclusion Principle. For example, if we have three energy levels, then the state  represents a system which has a fermion in the second energy level, but no fermions in the first or third energy levels. To simulate fermionic systems, we need to be able to simulate sequences of fermionic raising and lowering operators (don't worry about exactly what they are). Doing so efficiently boils down to being able to do three things efficiently on a state:

: Query whether an energy level  is occupied (return 1) or not occupied (return 0);
: Change the value at energy level  from either occupied (1) to not occupied (0) or vice-versa.
: Calculate the parity (return 1 if odd, 0 if even) of the sum of the occupation numbers of every energy level up to and including level .
Your job is to design a system that can handle any sequence of any of these three types of queries efficiently. Assume that in the initial state, every energy level is unoccupied. Further assume that the positions in the state are zero-indexed, i.e. they start from zero.

Input Format

The first line contains two positive integers  and , separated by the space. Here  is the number of energy levels in the system and  is the number of queries that will be issued. The subsequent  lines will contain two space-separated numbers, which will represent the type of query (1 = , 2 = , 3 = ) and the argument of the query, respectively. See sections below for how queries are formed.

Constraints

, . You can assume that no query will be malformed, i.e. every line will be of the form  where  and .

Output Format

Your program should output answers to queries in the order they are issued. Note that for queries of type 2 (), your program will not output anything; however, queries of type 2 will impact the output of future type 1 and 3 queries.

Sample Input 0

5 6
1 3
2 2
2 3
3 0
3 4
1 2
Sample Output 0

0
0
0
1


'''
# WINNER

#!/bin/python3

import math
import os
import random
import re
import sys


def parity(x, nr):

    k = int(math.log2(nr + 1))
    while(k >= 0):
        x ^= x >> int(2**k)
        k -= 1

    return (x & 1)


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    s = 0
    d = dict()

    for m_itr in range(m):
        # Parse the query

        second_multiple_input = input().rstrip().split()

        queryType = int(second_multiple_input[0])

        index = int(second_multiple_input[1])

        # Do something with each query

        if queryType == 1:
            if index in d:
                print(d[index])
            else:
                print(0)
        elif queryType == 2:
            s = s ^ (1 << (n - index - 1))
            if index in d:
                d[index] = 1 - d[index]
            else:
                d[index] = 1
        elif queryType == 3:
            aux = s >> (n - index - 1)
            print(parity(aux, index))
