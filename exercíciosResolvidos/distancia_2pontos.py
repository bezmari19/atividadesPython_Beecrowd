import math #importa a biblioteca de funções matemáticas do python
x1, y1 = map(float, input().split())
#as entradas são lidas da seguinte forma:
#split() usado com o input transforma e divide em uma lista de string. Cada váriavel com seu número
#map(float,...) converte cada string em um numero com casas decimais
x2, y2 = map(float, input().split())

distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
#função do módulo math que calcula a raiz quadrada de um número

print(f'{distancia:.4f}') #saida do resultado com 4 casas decimais