import pandas as pd
import streamlit as st
import plotly.express as px


df = pd.read_csv("clientes_tratado.csv")

st.title("📊 Dashboard de Vendas")

col1, col2, col3 = st.columns(3)

col1.metric("Total de Vendas", len(df))
col2.metric("Faturamento Total", f"R$ {df['valor'].sum():.2f}")
col3.metric("Produtos", df["produto"].nunique())

st.subheader("💰 Faturamento por Região")

fat_regiao = df.groupby("regiao", as_index=False)["valor"].sum()

fig1 = px.bar(
    fat_regiao,
    x="regiao",
    y="valor",
    title="Faturamento por Região"
)

st.plotly_chart(fig1)

st.subheader("📦 Participação por Produto")

prod = df.groupby("produto", as_index=False)["valor"].sum()

fig2 = px.pie(
    prod,
    names="produto",
    values="valor",
    title="Participação de Receita por Produto"
)

st.plotly_chart(fig2)

st.subheader("📊 Status dos Pedidos")

status = df["status"].value_counts().reset_index()
status.columns = ["status", "quantidade"]

fig3 = px.bar(status, x="status", y="quantidade")

st.plotly_chart(fig3)

st.subheader("📄 Dados Brutos")
st.dataframe(df)

st.subheader("🧠 Insights Analíticos")

st.markdown("""
📍 **Concentração de Receita por Região**  
A análise indica concentração de faturamento em determinadas regiões, sugerindo oportunidade de expansão em mercados menos explorados.

📦 **Dependência de Produtos**  
A distribuição de receita por produto evidencia possíveis dependências de portfólio, exigindo diversificação estratégica.

📊 **Eficiência Operacional**  
A presença de pedidos em diferentes status permite avaliar a maturidade do processo operacional e possíveis gargalos.

📱 **Adoção de Plataforma**  
A distribuição por plataforma ajuda a entender o comportamento do cliente e priorizar melhorias de experiência.

💰 **Visão Geral de Performance**  
Os KPIs resumem o desempenho geral do período analisado, permitindo acompanhamento da evolução do negócio.
""")