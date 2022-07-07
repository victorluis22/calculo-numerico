import math

expressoes = {
    'e1': '-x + 2*math.exp(-x)',
    'e2': 'x**2 - math.cos(x)',
    'e3': '4*math.cos(x) - math.cosh(x)',
    'e4': 'math.log(x) + x*(x**0.5)',
    'e5': 'x**2 - 2',
    'e6': '3*(x**0.5) + math.log(x) - 4',
    'e7': 'x*math.log(x) - 1'
}

def expressao(x):
    return eval(expressoes['e7'])

def calculaRaiz():
    contador = 0
    x_velho_1 = 0
    x_velho_2 = 0
    
    intervaloInicio = float(input("Insira o inicio do intervalo de varredura = "))
    intervaloFim = float(input("Insira o fim do intervalo de varredura = "))
    precisao = 0.00001

    while True:
        contador += 1
        
        if contador == 1:
            x = (intervaloInicio + intervaloFim)/2
            x_velho_1 = intervaloInicio
            x_velho_2 = intervaloFim
        else:
            x = (x_velho_1 - ((expressao(x_velho_1)*(x_velho_1-x_velho_2))/(expressao(x_velho_1)-expressao(x_velho_2))))

        print(x)
        resultadoMedio = expressao(x)

        if abs(resultadoMedio) < precisao:
            raiz = x
            break

        x_velho_1 = x
        x_velho_2 = intervaloInicio

    print(f'\nRaiz: {raiz}\nNúmero de iterações: {contador}')
    return raiz

calculaRaiz()