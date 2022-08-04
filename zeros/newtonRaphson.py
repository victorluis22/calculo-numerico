import math
from expressoes import expressoes

def newtonRaphson(intervaloInicio, intervaloFim, precisao, key):

    def expressao(x):
        return eval(expressoes[key])

    def deriv_expressao(x):
        precisao_dif = 0.00001
        diferencial = (x+precisao_dif) - x
        return (expressao(x+precisao_dif) - expressao(x))/ diferencial

    contador = 0
    x_velho = 0

    while True:
        contador += 1
        
        if contador == 1:
            x = (intervaloInicio + intervaloFim)/2
        else:
            x = x_velho - (expressao(x_velho)/deriv_expressao(x_velho))

        resultadoMedio = expressao(x)

        if abs(resultadoMedio) < precisao:
            raiz = x
            break
        
        x_velho = x

    print('\nMétodo Newton-Raphson')
    print(f'Raiz: {raiz}\nNúmero de iterações: {contador}')