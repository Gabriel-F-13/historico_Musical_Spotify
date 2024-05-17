import pandas as pd
import matplotlib.pyplot as plt
import json 

"""
Gráfico de Barras empilhadas personalizado(Generos musicais e artistas)
"""

with open('C:/Users/gabri/Desktop/Imersao_AI/Challenges/Class1/historico_Spotify/genero.json', 'r') as archive:
    generos_por_artista = json.load(archive)


# Carregar dados do CSV
df = pd.read_csv("./dataSet/playlist.csv")

# Obter lista de artistas únicos
artistas = df['items__track__artistName'].unique()

# Remover valores ausentes (NaN)
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
        generos_classificados.append((artista, genero))
    else:
        genero = "Desconhecido"  # Ou implementar lógica de inferência

# Criar um dicionário para mapear artistas para gêneros classificados
genero_map = {artista: genero for artista, genero in generos_classificados}

# Mapear os gêneros classificados para o DataFrame original
df['genero'] = df['items__track__artistName'].map(genero_map)

df.to_csv("playlist_com_generos.csv", index=False)

df_generos = pd.DataFrame(generos_classificados, columns=['artista', 'genero'])


# Criar uma tabela de contingência para contar as músicas por artista e gênero
contagem_generos = pd.crosstab(df['items__track__artistName'], df['genero'])

##Criar o gráfico de barras empilhadas
ax = contagem_generos.plot(kind='bar', stacked=True, figsize=(12, 6), legend=True)
plt.xlabel("Artista com mais de 4 músicas na playlist")
plt.ylabel("Número de Músicas")
plt.title("Distribuição de Gêneros Musicais por Artista")

# Adicionar rótulos do eixo x condicionalmente
labels = []
for j in range(len(contagem_generos.index)):
    artista = contagem_generos.index[j]
    num_musicas = contagem_generos.sum(axis=1)[j]
    if num_musicas > 4:
        labels.append(artista)
    else:
        labels.append("")

ax.set_xticklabels(labels, rotation=45, ha='right')

# Adicionar legenda
plt.legend(title="Gênero", bbox_to_anchor=(1, 0.5), labels=contagem_generos.columns)
plt.tight_layout()
plt.show()