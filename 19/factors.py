#!/usr/bin/env  python

from __future__ import print_function

from math import sqrt


def factors(n):
    i = 2
    while i<sqrt(n):
        if n%i == 0:
            print(i, n//i)
            return [i] + factors(n//i)
        i+=1
    return [n]


def factor_generator(n):
    i = 2
    while i<sqrt(n):
        i+=1
        if n%i == 0:
            yield i
            n = n // i
            i = 2
    yield n





if __name__ == '__main__':
    n = 10551315
    print(factors(n))
    print(list(factor_generator(n)))
