## Questão 2

# Solicitando as idades

idade_juliana = int(input("Digite a idade da Juliana: "))
idade_cris = int(input("Digite a idade da Cris: "))

# Verificando se alguma das duas é maior de idade
podem_entrar = idade_juliana >17 or idade_cris > 17

# Exibe o resultado
print(podem_entrar)