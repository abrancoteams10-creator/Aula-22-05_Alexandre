import streamlit as st
import pandas as pd

st.title("📊 Maiores Torcidas do Mundo")

# Ler CSV
df = pd.read_csv("torcidas.csv")

# Mostrar tabela original
st.subheader("📋 Tabela de Dados")
st.dataframe(df)

# -----------------------------
# 🔧 CORREÇÃO PARA O GRÁFICO
# -----------------------------

# corrigir nomes das colunas
df.columns = df.columns.str.strip().str.lower()

# remover texto "milhoes" e converter para número
df["torcedores_milhoes"] = (
    df["torcedores_milhoes"]
    .astype(str)
    .str.replace("milhoes", "", regex=False)
    .str.replace(",", ".")
    .str.strip()
)

df["torcedores_milhoes"] = pd.to_numeric(df["torcedores_milhoes"], errors="coerce")

# remover linhas inválidas
df = df.dropna(subset=["torcedores_milhoes", "time"])

# ordenar
df = df.sort_values("torcedores_milhoes", ascending=False)

# -----------------------------
# 📈 GRÁFICO (AGORA FUNCIONA)
# -----------------------------
st.subheader("📈 Gráfico em Colunas")

st.bar_chart(df.set_index("time")["torcedores_milhoes"])

# destaque maior torcida
if not df.empty:
    maior = df.iloc[0]
    st.success(f"🔥 Maior torcida: {maior['time']} ({maior['torcedores_milhoes']} milhões)")
