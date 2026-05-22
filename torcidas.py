import streamlit as st
import pandas as pd

# Título
st.title("Maiores Torcidas do Mundo")

# Ler CSV
df = pd.read_csv("torcidas.csv")

# Remover espaços e padronizar nomes das colunas
df.columns = df.columns.str.strip().str.lower()

# Mostrar tabela
st.subheader("Tabela de Dados")
st.write(df)

# Mostrar nomes das colunas
st.write("Colunas encontradas:")
st.write(df.columns)

# Criar gráfico
st.subheader("Gráfico de Barras")

# Definir índice
grafico = df.set_index("time")

# Mostrar gráfico
st.bar_chart(grafico["torcedores_milhoes"])
