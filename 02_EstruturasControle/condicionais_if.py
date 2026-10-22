# ============================================
# ARQUIVO: condicionais_if.py
# PASTA: 02_EstruturasControle
# OBJETIVO: Aprender a tomar decisões no código (if, elif, else)
# ============================================

# 1. Definir variáveis
nome_vendedor = "Carlos"
total_venda = 2000# Este é o valor que calculamos no exercício anterior
meta_venda = 3000.00

print("=" * 50)
print(f"RELATÓRIO DE DESEMPENHO: {nome_vendedor}")
print("=" * 50)
print(f"Total da venda: R$ {total_venda:.2f}")
print(f"Meta estabelecida: R$ {meta_venda:.2f}")
print("-" * 50)

# 2. Estrutura Condicional (if / elif / else)
if total_venda >= meta_venda:
    print("✅ Parabéns! Meta de venda atingida.")
    # Calcula um bônus de 5% sobre o total
    bonus = total_venda * 0.05
    print(f"Você ganhou um bônus de: R$ {bonus:.2f}")
    
elif total_venda >= (meta_venda * 0.8):
    # Se atingiu pelo menos 80% da meta
    print("⚠️ Quase lá! Atingiu 80% da meta, mas não o suficiente para o bônus.")
    bonus = 0.00
    
else:
    # Se foi menor que 80% da meta
    print("❌ Meta não atingida. Precisamos melhorar no próximo mês.")
    bonus = 0.00

print("=" * 50)
print(f"Bônus final a receber: R$ {bonus:.2f}")
print("=" * 50)