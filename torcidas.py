import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Título da aplicação
st.title("Maiores Torcidas do Mundo")

# Caminho do CSV
# Se estiver no GitHub RAW, coloque a URL
# Se estiver localmente, coloque o nome do arquivo

url = "https://raw.githubusercontent.com/SEU-USUARIO/SEU-REPOSITORIO/main/torcidas.csv"

# Ler CSV
df = pd.read_csv(url)

# Mostrar tabela
st.subheader("Tabela de Dados")
st.write(df)

# Criar gráfico
fig, ax = plt.subplots()

# Gráfico de barras
ax.bar(df["time"], df["torcedores_milhoes"], color="blue")

# Configurações do gráfico
ax.set_title("Top 12 Maiores Torcidas do Mundo")
ax.set_xlabel("Times")
ax.set_ylabel("Torcedores (milhões)")

# Rotacionar nomes
plt.xticks(rotation=45)

# Mostrar gráfico
st.pyplot(fig)
