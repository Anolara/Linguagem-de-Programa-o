def inverte_frase(frase):
    invertida = frase[::-1]
    return invertida


a = input("Digite a frase para inverter: ")
inverte_frase(a)
print("A frase invertida ficou: ", inverte_frase(a))