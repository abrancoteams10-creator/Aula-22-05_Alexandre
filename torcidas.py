import streamlit as st
import pandas as pd

st.title("📊 Maiores Torcidas do Mundo")

df = pd.read_csv("torcidas.csv")

df.columns = df.columns.str.strip().str.lower()

st.subheader("📋 Dados")
st.dataframe(df)

df = df.sort_values("torcedores_milhoes", ascending=False)

st.subheader("📈 Gráfico de Colunas (Vertical)")

st.column_chart(
    df.set_index("time")["torcedores_milhoes"]
)

maior = df.iloc[0]

st.success(f"🔥 Maior torcida: {maior['time']} ({maior['torcedores_milhoes']} milhões)")
