# ============================================
# ARQUIVO: intro_pandas.py
# PASTA: 04_Pandas
# OBJETIVO: Ver o poder do Pandas para análise de dados
# ============================================

import pandas as pd

# 1. Criar os dados (o mesmo que fizemos antes, mas agora o Pandas organiza tudo)
dados_vendas = {
    "Cliente": ["João Silva", "Maria Santos", "Pedro Oliveira", "Ana Costa", "Carlos Souza"],
    "Produto": ["Notebook", "Impressora", "Mouse", "Teclado", "Monitor"],
    "Valor": [4500.00, 850.00, 150.00, 300.00, 1200.00]
}

# 2. Transformar em um DataFrame (uma "planilha" do Python)
df = pd.DataFrame(dados_vendas)

print("=" * 60)
print("TABELA ORIGINAL (DATAFRAME)")
print("=" * 60)
print(df)
print("\n")

# 3. Aplicar a regra de desconto de forma VETORIZADA (muito mais rápido que o loop 'for')
# Cria uma nova coluna: se Valor >= 1000, multiplica por 0.90, senão, mantém o Valor
df["Valor_Final"] = df["Valor"].apply(lambda x: x * 0.90 if x >= 1000 else x)

print("=" * 60)
print("TABELA COM DESCONTO APLICADO")
print("=" * 60)
print(df)
print("\n")

# 4. Análise instantânea: Somar tudo e contar
total_faturamento = df["Valor_Final"].sum()
total_vendas = len(df)

print("=" * 60)
print("RESUMO AUTOMÁTICO")
print("=" * 60)
print(f"Total de vendas processadas: {total_vendas}")
print(f"FATURAMENTO TOTAL FINAL:     R$ {total_faturamento:.2f}")
print("=" * 60)