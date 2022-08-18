from dados import dados

abscissas = dados["abscissas"]
ordenadas = dados["ordenadas"]
resultados = []
lagrange_parcial = []
aux = []

def L(x, inicio, fim):
    return ((x - abscissas[fim])/(abscissas[inicio] - abscissas[fim]))

def P1(x, inicio, fim):
    return L(x, inicio, fim)*ordenadas[inicio] + L(x, fim, inicio)*ordenadas[fim]

def P(x, inicio, fim, parciais):
    return ((x-fim)*parciais[0] - (x-inicio)*parciais[1])/(inicio-fim)


def lagrange():
    cont = 1
    x = float(input("Insira o x que se deseja aproximar: "))
    
    # Calcula os primeiros p1 do programa
    for indice in range(len(abscissas)-cont):
        p1 = P1(x, indice, indice+cont)
        lagrange_parcial.append(p1)

    resultados.append(lagrange_parcial[:])

    while len(lagrange_parcial) != 1:
        cont += 1 

        for indice in range(len(lagrange_parcial)-1):
            p = P(x, abscissas[indice], abscissas[indice+cont], [lagrange_parcial[indice], lagrange_parcial[indice+1]])
            aux.append(p)

        resultados.append(aux[:])
        lagrange_parcial.clear()
        lagrange_parcial.extend(aux)
        aux.clear()

lagrange()


print("\n==== Resultados ====\n\n")
for i in range(len(resultados)):
    print(f'P{i+1}(x) = {resultados[i]}')
print("\n")

        









        