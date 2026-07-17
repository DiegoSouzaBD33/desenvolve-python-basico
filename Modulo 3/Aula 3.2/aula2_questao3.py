## Questão 3

# Solicita os dados
idade = int(input("Digite sua idade: "))
jogou_3_jogos = input("Já jogou pelo menos 3 jogos? (True/False): ") == "True"
vitorias = int(input("Quantas vezes você venceu um jogo? "))

# Verifica se pode entrar no clube
pode_entrar = (16 <= idade <= 18) and jogou_3_jogos and (vitorias >= 1)

# Exibe o resultado
print(pode_entrar)