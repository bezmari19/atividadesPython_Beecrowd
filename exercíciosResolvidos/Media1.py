#2 entradas Float (casas decimais)
A = float(input()) 
B = float(input())
PesoA = 3.5
PesoB = 7.5 #Os dois pesos de cada questão A e B

NotaDoAluno = (A * PesoA + B * PesoB) / 11 #Cáculo simples de média escolar com 2 pesos e duas notas

print(f'MEDIA = {NotaDoAluno:.5f}') #Resultado do cálculo da média mostrando 5 casas decimais após a virgula 