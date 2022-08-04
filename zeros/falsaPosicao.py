import math
from expressoes import expressoes

def falsaPosicao(intervaloInicio, intervaloFim, precisao, key):

    def expressao(x):
        return eval(expressoes[key])

    contador = 0

    while True:
        contador += 1

        x = ((intervaloInicio*expressao(intervaloFim) - intervaloFim*expressao(intervaloInicio))/(expressao(intervaloFim) - expressao(intervaloInicio)))

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

    print('\nMétodo Falsa Posição')
    print(f'Raiz: {raiz}\nNúmero de iterações: {contador}')