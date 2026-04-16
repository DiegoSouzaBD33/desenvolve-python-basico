# Solicita ao usuário uma temperatura em graus Fahrenheit (valor inteiro)
fahrenheit = int(input("Digite a temperatura em Fahrenheit: "))

# Aplica a fórmula de conversão para Celsius
celsius = (fahrenheit - 32) * (5/9)

# Converte o valor de Celsius para inteiro antes de exibir
celsius = int(celsius)

# Exibe o resultado no formato solicitado
print(f"{fahrenheit} graus Fahrenheit são {celsius} graus Celsius.")