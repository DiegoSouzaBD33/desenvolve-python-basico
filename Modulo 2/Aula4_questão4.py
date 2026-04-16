# Solicita ao usuário um valor inteiro em reais
valor = int(input())

# Calcula a quantidade de notas de 100 reais
nota_100 = valor // 100
valor = valor % 100

# Calcula a quantidade de notas de 50 reais
nota_50 = valor // 50
valor = valor % 50

# Calcula a quantidade de notas de 20 reais
nota_20 = valor // 20
valor = valor % 20

# Calcula a quantidade de notas de 10 reais
nota_10 = valor // 10
valor = valor % 10

# Calcula a quantidade de notas de 5 reais
nota_5 = valor // 5
valor = valor % 5

# Calcula a quantidade de notas de 2 reais
nota_2 = valor // 2
valor = valor % 2

# Calcula a quantidade de notas de 1 real
nota_1 = valor // 1

# Exibe o resultado no formato solicitado
print(f"{nota_100} nota(s) de R$100,00")
print(f"{nota_50} nota(s) de R$50,00")
print(f"{nota_20} nota(s) de R$20,00")
print(f"{nota_10} nota(s) de R$10,00")
print(f"{nota_5} nota(s) de R$5,00")
print(f"{nota_2} nota(s) de R$2,00")
print(f"{nota_1} nota(s) de R$1,00")