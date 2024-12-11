import numpy as np

def linear_regression(x, y):
    if len(x) != len(y):
        raise ValueError("Las listas x e y deben tener la misma longitud")
    
    n = len(x)
    
    # Calcular medias
    mean_x = sum(x) / n
    mean_y = sum(y) / n
    
    # Calcular coeficientes
    numerador = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n))
    denominador = sum((x[i] - mean_x) ** 2 for i in range(n))
    
    # Calcular pendiente (m) y intersección (b)
    m = numerador / denominador
    b = mean_y - m * mean_x
    
    return {
        pendiente: m,
        interseccion: b,
        ecuacion: f'y = {m:.2f}x + {b:.2f}'
    }
