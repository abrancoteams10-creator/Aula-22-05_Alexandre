import streamlit as st
import pandas as pd

st.title("📊 Torcidas de Futebol")

# Ler CSV
df = pd.read_csv("torcidas.csv")

# Mostrar colunas (DEBUG IMPORTANTE)
st.write("🔎 Colunas encontradas:", df.columns)

# Padronizar nomes
df.columns = df.columns.str.strip().str.lower()

# Conferir dados brutos
st.subheader("📋 Dados originais")
st.dataframe(df)

# Converter valores para número (FORÇADO)
df["torcedores_milhoes"] = (
    df["torcedores_milhoes"]
    .astype(str)
    .str.replace(",", ".")
)

df["torcedores_milhoes"] = pd.to_numeric(df["torcedores_milhoes"], errors="coerce")

# Remover linhas inválidas
df = df.dropna()

# Ordenar
df = df.sort_values("torcedores_milhoes", ascending=False)

# 🔥 TESTE: mostrar dados usados no gráfico
st.subheader("📊 Dados do gráfico")
st.dataframe(df[["time", "torcedores_milhoes"]])

# GRÁFICO
st.subheader("📈 Gráfico em Colunas")

st.bar_chart(df.set_index("time")["torcedores_milhoes"])

# Maior torcida
if not df.empty:
    maior = df.iloc[0]
    st.success(f"🔥 Maior torcida: {maior['time']} ({maior['torcedores_milhoes']} milhões)")
else:
    st.error("❌ Nenhum dado válido para o gráfico")
