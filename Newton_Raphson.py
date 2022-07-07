import math

expressoes = {
    'e1': '-x + 2*math.exp(-x)',
    'e2': 'x**2 - math.cos(x)',
    'e3': '4*math.cos(x) - math.cosh(x)',
    'e4': 'math.log(x) + x*(x**0.5)',
    'e5': 'x**2 - 2',
    'e6': '3*(x**0.5) + math.log(x) - 4',
    'e7': 'x*math.log(x) - 1',
    'e8': 'x**3 - math.exp(-2*x)',
    'e9': 'x**2 - math.sin(2*x)',
    'e10': 'math.log(3*x) - math.cos(3*x)'
}

def expressao(x):
    return eval(expressoes['e7'])

def deriv_expressao(x):
    precisao_dif = 0.00001
    diferencial = (x+precisao_dif) - x
    return (expressao(x+precisao_dif) - expressao(x))/ diferencial

def calculaRaiz():
    contador = 0
    x_velho = 0
    
    intervaloInicio = float(input("Insira o inicio do intervalo de varredura = "))
    intervaloFim = float(input("Insira o fim do intervalo de varredura = "))
    precisao = 0.00001

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
        else:
            resultadoInicio = expressao(intervaloInicio)
            resultadoFim = expressao(intervaloFim)

            if resultadoInicio * resultadoMedio < 0:
                intervaloFim = x
            elif resultadoMedio * resultadoFim < 0:
                intervaloInicio = x
            x_velho = x

    print(f'\nRaiz: {raiz}\nNúmero de iterações: {contador}')
    return raiz

calculaRaiz()