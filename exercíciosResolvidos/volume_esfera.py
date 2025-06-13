#Calculando o volume de uma esfera a partir do raio dela

raio_esfera = float(input())

#A fórmula do volume da esfera se calcula da seguinte forma:
#V = 4/3 * pi * r³
volume_esfera = (4/3) * 3.14159 * (raio_esfera ** 3)

#Exibindo o resultado com 3 casas decimais
print(f'VOLUME = {volume_esfera:.3f}')