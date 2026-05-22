import streamlit as st
import pandas as pd

# Título
st.title("Maiores Torcidas do Mundo")

# Ler CSV
df = pd.read_csv("torcidas.csv")

# Mostrar colunas existentes
st.write("Colunas do CSV:")
st.write(df.columns)

# Mostrar tabela
st.subheader("Tabela de Dados")
st.write(df)

# Verificar se as colunas existem
if "time" in df.columns and "torcedores_milhoes" in df.columns:

    # Criar gráfico
    st.subheader("Gráfico de Barras")

    grafico = df.set_index("time")

    st.bar_chart(grafico["torcedores_milhoes"])

else:
    st.error(
        "As colunas 'time' e/ou 'torcedores_milhoes' não foram encontradas no CSV."
    )
