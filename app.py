import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# CONFIGURAÇÃO
st.set_page_config(
    page_title="Dashboard de Funcionários",
    layout="wide"
)

st.title("📊 Dashboard de Análise de Funcionários")

uploaded_file = st.sidebar.file_uploader("Envie um CSV", type=["csv"])

@st.cache_data
def carregar_dados():
    dados = {
        "nome": ["Ana", "Bruno", "Carlos", "Daniela", "Eduardo"],
        "idade": [23, 35, 29, np.nan, 40],
        "cidade": ["SP", "RJ", "SP", "MG", "RJ"],
        "salario": [3000, 5000, 4000, 3500, np.nan],
        "data_contratacao": pd.to_datetime([
            "2020-01-01", "2019-05-10", "2021-07-15",
            "2018-03-20", "2022-08-01"
        ])
    }

    df = pd.DataFrame(dados)

    # limpeza
    df["idade"] = df["idade"].fillna(df["idade"].mean())
    df["salario"] = df["salario"].fillna(df["salario"].median())

    # features
    df["salario_anual"] = df["salario"] * 12
    df["ano_contratacao"] = df["data_contratacao"].dt.year

    return df

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    # recriar categoria (IMPORTANTE)
    df["categoria_salario"] = df["salario"].apply(
        lambda x: "Alto" if x > 4500 else "Médio" if x > 3000 else "Baixo"
    )
else:
    df = carregar_dados()

    df["categoria_salario"] = df["salario"].apply(
        lambda x: "Alto" if x > 4500 else "Médio" if x > 3000 else "Baixo"
    )

st.sidebar.header("🔎 Filtros")

cidades = st.sidebar.multiselect(
    "Selecione a cidade",
    options=df["cidade"].unique(),
    default=df["cidade"].unique()
)

faixa_salario = st.sidebar.slider(
    "Faixa salarial",
    float(df["salario"].min()),
    float(df["salario"].max()),
    (float(df["salario"].min()), float(df["salario"].max()))
)

categoria = st.sidebar.selectbox(
    "Categoria salarial",
    options=["Todas"] + list(df["categoria_salario"].unique())
)

df_filtrado = df[
    (df["cidade"].isin(cidades)) &
    (df["salario"] >= faixa_salario[0]) &
    (df["salario"] <= faixa_salario[1])
]

# filtro novo
if categoria != "Todas":
    df_filtrado = df_filtrado[df_filtrado["categoria_salario"] == categoria]

st.write("Dados filtrados:", df_filtrado.shape[0], "linhas")

col1, col2, col3 = st.columns(3)

col1.metric("💰 Salário Médio", f"R$ {df_filtrado['salario'].mean():.2f}")
col2.metric("👥 Total Funcionários", df_filtrado.shape[0])
col3.metric("📈 Salário Máximo", f"R$ {df_filtrado['salario'].max():.2f}")

st.subheader("📋 Dados")
st.dataframe(df_filtrado, use_container_width=True)

st.subheader("📊 Análises")

col1, col2 = st.columns(2)

# Gráfico 1
fig1 = px.bar(
    df_filtrado,
    x="cidade",
    y="salario",
    color="categoria_salario",
    title="Salário por Cidade",
    hover_data=["nome", "salario", "categoria_salario"]
)

col1.plotly_chart(fig1, use_container_width=True)

# Gráfico 2
fig2 = px.histogram(
    df_filtrado,
    x="categoria_salario",
    color="categoria_salario",
    title="Distribuição por Categoria"
)

col2.plotly_chart(fig2, use_container_width=True)

pivot = pd.pivot_table(
    df_filtrado,
    values="salario",
    index="cidade",
    columns="categoria_salario",
    aggfunc="mean"
)

st.subheader("📊 Pivot Table")
st.dataframe(pivot)

csv = df_filtrado.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Baixar CSV",
    data=csv,
    file_name="dados_filtrados.csv",
    mime="text/csv"
)