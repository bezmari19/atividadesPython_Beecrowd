#Calculo usando a função split()
#A função split() divide uma string em uma lista de substrings, ou seja, partes da string separadas por um demmarcaddor

#Primeiro: Receber os dados da primeira peça;
#A função input() lê uma linha do teclado.
#.split() divide a linha em uma lista de strings usando o espaço como separador.
#Por exemplo, se você digitar "12 1 5.30", ele se tornará ["12", "1", "5.30"]
linha_pecas1 = input().split()

#Segundo: Extrair os valores da primeira peça
#Para a primeira peça:
#O código da peça 1 é o primeiro elemento da lista (índice 0).
#O número de peças 1 é o segundo elemento (índice 1). Convertemos para inteiro (int()).
#O valor unitário da peça 1 é o terceiro elemento (índice 2). Convertemos para float (float()) para lidar com casas decimais.
codigo_peca1 = int(linha_pecas1[0]) # Não vamos usar o código para o cálculo, mas é bom extrair
quanti_pecas1 = int(linha_pecas1[1])
valor_unitario_peca1 = float(linha_pecas1[2])

#Terceiro: Receber os dados da segunda peça
linha_pecas2 = input().split()

#Quarto: Extrair os valores da segunda peça
codigo_peca2 = int(linha_pecas2[0]) 
quanti_pecas2 = int(linha_pecas2[1])
valor_unitario_peca2 = float(linha_pecas2[2])

#Quinto: Calcular o valor do final da compra
total_peca1 = quanti_pecas1 * valor_unitario_peca1
total_peca2 = quanti_pecas2 * valor_unitario_peca2
valor_total = total_peca1 + total_peca2

#E por último, mas não menos importante, imprir o resultado
print(f"VALOR A PAGAR: R$ {valor_total:.2f}")
#A função print() exibe o resultado formatado com duas casas decimais
