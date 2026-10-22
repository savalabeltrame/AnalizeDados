# ============================================
# ARQUIVO: variaveis_tipos.py
# PASTA: 01_Fundamentos
# OBJETIVO: Aprender sobre variáveis e tipos de dados
# ============================================

# 1. VARIÁVEIS DO TIPO STRING (texto)
nome_cliente = "JMaria Santos"
produto = "impresora HP"

# 2. VARIÁVEIS DO TIPO INT (número inteiro)
quantidade = 5

# 3. VARIÁVEIS DO TIPO FLOAT (número decimal)
preco_unitario = 850.00
desconto = 0.15  # 10% de desconto

# 4. CÁLCULOS
subtotal = quantidade * preco_unitario
valor_desconto = subtotal * desconto
total_final = subtotal - valor_desconto

# 5. EXIBIR RESULTADOS
print("=" * 50)
print("RELATÓRIO DE VENDA")
print("=" * 50)
print(f"Cliente: {nome_cliente}")
print(f"Produto: {produto}")
print(f"Quantidade: {quantidade} unidades")
print(f"Preço unitário: R$ {preco_unitario:.2f}")
print("-" * 50)
print(f"Subtotal: R$ {subtotal:.2f}")
print(f"Desconto (10%): - R$ {valor_desconto:.2f}")
print(f"TOTAL FINAL: R$ {total_final:.2f}")
print("=" * 50)

# 6. VERIFICAR TIPOS DE DADOS
print("\nTipos de dados das variáveis:")
print(f"nome_cliente é do tipo: {type(nome_cliente)}")
print(f"quantidade é do tipo: {type(quantidade)}")
print(f"preco_unitario é do tipo: {type(preco_unitario)}")