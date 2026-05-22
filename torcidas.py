import streamlit as st
import pandas as pd

st.title("📊 Torcidas de Futebol")

# Lê arquivo LOCAL (mesma pasta do app)
df = pd.read_csv("torcidas.csv")

df.columns = df.columns.str.strip().str.lower()

st.subheader("📋 Dados")
st.dataframe(df)

df["torcedores_milhoes"] = pd.to_numeric(df["torcedores_milhoes"], errors="coerce")
df = df.dropna()

df = df.sort_values("torcedores_milhoes", ascending=False)

st.subheader("📈 Gráfico em Colunas")

st.bar_chart(df.set_index("time")["torcedores_milhoes"])

if not df.empty:
    maior = df.iloc[0]
    st.success(f"🔥 Maior torcida: {maior['time']} ({maior['torcedores_milhoes']} milhões)")
