# Questão 4

saldo = 500.00  # valor inicial
juros = 0.01    # taxa de juros mensal (1%)

for _ in range(3):
    saldo += saldo * juros

print(f"Saldo após 3 meses: R${saldo:.2f}")

