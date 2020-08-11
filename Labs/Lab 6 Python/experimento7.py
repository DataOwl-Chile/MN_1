# -*- coding: utf-8 -*-


def suma(x, y):
    z = x + y
    return z

def resta(x, y):
    z = x - y
    print(z)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

