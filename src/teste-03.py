import json

# Função para carregar dados do arquivo JSON
def carregar_dados(caminho_arquivo):
    with open(caminho_arquivo, 'r') as arquivo:
        return json.load(arquivo)

# Função para calcular métricas de faturamento
def calcular_metricas(dados):
    valores_validos = [item['valor'] for item in dados if item['valor'] > 0]
    menor = min(valores_validos)
    maior = max(valores_validos)
    media = sum(valores_validos) / len(valores_validos)
    dias_acima_media = sum(1 for valor in valores_validos if valor > media)
    return menor, maior, dias_acima_media

# Caminho do arquivo com os dados
arquivo_json = 'src/dados/dados.json'

# Processamento dos dados
dados_faturamento = carregar_dados(arquivo_json)
menor_faturamento, maior_faturamento, dias_acima_media = calcular_metricas(dados_faturamento)

# Exibir os resultados
print(f"Menor faturamento: {menor_faturamento:.2f}")
print(f"Maior faturamento: {maior_faturamento:.2f}")
print(f"Dias acima da média: {dias_acima_media}")


