A = int(input()) #Entrada do valor A. Lembre-se que Int() são referentes aos números inteiros dentro de uma váriavel, assim seu programa reconhecerá a função e converterá um número ou string.
B = int(input())
    #Saber a função Int() é importante para qualquer cálculo em linguagem Python!
if A == -A and -A > B: #Condição 'if-else', usada para condicões especificas do programa.
  #O if é usado para verificar se uma condição é verdadeira, se sim, ele será executado. Aqui leria-se ==(igual a), and(lógico E)
  print('X =', -A + B)
elif B == A and A > -B: #Já o 'elif' é usado como um verificador secundario se caso o if não for verdadeiro. Cada bloco de código com elif só é executado quando a condição relacionada a primeira for verdadeira.
  print('X =', A - B)
else: #O else serve como um verificador do bloco de código caso nenhuma das condições especificadas sejam verdadeiras. Como uma condição a mais ou fora do padrão do código que foi especificado.
  print('X =', A + B)
  #Aqui o 'X =' é especificado na questão como deve ser executado. Nele pode ser tanto "" ou '' tudo vai depender do que se sente mais confortável para usar nos seus códigos.
  #O programa deve executar X = a equação que foi feita no programa, ou seja a soma.