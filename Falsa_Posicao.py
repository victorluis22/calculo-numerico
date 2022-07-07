import math

expressoes = {
    'e1': '-x + 2*math.exp(-x)',
    'e2': 'x**2 - math.cos(x)',
    'e3': '4*math.cos(x) - math.cosh(x)',
    'e4': 'math.log(x) + x*(x**0.5)',
    'e5': 'x**2 - 2',
    'e6': '3*(x**0.5) + math.log(x) - 4'
}

def expressao(x):
    return eval(expressoes['e6'])

def calculaRaiz():
    contador = 0
    intervaloInicio = float(input("Insira o inicio do intervalo de varredura = "))
    intervaloFim = float(input("Insira o fim do intervalo de varredura = "))
    precisao = 0.00001

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

    print(f'\nRaiz: {raiz}\nNúmero de iterações: {contador}')
    return raiz

calculaRaiz()