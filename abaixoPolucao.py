array = []
casasMultadas = 0
tributo = 0
numero = 0

while numero != 999:
    numero = int(input("Digita a quantidade de carros na casa: "))
    if numero == 999:
        break 
    if numero > 2:
        quantidadeCasos = numero -2
        tributo = tributo + (quantidadeCasos * 12.89)
        casasMultadas += 1
    array.append(numero)

print(tributo)
print(casasMultadas)
