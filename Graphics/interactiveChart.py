import plotly.express as px
import pandas as pd

# Carregar dados do CSV
df = pd.read_csv("playlist_com_generos.csv")

# Criar um gráfico de barras interativo com Plotly
fig = px.bar(df, x="items__addedDate", y="items__track__artistName", color="genero") 
fig.show()