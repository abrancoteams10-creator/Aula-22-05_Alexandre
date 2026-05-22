import streamlit as st
import pandas as pd

# Título da aplicação
st.title("📊 Maiores Torcidas do Mundo")

# Ler CSV (arquivo local)
df = pd.read_csv("torcidas.csv")

# Padronizar nomes das colunas
df.columns = df.columns.str.strip().str.lower()

# Mostrar tabela
st.subheader("📋 Tabela de Dados")
st.dataframe(df)

# Ordenar do maior para o menor
df = df.sort_values("torcedores_milhoes", ascending=False)

# Gráfico de colunas (vertical)
st.subheader("📈 Gráfico de Colunas")

dados_grafico = df.set_index("time")["torcedores_milhoes"]

st.column_chart(dados_grafico)

# Mostrar maior torcida
maior = df.iloc[0]

st.success(
    f"🔥 Maior torcida: {maior['time']} com {maior['torcedores_milhoes']} milhões de torcedores"
)
