from dados import formulas
from sympy import *
from math import *

e = E.n()

formula = formulas['8']
ordem = 2
valor = 2
h = 0.01

def f(x):
    return eval(formula)

def derivada(x0, ordem):
    x = Symbol('x')
    y = sympify(formula)

    y = y.diff(x, ordem)

    x = x0

    return eval(str(y))

def formulaCentrada(x0, h, ordem):
    if ordem == 1:
        return (f(x0+h) - f(x0-h))/(2*h)
    elif ordem == 2:
        return (f(x0-h) + f(x0+h) - 2*f(x0))/(h**2)

def formulaNaoCentrada(x0, h):
    return (-3*f(x0))/(2*h) + (2*f(x0+h))/h + (-f(x0+2*h))/(2*h)


def erroTruncamentoCentrado(x0, h, ordem):
    if ordem == 1:
        print(f'\nErro de truncamento de {x0-h:.2f}: {fabs(((h**2)/6)*derivada(x0-h, 3)):e}')
        print(f'Erro de truncamento de {x0+h:.2f}: {fabs(((h**2)/6)*derivada(x0+h, 3)):e}')
    elif ordem == 2:
        print(f'\nErro de truncamento de {x0-h:.2f}: {fabs(((h**2)/12)*derivada(x0-h, 4)):e}')
        print(f'Erro de truncamento de {x0+h:.2f}: {fabs(((h**2)/12)*derivada(x0+h, 4)):e}')

def erroTruncamentoNaoCentrado(x0, h):
    print(f'\nErro de truncamento de {x0:.2f}: {fabs(((h**2)/3)*derivada(x0, 3)):e}')
    print(f'Erro de truncamento de {x0+2*h:.2f}: {fabs(((h**2)/3)*derivada(x0+2*h, 3)):e}')

def DRP(aprox):
    ref = derivada(valor, ordem)
    print(f'DRP = {fabs(((ref - aprox)/ref))*100:.2e} %\n')

        
def inicio():
    print(f'\t==== Resultados ====\n\n')

    print("Dados da fórmula centrada: ")
    print(f'Aproximação da derivada {ordem}° de [{sympify(formula)}]: {formulaCentrada(valor, h, ordem)}')
    erroTruncamentoCentrado(valor, h, ordem)
    DRP(formulaCentrada(valor, h, ordem))

    if ordem == 1:
        print("Dados da fórmula não centrada: ")
        print(f'Aproximação da derivada {ordem}° de [{sympify(formula)}]: {formulaNaoCentrada(valor, h)}')
        erroTruncamentoNaoCentrado(valor, h)
        DRP(formulaNaoCentrada(valor, h))

inicio()


