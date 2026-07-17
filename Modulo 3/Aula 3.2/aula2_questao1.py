### Questão 1 

# Solicita as idades
idade_juliana = int(input("Digite a idade da Juliana: "))
idade_cris = int(input("Digite a idade da Cris: "))

# Verifica se ambas são maiores de 17 anos
podem_entrar = idade_juliana > 17 and idade_cris > 17

# Exibe o resultado
print(podem_entrar)