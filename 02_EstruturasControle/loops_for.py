# ============================================
# ARQUIVO: loops_for.py
# PASTA: 02_EstruturasControle
# OBJETIVO: Iterar sobre listas de dados (simulando linhas de uma planilha)
# ============================================

# Lista de dicionários (simula linhas de uma planilha ou banco de dados)
vendas = [
    {"cliente": "João Silva", "produto": "Notebook", "valor": 4500.00},
    {"cliente": "Maria Santos", "produto": "Impressora", "valor": 850.00},
    {"cliente": "Pedro Oliveira", "produto": "Mouse", "valor": 150.00},
    {"cliente": "Ana Costa", "produto": "Teclado", "valor": 300.00},
       {"cliente": "Carlos Souza", "produto": "Monitor", "valor": 1200.00},
]

print("=" * 70)
print("RELATÓRIO DE VENDAS DETALHADO")
print("=" * 70)

total_geral = 0.0
contador_vendas = 0

# Loop FOR para percorrer cada "linha" (dicionário) da lista
for venda in vendas:
    cliente = venda["cliente"]
    produto = venda["produto"]
    valor = venda["valor"]
    
    # Regra de negócio: Desconto de 10% para vendas acima de 1000
    if valor >= 1000.00:
        valor_com_desconto = valor * 0.90
        status = "COM DESCONTO (10%)"
    else:
        valor_com_desconto = valor
        status = "PREÇO NORMAL"
        
    total_geral += valor_com_desconto
    contador_vendas += 1
    
    # Formatação com alinhamento (<16 significa alinhado à esquerda, 16 espaços)
    print(f"Cliente: {cliente:<16} | Produto: {produto:<10} | Valor: R$ {valor_com_desconto:>7.2f} | {status}")

print("-" * 70)
print(f"Total de vendas processadas: {contador_vendas}")
print(f"FATURAMENTO TOTAL FINAL:     R$ {total_geral:.2f}")
print("=" * 70)