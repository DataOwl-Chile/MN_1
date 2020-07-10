# -*- coding: utf-8 -*-
import numpy as np


#def secante(x0, x1, f, error = 0.01):
    
def newtonraphson(f, x0, dx=0.01, error=0.0001, max_iter=100000):
    
    xn = x0
    
    for n in range(0, max_iter):
        
        fn = f(xn)
        
        if abs(fn) < error:
            print('Solución tras ', n, ' iteraciones.')
            return xn
        
        dfn = (f(xn + dx) - f(xn - dx)) / (2 * dx)
        
        if dfn == 0:
            print('Método se indefine (derivada se anula).')
            return None
        
        xn = xn - fn/dfn
        
    print('Método no converge (se supera el máximo de iteraciones).')
    return None


def cerof(x, y, error = 0.01):
    
    x0 = []
    y0 = []
    
    for i, X in enumerate(x):
        if np.abs(y[i]) <= error:
            x0.append(X)
            y0.append(y[i])
            
    x0 = np.asarray(x0)
    y0 = np.asarray(y0)
    
    return x0, y0


def ceros(a, b, f, error=0.01):
    """
    params x: arreglo en el que se quiere encontrar el cero de f
    params f: función a la que se le quiere encontrar el cero
    params a, b: extremos del intervalo que se desea explorar
    params error: nivel de precisión deseado
    returns: valor x en [a, b] en que f(x)=0
    """
    
    fa = f(a)
    fb = f(b)
    
    ceros = []
    fceros = []
    
    if fa * fb > 0:
        print('El método no aplica')
        return ceros, fceros
    elif fa * fb == 0:
        if fa == 0:
            ceros.append(a)
            fceros.append(fa)
        if fb == 0:
            ceros.append(b)
            fceros.append(fb)
            
        return ceros, fceros
    
    else:
        while (np.abs(fa).astype(float) > error) and (np.abs(fb).astype(float) > error):
            c = (a + b) / 2
            fc = f(c)
            
            if fa * fc > 0:
                a = c
                fa = fc
            
            else:
                b = c
                fb = fc
                
        if np.abs(fa).astype(float) <= error:
            ceros.append(a)
            fceros.append(fa)
        
        if np.abs(fb).astype(float) <= error:
            ceros.append(b)
            fceros.append(fb)
        
        return ceros, fceros
    
    
def derivadafun(a, b, f, dx=0.01):
    """
    Devuelve la derivada de una función, considerando que en extremo izquierdo sólo se puede
    aplicar derivada forward, en extremo derecho sólo se puede aplicar derivada backward y 
    entremedio puede aplicad derivada central, que es más precisa.
    
    param x: vector en el que se evaluará la función, tiene largo N.
    param y: vector de la función evaluada en x.
    """
    
    N = int((b - a) / dx)
    x = np.linspace(a, b, N)
    
    derivada = []

    for i, X in enumerate(x):
        
        if i == 0:                   # Extremo izquierdo: usamos derivada forward
            deriv = (f(x[1]) - f(x[0])) / dx
            derivada.append(deriv)
            
        elif i == N - 1:             # Extremo derecho: usamos derivada backward (recordar que índice de x e y llega hasta N-1
            deriv = (f(x[N - 1]) - f(x[N - 2])) / dx
            derivada.append(deriv)
            
        else:                        # Extremo izquierdo: usamos derivada forward
            deriv = (f(x[i + 1]) - f(x[i - 1])) / (2 * dx)
            derivada.append(deriv)
         
    derivada = np.asarray(derivada)
    
    return derivada


def derivadavec(x, y):
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
    
    derivada = []

    for i in range(N):
        
        if i == 0:                   # Extremo izquierdo: usamos derivada forward
            deriv = (y[1] - y[0]) / dx[0]
            derivada.append(deriv)
            
        elif i == N - 1:             # Extremo derecho: usamos derivada backward (recordar que índice de x e y llega hasta N-1
            deriv = (y[N - 1] - y[N - 2]) / dx[N - 2]
            derivada.append(deriv)
            
        else:                        # Centro: usamos derivada central
            deriv = (y[i + 1] - y[i - 1]) / (dx[i] + dx[i - 1])
            derivada.append(deriv)
            
    derivada = np.asarray(derivada)       
    
    return derivada
