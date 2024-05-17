# Importar bibliotecas necessárias
import pandas as pd
import matplotlib.pyplot as plt
import json 

# Carregar o arquivo JSON contendo os gêneros de cada artista
with open('C:/Users/gabri/Desktop/Imersao_AI/Challenges/Class1/historico_Spotify/genero.json', 'r') as archive:
    generos_por_artista = json.load(archive)

# Carregar o arquivo CSV contendo os dados da playlist
df = pd.read_csv("./dataSet/playlist.csv")

# Obter uma lista de artistas únicos da playlist
artistas = df['items__track__artistName'].unique()

# Remover valores ausentes (NaN) da lista de artistas
artistNaN = artistas[~pd.isna(artistas)]

# Imprimir a lista de artistas
print("Lista de Artistas:")
for artista in artistas:
    print(artista)

# Classificar o gênero de cada artista
generos_classificados = []
for artista in artistas:
    if artista in generos_por_artista :
        genero = generos_por_artista[artista]
    else:
        genero = "Desconhecido"  # Ou implementar lógica de inferência
    generos_classificados.append((artista, genero))

# Criar um novo DataFrame df_generos a partir da lista generos_classificados
df_generos = pd.DataFrame(generos_classificados, columns=['artista', 'genero'])

# Contar o número de ocorrências de cada gênero
generos_contados = df_generos['genero'].value_counts()

# Criar um gráfico de barras da distribuição de gêneros
generos_contados.plot(kind='bar', title='Distribuição de Gêneros')
plt.xlabel('Gênero')
plt.ylabel('Contagem')
plt.show()
plt.savefig("grafico_generos.pdf")  # Salvar como PDF