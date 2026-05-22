import streamlit as st
import pandas as pd

# Título da aplicação
st.title("📊 Maiores Torcidas do Mundo")

# Ler CSV
df = pd.read_csv("torcidas.csv")

# Mostrar dados originais
st.subheader("📋 Tabela de Dados")
st.dataframe(df)

# -----------------------------
# 🔧 PARTE ADICIONADA (SUA CORREÇÃO)
# -----------------------------

# corrigir espaços nos nomes
df.columns = df.columns.str.strip().str.lower()

# garantir que existe dado válido
df = df.dropna(subset=["time", "torcedores_milhoes"])

# converter número de forma segura
df["torcedores_milhoes"] = df["torcedores_milhoes"].astype(str)
df["torcedores_milhoes"] = df["torcedores_milhoes"].str.replace(",", ".")
df["torcedores_milhoes"] = pd.to_numeric(df["torcedores_milhoes"], errors="coerce")

# remover só valores inválidos da coluna numérica
df = df.dropna(subset=["torcedores_milhoes"])

# ordenar
df = df.sort_values("torcedores_milhoes", ascending=False)

# -----------------------------

# 🔥 GRÁFICO (FUNCIONANDO)
st.subheader("📈 Gráfico em Colunas")

st.bar_chart(df.set_index("time")["torcedores_milhoes"])

# Mostrar maior torcida (opcional mas útil)
if not df.empty:
    maior = df.iloc[0]
    st.success(f"🔥 Maior torcida: {maior['time']} ({maior['torcedores_milhoes']} milhões)")
