# -*- coding: utf-8 -*-
import numpy as np


def sucesion(n):
    return 1 / (1 + np.exp(-n))


def raiz2a(n):
    if n == 0:
        return 4
    else:
        return raiz2(n-1)/2 + 1/raiz2(n-1)

    
def raiz2b(n):                      # Versión alternativa de raiz2(n). ¡Es mucho más rápida!
    r = 4
    for i in range(n):
        rnuevo = r/2 + 1/r
        r = rnuevo
    return r
    
def sinc(x):
    if x == 0:
        return 1
    else:
        return np.sin(x) / x

    
def sinc2(x):
    if x == 0:
        return 1
    else:
        return np.sin(x) / (x ** 2)