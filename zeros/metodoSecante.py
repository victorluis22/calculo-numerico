import math
from expressoes import expressoes

def secante(intervaloInicio, intervaloFim, precisao, key):

    def expressao(x):
        return eval(expressoes[key])

    contador = 0
    x_velho_1 = 0
    x_velho_2 = 0

    while True:
        contador += 1
        
        if contador == 1:
            x = (intervaloInicio + intervaloFim)/2
            x_velho_1 = intervaloInicio
            x_velho_2 = intervaloFim
        else:
            x = (x_velho_1 - ((expressao(x_velho_1)*(x_velho_1-x_velho_2))/(expressao(x_velho_1)-expressao(x_velho_2))))

        resultadoMedio = expressao(x)

        if abs(resultadoMedio) < precisao:
            raiz = x
            break

        x_velho_1 = x
        x_velho_2 = intervaloInicio

    print('\nMétodo Secante')
    print(f'Raiz: {raiz}\nNúmero de iterações: {contador}')