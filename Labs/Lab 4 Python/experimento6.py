# -*- coding: utf-8 -*-
import numpy as np


def descenso(f, x0, dx=0.001, error=0.00001, maxiter=100000):    # introducir maxtol?
    
    xpost = x0 + dx
    xpre = x0 - dx
    
    f0 = f(x0)
    fpost = f(xpost)
    fpre = f(xpre)
    step = np.min([f0 - fpre, fpost - f0])
    
    contador = 0
    
    while np.abs(step) > error and contador <= maxiter:
        if fpost > f0:
            if fpre > f0:
                return x0, f0, contador
            else:
                contador += 1
                x0 = xpre
                xpre = x0 - dx
                f0 = f(x0)
                fpre = f(xpre)
                step = f0 - fpre
                
        elif fpost < f0 and f0 < fpre:
            contador += 1
            x0 = xpost
            xpost = x0 + dx
            f0 = f(x0)
            fpost = f(xpost)
            step = fpost - f0
            
        else:
            print('No se puede encontrar mínimo')
            return [], [], []
    
    return x0, f0, contador
    

def newtonoptim(f, x0, dx=0.01, error=0.0001, max_iter=100000):
        
    xn = x0
    
    for n in range(0, max_iter):
        
        dfn = (f(xn + dx) - f(xn - dx)) / (2 * dx)
        
        if abs(dfn) < error:
            print('Solución tras ', n, ' iteraciones.')
            return xn, f(xn), dfn
        
        d2fn = (f(xn + dx) - 2 * f(xn) + f(xn - dx)) / (dx ** 2)
        
        if d2fn == 0:
            print('Método se indefine (segunda derivada se anula).')
            return None, None, None
        
        xn = xn - dfn / d2fn
        
    print('Método no converge (se supera el máximo de iteraciones).')
    return None, None, None
    
    
    
    
    
    

