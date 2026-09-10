import math

def f(func):
    L = float(input())
    R = float(input())
    while abs(L - R) > 0.001:
        b = L + (R - L) / 2
        if func(L) * func(b) < 0: # при перемножении, если у одной точки на границе + , a y другой - , то тогда есть решение на этом отрезке.
            R = b
        else:
            L = b
    return (L + R) / 2

def f2(x):
    return (1 - 0.4*x**2)**0.5 - math.asin(x)

print(f(f2)) #ответ по 4 варианту






import math

def f(func):
    L = float(input())
    R = float(input())
    eps = 0.001
    pred_peresech = L # предыдущее пересечение
    while True:
        peresech = L - (func(L) * (R - L)) / (func(R) - func(L)) # по формуле просто
        if func(peresech) == 0 or abs(peresech - pred_peresech) < eps: # если сразу решение или
            return peresech                     # расстояние между пред пересеч и текущим очень малое
        elif func(peresech) * func(L) < 0:
            R = peresech
        else:
            L = peresech
        pred_peresech = peresech # задаем текущее пересечение как предыдущее

def f2(x):
    return (1 - 0.4*x**2)**0.5 - math.asin(x)

print(f(f2))