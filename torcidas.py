import streamlit as st
import pandas as pd

# Título do app
st.title("📊 Torcidas de Futebol - Gráfico em Colunas")

# URL RAW do GitHub (troque pelo seu link)
url = "https://raw.githubusercontent.com/SEU_USUARIO/SEU_REPOSITORIO/main/torcidas.csv"

# Ler CSV
df = pd.read_csv(url)

# Padronizar nomes das colunas
df.columns = df.columns.str.strip().str.lower()

# Mostrar dados
st.subheader("📋 Dados do CSV")
st.dataframe(df)

# Garantir que a coluna numérica é número
df["torcedores_milhoes"] = pd.to_numeric(df["torcedores_milhoes"], errors="coerce")

# Remover linhas inválidas
df = df.dropna()

# Ordenar do maior para o menor
df = df.sort_values("torcedores_milhoes", ascending=False)

# 📊 GRÁFICO EM COLUNAS (VERTICAL)
st.subheader("📈 Gráfico em Colunas")

st.bar_chart(
    data=df,
    x="time",
    y="torcedores_milhoes"
)

# Destaque maior torcida
if not df.empty:
    maior = df.iloc[0]
    st.success(f"🔥 Maior torcida: {maior['time']} com {maior['torcedores_milhoes']} milhões")
