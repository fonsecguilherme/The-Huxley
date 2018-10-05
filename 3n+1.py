def resultado(numero):
    lista = [numero]
    while numero != 1:
        if numero % 2 == 0:
            numero = numero /2
            lista.append(numero)
        else: 
            numero = (numero * 3) + 1
            lista.append(numero)
    return lista  

def comparaListas(lista1, lista2):
    if lista1 > lista2:
        return lista1
    else:
        return lista2

num = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

lista1 = resultado(num)
lista2 = resultado(num2)

tamLista1 = len(lista1)
tamLista2 = len(lista2)

resultadoFinal = comparaListas(tamLista1, tamLista2)
print(resultadoFinal)
