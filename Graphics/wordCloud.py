import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Carregar dados do CSV / Load data from CSV file
df = pd.read_csv("./dataSet/playlist.csv") 
""" 
#Lê o arquivo CSV e armazena os dados no DataFrame da biblioteca Pandas 
#Read the CSV file and store the data in a pandas DataFrame
"""

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