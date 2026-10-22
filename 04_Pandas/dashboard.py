# ============================================
# ARQUIVO: dashboard.py (Versão Bilingue)
# PASTA: 04_Pandas
# OBJETIVO: Dashboard com seletor de idioma (PT/ES)
# ============================================

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ============================================
# DICIONÁRIO DE TRADUÇÕES
# ============================================
traducoes = {
    "pt": {
        "titulo": "📊 Dashboard de Análise de Vendas",
        "navegacao": "🎯 Navegação",
        "escolha_secao": "Escolha uma seção:",
        "visao_geral": "📈 Visão Geral",
        "ranking": "🏆 Ranking de Categorias",
        "premium": "💎 Produtos Premium",
        "dados_completos": "📋 Dados Completos",
        
        # Visão Geral
        "metricas_gerais": "📈 Métricas Gerais do Negócio",
        "faturamento_total": "Faturamento Total",
        "acumulado": "Acumulado",
        "total_itens": "Total de Itens Vendidos",
        "unidades": "unidades",
        "quantidade": "Quantidade",
        "ticket_medio": "Ticket Médio",
        "por_venda": "Por venda",
        "faturamento_categoria": "Faturamento por Categoria",
        
        # Ranking
        "ranking_desempenho": "🏆 Ranking de Desempenho por Categoria",
        "categoria_campea": "🏆 Categoria Campeã:",
        
        # Premium
        "analise_premium": "💎 Análise de Produtos Premium (Preço > R$ 10.00)",
        "filtrar_preco": "Filtrar por preço mínimo:",
        "encontrados": "Encontrados",
        "produtos_com_preco": "produtos com preço >=",
        "exportar_csv": "📥 Exportar para CSV",
        "arquivo_exportado": "✅ Arquivo exportado com sucesso!",
        
        # Dados Completos
        "tabela_completa": "📋 Tabela Completa de Vendas",
        "visualize_dados": "Visualize todos os dados brutos processados:",
        "baixar_dados": "📥 Baixar Dados Completos (CSV)",
        
        # Rodapé
        "rodape": "Dashboard criado com Python + Streamlit | Análise de Dados Profissional"
    },
    "es": {
        "titulo": "📊 Dashboard de Análisis de Ventas",
        "navegacao": "🎯 Navegación",
        "escolha_secao": "Elige una sección:",
        "visao_geral": "📈 Visión General",
        "ranking": "🏆 Ranking de Categorías",
        "premium": "💎 Productos Premium",
        "dados_completos": "📋 Datos Completos",
        
        # Visión General
        "metricas_gerais": "📈 Métricas Generales del Negocio",
        "faturamento_total": "Ingresos Totales",
        "acumulado": "Acumulado",
        "total_itens": "Total de Artículos Vendidos",
        "unidades": "unidades",
        "quantidade": "Cantidad",
        "ticket_medio": "Ticket Promedio",
        "por_venda": "Por venta",
        "faturamento_categoria": "Ingresos por Categoría",
        
        # Ranking
        "ranking_desempenho": "🏆 Ranking de Desempeño por Categoría",
        "categoria_campea": "🏆 Categoría Ganadora:",
        
        # Premium
        "analise_premium": "💎 Análisis de Productos Premium (Precio > R$ 10.00)",
        "filtrar_preco": "Filtrar por precio mínimo:",
        "encontrados": "Encontrados",
        "produtos_com_preco": "productos con precio >=",
        "exportar_csv": "📥 Exportar a CSV",
        "arquivo_exportado": "✅ ¡Archivo exportado con éxito!",
        
        # Datos Completos
        "tabela_completa": "📋 Tabla Completa de Ventas",
        "visualize_dados": "Visualiza todos los datos procesados:",
        "baixar_dados": "📥 Descargar Datos Completos (CSV)",
        
        # Rodapé
        "rodape": "Dashboard creado con Python + Streamlit | Análisis de Datos Profesional"
    }
}

# ============================================
# CONFIGURAÇÃO INICIAL
# ============================================
st.set_page_config(page_title="Dashboard Cafe&Marmitas", layout="wide")

# ============================================
# SELETOR DE IDIOMA (Sidebar)
# ============================================
st.sidebar.header("🌐 Idioma / Language")
idioma = st.sidebar.radio(
    "Selecione / Select:",
    ["🇧🇷 Português", "🇪🇸 Español"],
    index=0
)

# Mapear para código do idioma
if "Português" in idioma:
    lang = "pt"
else:
    lang = "es"

# Carregar traduções
t = traducoes[lang]

# ============================================
# TÍTULO PRINCIPAL
# ============================================
st.title(t["titulo"])
st.markdown("---")

# ============================================
# CARREGAR DADOS
# ============================================
@st.cache_data
def carregar_dados():
    df = pd.read_csv("vendas_cafe.csv")
    df["Faturamento"] = df["Quantidade"] * df["Preco_Unitario"]
    return df

df = carregar_dados()

# ============================================
# MENU LATERAL (Navegação)
# ============================================
st.sidebar.header(t["navegacao"])
opcao = st.sidebar.radio(
    t["escolha_secao"],
    [t["visao_geral"], t["ranking"], t["premium"], t["dados_completos"]]
)

# ============================================
# SEÇÃO 1: VISÃO GERAL
# ============================================
if opcao == t["visao_geral"]:
    st.header(t["metricas_gerais"])
    
    total_faturamento = df["Faturamento"].sum()
    total_vendas = df["Quantidade"].sum()
    ticket_medio = total_faturamento / len(df)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(
            label=t["faturamento_total"],
            value=f"R$ {total_faturamento:.2f}",
            delta=t["acumulado"]
        )
    
    with col2:
        st.metric(
            label=t["total_itens"],
            value=f"{int(total_vendas)} {t['unidades']}",
            delta=t["quantidade"]
        )
    
    with col3:
        st.metric(
            label=t["ticket_medio"],
            value=f"R$ {ticket_medio:.2f}",
            delta=t["por_venda"]
        )
    
    st.markdown("---")
    
    st.subheader(t["faturamento_categoria"])
    resumo = df.groupby("Categoria")["Faturamento"].sum()
    
    fig, ax = plt.subplots(figsize=(10, 5))
    resumo.plot(kind='bar', color=['#4CAF50', '#FF9800', '#2196F3', '#9C27B0'], ax=ax)
    plt.title(t["faturamento_categoria"], fontsize=14, fontweight='bold')
    plt.xlabel("Categoria")
    plt.ylabel("Valor (R$)")
    plt.xticks(rotation=0)
    plt.tight_layout()
    
    st.pyplot(fig)

# ============================================
# SEÇÃO 2: RANKING
# ============================================
elif opcao == t["ranking"]:
    st.header(t["ranking_desempenho"])
    
    resumo = df.groupby("Categoria").agg({
        "Faturamento": "sum",
        "Quantidade": "sum"
    }).sort_values("Faturamento", ascending=False)
    
    resumo["Ticket Médio"] = resumo["Faturamento"] / resumo["Quantidade"]
    
    categoria_campea = resumo.index[0]
    st.success(f"{t['categoria_campea']} **{categoria_campea}**")
    
    st.dataframe(resumo, use_container_width=True)

# ============================================
# SEÇÃO 3: PRODUTOS PREMIUM
# ============================================
elif opcao == t["premium"]:
    st.header(t["analise_premium"])
    
    preco_minimo = st.slider(
        t["filtrar_preco"],
        min_value=0.0,
        max_value=50.0,
        value=10.0,
        step=1.0
    )
    
    df_premium = df[df["Preco_Unitario"] >= preco_minimo]
    
    st.write(f"{t['encontrados']} **{len(df_premium)}** {t['produtos_com_preco']} R$ {preco_minimo:.2f}")
    
    st.dataframe(
        df_premium[["Produto", "Categoria", "Quantidade", "Preco_Unitario", "Faturamento"]],
        use_container_width=True
    )
    
    if st.button(t["exportar_csv"]):
        df_premium.to_csv("produtos_premium_dashboard.csv", index=False)
        st.success(t["arquivo_exportado"])

# ============================================
# SEÇÃO 4: DADOS COMPLETOS
# ============================================
elif opcao == t["dados_completos"]:
    st.header(t["tabela_completa"])
    
    st.write(t["visualize_dados"])
    st.dataframe(df, use_container_width=True)
    
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label=t["baixar_dados"],
        data=csv,
        file_name='vendas_completas.csv',
        mime='text/csv'
    )

# ============================================
# RODAPÉ
# ============================================
st.markdown("---")
st.markdown(
    f"""
    <div style='text-align: center; color: gray;'>
        <small>{t['rodape']}</small>
    </div>
    """,
    unsafe_allow_html=True
)