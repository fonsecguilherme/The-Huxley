def retornaPares(lista):
    listaPar = []
    for i in lista:
        if i % 2 == 0: 
            listaPar.append(i)
    return listaPar

lista = [1,2,3,4,5,6,7,8,9,10]

result = retornaPares(lista)
print(result)