# coding: utf-8

"""
This problem was asked by Jane Street.

cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair.
For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.
Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair
Implement car and cdr.
"""

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(f) -> int:
    def take(a, b):
        return a
    return f(take)

def cdr(f) -> int:
    def take(a, b):
        return b
    return f(take)

if __name__ == "__main__":
    assert car(cons(3, 4)) == 3
    assert car(cons(10, 20)) == 10
    assert cdr(cons(3, 4)) == 4
    assert cdr(cons(10, 20)) == 20
    
