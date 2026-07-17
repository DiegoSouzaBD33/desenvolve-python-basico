## Questão 4

classe = str(input("Escolha a classe (guerreiro, mago ou arqueiro)")).lower()
pontos_força = int(input("Digite os pontos de força ( de 1 a 20): "))
pontos_magia = int(input("Digite os pontos de magia (de 1 a 20): "))

# Verifica se os atributos são válidos para a classe
if classe == "guerreiro":
    valido = (pontos_força >= 15) and (pontos_magia <= 10)

elif classe == "mago":
    valido = (pontos_força <= 10) and (pontos_magia >= 15)  

elif classe == "arqueiro":
    valido = (pontos_força > 5) and (pontos_força <= 15) and (pontos_magia >5) and (pontos_magia <=15)
else:
    valido= False

# Exibindo o resultado

print(valido)