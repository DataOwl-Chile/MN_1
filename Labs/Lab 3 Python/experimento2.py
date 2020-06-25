# -*- coding: utf-8 -*-
import numpy as np


def tribonacci(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3)


def lesera(n):
    if n == 0:
        return 4
    else:
        return lesera(n-1)/2 + 1/lesera(n-1)

    
def weierstrass(n, x):
    a = 0.5
    b = 13
    suma = 0
    for k in range(n+1):
        y = (a ** k) * np.cos((b ** k) * np.pi * x)
        suma += y
    return suma
    
    