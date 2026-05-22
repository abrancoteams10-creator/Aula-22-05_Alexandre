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

# Ordenar dados (IMPORTANTE para gráfico ficar bonito)
df = df.sort_values("torcedores_milhoes", ascending=True)

# Criar gráfico com Streamlit (melhor que matplotlib aqui)
st.subheader("📈 Gráfico de Barras")

st.bar_chart(
    df.set_index("time")["torcedores_milhoes"]
)

# Destaque extra: maior torcida
maior = df.loc[df["torcedores_milhoes"].idxmax()]

st.success(
    f"🔥 Maior torcida: {maior['time']} com {maior['torcedores_milhoes']} milhões de torcedores"
)
