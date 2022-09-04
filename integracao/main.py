from dados import formulas
from math import *
from sympy import *

e = E.n()
pi = pi.n()

formula = formulas['5']
x0 = 0
x1 = 1
h = x1 - x0
m = 10

def f(x):
    return eval(formula)

def DRP(ref, aprox):
    return fabs(((ref - aprox)/ref) * 100)

def derivada(x0, ordem):
    x = Symbol('x')
    y = sympify(formula)

    y = y.diff(x, ordem)

    x = x0

    return eval(str(y))

def integral(x0, x1, ordem):
    x = Symbol('x')
    y = sympify(formula)

    y = integrate(y, (x, x0, x1))

    x = x0

    return eval(str(y))


def metodoTrapezio(x0, x1, h):
    return (h * (f(x0) + f(x1))) / 2

def erroTruncamentoTrapezio(x0, x1, h):
    erro_x0 = fabs(((h**3)/12) * (derivada(x0, 2)))
    erro_x1 = fabs(((h**3)/12) * (derivada(x1, 2)))

    if erro_x0 > erro_x1:
        return erro_x0
    else:
        return erro_x1

def metodoTrapezioRepetido(x0, x1, m):
    h = (x1 - x0)/m
    x0_aux = x0
    x1_aux = x1
    resultado = 0

    for i in range(m):
        resultado += metodoTrapezio(x0_aux, x0_aux+h, h)
        x0_aux += h

    return resultado

def erroTruncamentoTrapezioRepetido(x0, x1, m):
    h = (x1 - x0)/m
    x0_aux = x0
    x1_aux = x1
    erros = []

    for i in range(m):
        erros.append(fabs((((x1-x0)*(h**2))/12) * (derivada(x0_aux, 2))))
        x0_aux += h

    return max(erros)


print(f'Aproximaçao trapézio: {metodoTrapezio(x0, x1, h)}')
print(f'Erro de truncamento trapézio: {erroTruncamentoTrapezio(x0, x1, h):e}')
print(f'DRP: {DRP(integral(x0, x1, 1), metodoTrapezio(x0, x1, h)):.2f} %')

print('\n----------------------------------------------\n')

print(f'Aproximação trapézio repetido: {metodoTrapezioRepetido(x0, x1, m)}')
print(f'Erro de truncamento trapézio repetido: {erroTruncamentoTrapezioRepetido(x0, x1, m):e}')
print(f'DRP: {DRP(integral(x0, x1, 1), metodoTrapezioRepetido(x0, x1, m)):.2f} %')