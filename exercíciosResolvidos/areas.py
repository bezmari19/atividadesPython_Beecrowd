valores_calculo = input().split() #Lê uma linha de entrada e a divide em uma lista de strings com base nos espaços.
valorA = float(valores_calculo[0]) #Pega o primeiro elemento da lista e o converte para float, atribuindo-o à variável valorA.
valorB = float(valores_calculo[1]) #Pega o segundo elemento da lista e o converte para float, atribuindo-o à variável valorB.
valorC = float(valores_calculo[2]) #Pega o terceiro elemento da lista e o converte para float, atribuindo-o à variável valorC.

triangulo_retangulo = (valorA * valorC) / 2
circulo_raio = 3.14159 * valorC ** 2
trapezio = (valorA + valorB) * valorC / 2
quadrado_area = valorB * valorB
retangulo = valorA * valorB

print(f'TRIANGULO: {triangulo_retangulo:.3f}')
print(f'CIRCULO: {circulo_raio:.3f}')
print(f'TRAPEZIO: {trapezio:.3f}')
print(f'QUADRADO: {quadrado_area:.3f}')
print(f'RETANGULO: {retangulo:.3f}')