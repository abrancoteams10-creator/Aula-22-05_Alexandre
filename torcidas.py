import streamlit as st
import pandas as pd

st.title("📊 Maiores Torcidas do Mundo")

# Ler CSV
df = pd.read_csv("torcidas.csv")

# Padronizar colunas
df.columns = df.columns.str.strip().str.lower()

# Mostrar colunas (DEBUG IMPORTANTE)
st.write("Colunas encontradas:", df.columns)

# Verificar se está vazio
if df.empty:
    st.error("❌ O CSV está vazio ou não foi lido corretamente.")
    st.stop()

# Converter número com segurança
if "torcedores_milhoes" in df.columns:
    df["torcedores_milhoes"] = pd.to_numeric(df["torcedores_milhoes"], errors="coerce")
else:
    st.error("❌ Coluna 'torcedores_milhoes' não encontrada no CSV.")
    st.stop()

# Remover apenas linhas inválidas nessa coluna
df = df.dropna(subset=["torcedores_milhoes"])

# Ordenar
df = df.sort_values("torcedores_milhoes", ascending=False)

# Mostrar tabela
st.subheader("📋 Tabela de Dados")
st.dataframe(df)

# Gráfico seguro
st.subheader("📈 Gráfico de Colunas")

st.bar_chart(df.set_index("time")["torcedores_milhoes"])

# Maior torcida (só se tiver dados)
if not df.empty:
    maior = df.iloc[0]
    st.success(f"🔥 Maior torcida: {maior['time']} ({maior['torcedores_milhoes']} milhões)")
else:
    st.warning("⚠️ Sem dados para exibir")
