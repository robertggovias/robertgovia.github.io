# Lista de palavras-chave
palavras_positivas = ["bom", "ótimo", "excelente", "maravilhoso", "gostei", "incrível"]
palavras_negativas = ["ruim", "péssimo", "horrível", "terrível", "odeio"]
palavras_neutras = ["mas", "deixou", "apesar", "embora"]

# Entrada do usuário
comentario = input("Digite um comentário: ")

# Dividir o comentário em palavras
palavras = comentario.lower().split()

# Contadores
positivas = 0
negativas = 0
neutras = 0

# Verificar cada palavra
for palavra in palavras:
    if palavra in palavras_positivas:
        positivas += 1
    elif palavra in palavras_negativas:
        negativas += 1
    elif palavra in palavras_neutras:
        neutras += 1

# Determinar o sentimento
if positivas > negativas:
    sentimento = "positivo"
elif negativas > positivas:
    sentimento = "negativo"
else:
    sentimento = "neutro"

print(f"Sentimento: {sentimento}")