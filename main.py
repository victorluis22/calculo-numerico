from expressoes import expressoes
from bissecao import bissecao
from falsaPosicao import falsaPosicao
from newtonRaphson import newtonRaphson
from metodoSecante import secante

def init():
    for key, expressao in expressoes.items():
        print(f'{key}: {expressao}')

    key = input("\nSelecione a expressao desejada: ")
    intervaloInicio = float(input("Insira o inicio do intervalo de varredura = "))
    intervaloFim = float(input("Insira o fim do intervalo de varredura = "))
    precisao = 0.00001

    print('****** Resultados ******')
    bissecao(intervaloInicio, intervaloFim, precisao, key)
    falsaPosicao(intervaloInicio, intervaloFim, precisao, key)
    secante(intervaloInicio, intervaloFim, precisao, key)
    newtonRaphson(intervaloInicio, intervaloFim, precisao, key)

init()


