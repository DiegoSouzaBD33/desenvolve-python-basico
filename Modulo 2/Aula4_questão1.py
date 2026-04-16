# Solicita ao usuário o comprimento do terreno (valor inteiro)
comprimento = int(input("Digite o comprimento do terreno (m): "))

# Solicita ao usuário a largura do terreno (valor inteiro)
largura = int(input("Digite a largura do terreno (m): "))

# Solicita ao usuário o preço por metro quadrado (valor decimal)
preco_m2 = float(input("Digite o preço do metro quadrado (R$): "))

# Calcula a área do terreno em metros quadrados
area_m2 = comprimento * largura

# Calcula o preço total do terreno com base na área e no preço por m²
preco_total = preco_m2 * area_m2

# Exibe o resultado formatado conforme o exemplo solicitado
print(f"O terreno possui {area_m2}m2 e custa R${preco_total:,.2f}")