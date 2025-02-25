numeroFuncionario = int(input()) # Colocar o número do funcionário correspondente dentro da sua variável
numeroHorasTrabalhadas = int(input()) # Aqui a variável que representa o total de horas trabalhadas pelo tal funcionario
valorPorHora = float(input()) # Aqui está o valor representado pela variável em casa decimal(valor flutuante) que representa o preço por hora do respectivo trabalho

valorSalarioTotal = numeroHorasTrabalhadas * valorPorHora # para obter o valor criamos uma nova variavel que representa o calculo com os valores obtidos nas variaveis de entrada, assim temos o salario total do funcionario

print('NUMBER =', numeroFuncionario) # Imprimi o número do funcionario 
print('SALARY = U$', '%.2f' % valorSalarioTotal) # imprimi o total do salário do respectivo funcionario com duas casas decimais para representar o valor cheio monetário