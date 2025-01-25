# Dicionário com os valores de faturamento por estado
faturamento_estados = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

# Calcula o total de faturamento
total_faturamento = sum(faturamento_estados.values())

# Função para calcular o percentual
def calcular_percentual(faturamento, total):
    return (faturamento / total) * 100

# Exibição dos percentuais por estado
print("Percentual de representação por estado:")
for estado, valor in faturamento_estados.items():
    percentual = calcular_percentual(valor, total_faturamento)
    print(f"{estado}: {percentual:.2f}%")
