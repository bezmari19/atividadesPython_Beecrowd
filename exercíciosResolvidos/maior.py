#Lê as linhas de código uma a uma por ordem da váriavel
valores_comparacao = input().split()
#ValorA é a primeira da lista (começa contando em 0)
ValorA = int(valores_comparacao[0])
#ValorB é a segunda da lista (por contar por 0, seria o primeiro)
valorB = int(valores_comparacao[1])
#ValorC é a terceira da lista (esse será o terceiro)
valorC = int(valores_comparacao[2])

#independentemente dos valores colocados os cálculos abaixa mostrarão qual é o maior valor entre os 3 (A,B,C)
maiorAB = (ValorA + valorB + abs(ValorA-valorB)) / 2 #calculo pedido no exercicio - só comparando A e B
maior = (maiorAB + valorC + abs(maiorAB - valorC)) / 2 #calculo adiconando a comparação da terceira variável

print (f"{int(maior)} eh o maior") #converte a resposta para um número inteiro