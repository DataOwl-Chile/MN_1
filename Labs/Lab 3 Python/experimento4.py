# -*- coding: utf-8 -*-
import numpy as np


def derivada(x, y):
    """
    Devuelve la derivada de una función, considerando que en extremo izquierdo sólo se puede
    aplicar derivada forward, en extremo derecho sólo se puede aplicar derivada backward y 
    entremedio puede aplicad derivada central, que es más precisa.
    
    param x: vector en el que se evaluará la función, tiene largo N.
    param y: vector de la función evaluada en x.
    """
    
    N = len(x)
    
    # Calculamos dx, que tendrá N-1 valores
    dx = []
    
    for i in range(N-1):
        dx.append(x[i + 1] - x[i])
        
    # OJO: Si el vector x fuese definido de forma equiespaciada, por ejemplo, con linspace
    # , basta con dx = x[1] - x[0].
    # Además, en ese caso, dx[0] = dx[N - 1] = dx y dx[i + 1] + dx[i - 1] = 2*dx
    
    deriv = []

    for i, Y in enumerate(y):
        
        if i == 0:                   # Extremo izquierdo: usamos derivada forward
            der1 = (y[1] - y[0]) / dx[0]
            der.append(der1)
            
        elif i == N - 1:             # Extremo derecho: usamos derivada backward (recordar que índice de x e y llega hasta N-1
            der1 = (y[N - 1] - y[N - 2]) / dx[N - 1]
            der.append(der1)
            
        else:                        # Extremo izquierdo: usamos derivada forward
            der1 = (y[i + 1] - y[i - 1]) / (dx[i + 1] + dx[i - 1])
            der.append(der1)
            
    return der
