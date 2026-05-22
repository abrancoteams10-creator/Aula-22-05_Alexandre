import streamlit as st
import pandas as pd

# Título
st.title("📊 Maiores Torcidas do Mundo")

# Ler CSV
df = pd.read_csv("torcidas.csv")

# Padronizar colunas
df.columns = df.columns.str.strip().str.lower()

# Mostrar dados
st.subheader("📋 Dados da Tabela")
st.dataframe(df)

# Ordenar para visual melhor
df = df.sort_values("torcedores_milhoes", ascending=False)

# Gráfico de barras verticais (colunas)
st.subheader("📈 Gráfico de Barras")

st.bar_chart(
    data=df,
    x="time",
    y="torcedores_milhoes"
)

# Destaque maior torcida
maior = df.iloc[0]

st.success(
    f"🔥 Maior torcida: {maior['time']} com {maior['torcedores_milhoes']} milhões de torcedores"
)
