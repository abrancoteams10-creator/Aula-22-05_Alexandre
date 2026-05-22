import streamlit as st
import pandas as pd

# Título da aplicação
st.title("Maiores Torcidas do Mundo")

# Ler arquivo CSV
df = pd.read_csv("torcidas.csv")

# Mostrar tabela
st.subheader("Tabela de Dados")
st.write(df)

# Criar gráfico de barras
st.subheader("Gráfico de Barras")

# Definir coluna de índice
grafico = df.set_index("time")

# Mostrar gráfico
st.bar_chart(grafico["torcedores_milhoes"])
