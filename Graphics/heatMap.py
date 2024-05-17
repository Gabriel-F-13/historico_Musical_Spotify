import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv("playlist_com_generos.csv")

# Converter a coluna 'items__addedDate' para tipo datetime
df['items__addedDate'] = pd.to_datetime(df['items__addedDate'])

# Extrair o dia da semana (0 = segunda-feira, 6 = domingo)
df['dia_da_semana'] = df['items__addedDate'].dt.weekday

# Criar uma tabela dinâmica para contagem de músicas por genero e dia da semana
tabela_dinamica = df.pivot_table(index='genero', 
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