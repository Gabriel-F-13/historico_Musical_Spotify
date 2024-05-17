import pandas as pd
import matplotlib.pyplot as plt

# Carregar dados do CSV
df = pd.read_csv("./dataSet/playlist.csv")

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