# Função que realiza a inversão de uma string sem usar métodos prontos
def inverter_texto(frase):
    invertida = ""  # Armazena o texto invertido
    indice = len(frase) - 1  # Inicia no último caractere
    while indice >= 0:  # Continua até o início da string
        invertida += frase[indice]  # Adiciona o caractere atual
        indice -= 1  # Move para o próximo índice
    return invertida

# Texto de entrada (pode ser alterado para usar input do usuário)
texto_original = "Eu vou ser contrata para essa vaga de dev"
texto_invertido = inverter_texto(texto_original)

# Exibe os resultados
print("Texto original:", texto_original)
print("Texto invertido:", texto_invertido)
