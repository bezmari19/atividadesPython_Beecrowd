#Valores a serem atribuidos às váriaveis 1,2 e 3 em Float(casas decimais) que correspondem as notas dadas no exercicios ( ou qualquer outra )
valor1 = float(input())
valor2 = float(input())
valor3 = float(input())
 #Os valores já atribuidos de cada peso correspondente as cada nota do aluno 1, 2 e 3
Peso1 = 2
Peso2 = 3
Peso3 = 5
#O cálculo da média do aluno, atribuindo a operação feita com os valores correspondentes
MediaDoAluno = (valor1 * Peso1 + valor2 * Peso2 + valor3 * Peso3) / (Peso1 + Peso2 + Peso3)
#Saída (Output) da forma pedida, atribuindo a média uma casa decimal aparecendo no resultado
print(f'MEDIA = {MediaDoAluno:.1f}')