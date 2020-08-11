# -*- coding: utf-8 -*-
import numpy as np


def uniforme_discreta(k, a, b):
    if a <= k <= b:
        return 1 / (b + 1 - a)
    else:
        return 0

def bernoulli(k, p):
    if k == 0:
        return 1 - p
    elif k == 1:
        return p
    else:
        return 0

def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        prod = 1
        for i in range(1, n + 1):
            prod *= i
        return prod

def comb(n, k):
    return fact(n) / (fact(k) * fact(n - k))

def binomial(k, n, p):
    if 0 <= k <= n:
        return comb(n, k) * (p ** k) * (1 - p) ** (n - k)
    else:
        return 0

def geometrica(k, p):
    if 1 <= k:
        return p * (1 - p) ** (k - 1)
    else:
        return 0

def binomial_negativa(k, r, p):
    if 0 <= k:
        return comb(k + r - 1, k) * (p ** r) * (1 - p) ** k
    else:
        return 0

def poisson(k, l):
    if 0 <= k:
        return (l ** k) * np.exp(-l) / fact(k)
    else:
        return 0
    
def uniforme_continua(x, a, b):
    if a <= x <= b:
        return 1 / (b - a)
    else:
        return 0
    
def exponencial(x, l):
    if 0 <= x:
        return l * np.exp(-l * x)
    else:
        return 0
    
def normal(x, mu, sigma):
    return (1 / np.sqrt(2 * np.pi * sigma ** 2)) * np.exp(-(x - mu) ** 2 / (2 * sigma ** 2))


