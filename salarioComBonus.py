nomeVendedor = input()
salarioFixo = float(input())
totalVendas = float(input())

comissaoDada = totalVendas * 0.15
totalMes = salarioFixo + comissaoDada

print(f'TOTAL = R$ {totalMes:.2f}')