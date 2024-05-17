# Importar bibliotecas necessárias
import pandas as pd
import json 
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import plotly.express as px

###### Criar um gráfico de barras da distribuição de gêneros - barChart #########

# Carregar o arquivo JSON contendo os gêneros de cada artista
with open('genero.json', 'r') as archive:
    generos_por_artista = json.load(archive)

# Carregar o arquivo CSV contendo os dados da playlist / Load data from CSV file 
df = pd.read_csv("./dataSet/playlist.csv")
""" 
#Lê o arquivo CSV e armazena os dados no DataFrame da biblioteca Pandas 
#Read the CSV file and store the data in a pandas DataFrame
"""

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
###################################################################################
##### Cria um Mapa de Calor com base no gênero e dia da semana ########

dfG = pd.read_csv("playlist_com_generos.csv")

# Converter a coluna 'items__addedDate' para tipo datetime
dfG['items__addedDate'] = pd.to_datetime(df['items__addedDate'])

# Extrair o dia da semana (0 = segunda-feira, 6 = domingo)
dfG['dia_da_semana'] = dfG['items__addedDate'].dt.weekday

# Criar uma tabela dinâmica para contagem de músicas por genero e dia da semana
tabela_dinamica = dfG.pivot_table(index='genero', 
    columns='dia_da_semana', 
    aggfunc='size', 
    fill_value=0
)

# Criar o mapa de calor
plt.figure(figsize=(12, 8))
sns.heatmap(tabela_dinamica, cmap="YlGnBu")
plt.xlabel("Dia da Semana")
plt.ylabel("Gênero")
plt.title("Frequência de Escuta por Gênero e Dia da Semana")
plt.show()
######################################################################################

###### Gráfico de Barras empilhadas personalizado(Generos musicais e artistas) #######

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
dfG['genero'] = df['items__track__artistName'].map(genero_map)

dfG.to_csv("playlist_com_generos.csv", index=False)

df_generos = pd.DataFrame(generos_classificados, columns=['artista', 'genero'])


# Criar uma tabela de contingência para contar as músicas por artista e gênero
contagem_generos = pd.crosstab(dfG['items__track__artistName'], dfG['genero'])

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
######################################################################################
###### Cria o gráfico de linha temporal de adição de músicas na playlist #############

# Converter a coluna 'items__addedDate' para tipo datetime
df['items__addedDate'] = pd.to_datetime(df['items__addedDate'])

# Agrupar músicas por data e contar
adicoes_por_data = df.groupby(df['items__addedDate'].dt.date).size()

# Criar o gráfico de linha temporal
plt.figure(figsize=(10, 6))
plt.plot(adicoes_por_data.index, adicoes_por_data.values)
plt.xlabel("Data")
plt.ylabel("Número de Músicas Adicionadas")
plt.title("Adições de Músicas ao Longo do Tempo")
plt.show()
#######################################################################################
####### Cria a nuvem de palavras das músicas da playlist ########

# Extrair nomes dos artistas e contar frequência / Extract artist names and count frequencies
artistas = df["items__track__artistName"].value_counts().to_dict()

# Gerar a nuvem de palavras / Generate word cloud
wordcloud = WordCloud(background_color="white", width=800, height=600).generate_from_frequencies(artistas)
"""
#Cria a nuvem de palavras com a biblioteca WordCloud, determina a cor do plano de fundo e especifica o tamanho
#Generate a word cloud using the WordCloud library with a white background and specified width and height
"""

# Exibir a nuvem de palavras / Display word cloud
plt.figure(figsize=(10, 8)) 
# Cria uma nova figura determinado o tamanho com a bilbioteca matplotlib.pyplot 
#/ Create a new figure with a specified size

plt.imshow(wordcloud, interpolation="bilinear")
# Exibir a nuvem de palavra criada anteriormente na figura
# Display the word cloud on the figure

plt.axis("off")
# Desativa os eixos do gráfico.
# Turn off the axis for the figure

plt.show()
# Mostra a figura
# Display the figure
######################################################################################
#### Gráfico de barras com o Plotly que permiti a exploração dinâmica dos dados ######

# Criar um gráfico de barras interativo com Plotly
fig = px.bar(dfG, x="items__addedDate", y="items__track__artistName", color="genero") 
fig.show()