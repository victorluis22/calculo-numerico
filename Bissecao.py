import math
from expressoes import expressoes

def bissecao(intervaloInicio, intervaloFim, precisao, key):

    def expressao(x):
        return eval(expressoes[key])

    contador = 0

    while True:
        contador += 1
        x = (intervaloInicio + intervaloFim)/2
        resultadoMedio = expressao(x)

        if abs(resultadoMedio) < precisao:
            raiz = x
            break
        else:
            resultadoInicio = expressao(intervaloInicio)
            resultadoFim = expressao(intervaloFim)

            if resultadoInicio * resultadoMedio < 0:
                intervaloFim = x
            elif resultadoMedio * resultadoFim < 0:
                intervaloInicio = x

    print('\nMétodo Bisseção')
    print(f'Raiz: {raiz}\nNúmero de iterações: {contador}')