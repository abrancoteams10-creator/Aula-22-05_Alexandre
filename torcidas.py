import streamlit as st
import pandas as pd

st.title("📊 Maiores Torcidas do Mundo")

# Ler CSV
df = pd.read_csv("torcidas.csv")

# Padronizar colunas
df.columns = df.columns.str.strip().str.lower()

# Garantir que a coluna numérica é número
df["torcedores_milhoes"] = pd.to_numeric(df["torcedores_milhoes"], errors="coerce")

# Remover linhas com erro
df = df.dropna()

# Mostrar tabela
st.subheader("📋 Tabela de Dados")
st.dataframe(df)

# Ordenar
df = df.sort_values("torcedores_milhoes", ascending=False)

# Criar gráfico de colunas (FORMA MAIS SEGURA)
st.subheader("📈 Gráfico de Colunas")

st.bar_chart(
    data=df,
    x="time",
    y="torcedores_milhoes"
)

# Maior torcida
maior = df.iloc[0]

st.success(
    f"🔥 Maior torcida: {maior['time']} com {maior['torcedores_milhoes']} milhões de torcedores"
)
