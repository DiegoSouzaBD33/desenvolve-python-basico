# Solicita o nome do primeiro produto
nome1 = input("Digite o nome do produto 1:")

# Solicita o preço unitário do primeiro produto
preco1 = float(input("Digite o preço unitário do produto 1:"))

# Solicita a quantidade do primeiro produto
qtd1 = int(input("Digite a quantidade do produto 1:"))

# Calcula o total do primeiro produto
total1 = preco1 * qtd1

# Solicita o nome do segundo produto
nome2 = input("Digite o nome do produto 2:")

# Solicita o preço unitário do segundo produto
preco2 = float(input("Digite o preço unitário do produto 2:"))

# Solicita a quantidade do segundo produto
qtd2 = int(input("Digite a quantidade do produto 2:"))

# Calcula o total do segundo produto
total2 = preco2 * qtd2

# Solicita o nome do terceiro produto
nome3 = input("Digite o nome do produto 3:")

# Solicita o preço unitário do terceiro produto
preco3 = float(input("Digite o preço unitário do produto 3:"))

# Solicita a quantidade do terceiro produto
qtd3 = int(input("Digite a quantidade do produto 3:"))

# Calcula o total do terceiro produto
total3 = preco3 * qtd3

# Soma o valor total da compra
total_compra = total1 + total2 + total3

# Exibe o valor total formatado com separador de milhar e duas casas decimais
print(f"Total: R${total_compra:,.2f}")