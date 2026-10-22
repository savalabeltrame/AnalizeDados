import pandas as pd
import matplotlib.pyplot as plt

# 1. Leer datos
df = pd.read_csv("vendas_cafe.csv")

# 2. Calcular faturamento
df["Faturamento"] = df["Quantidade"] * df["Preco_Unitario"]

# 3. Resumen por categoría
resumo = df.groupby("Categoria")["Faturamento"].sum()

print("=== FATURAMENTO POR CATEGORIA ===")
print(resumo)
print()

# 4. Categoría ganadora
categoria_campea = resumo.idxmax()
faturamento_maximo = resumo.max()
print(f"🏆 Categoria campea: {categoria_campea} (R$ {faturamento_maximo:.2f})")
print()

# 5. Filtrar produtos premium
df_premium = df[df["Preco_Unitario"] > 10.00]
print("=== PRODUTOS PREMIUM ===")
print(df_premium[["Produto", "Preco_Unitario", "Faturamento"]])
print()

# 6. Exportar CSV
df_premium.to_csv("produtos_premium.csv", index=False, encoding="utf-8")
print("✅ CSV exportado: produtos_premium.csv")
print()

# 7. Criar gráfico SIMPLES (sin configuración de fuentes)
plt.figure(figsize=(10, 6))
resumo.plot(kind='bar', color='#4CAF50')
plt.title("Faturamento por Categoria", fontsize=14, fontweight='bold')
plt.xlabel("Categoria")
plt.ylabel("Valor (R$)")
plt.xticks(rotation=0)
plt.tight_layout()

# 8. Salvar gráfico
plt.savefig("grafico_vendas.png", dpi=150, bbox_inches='tight')
print("✅ Gráfico salvo como: grafico_vendas.png")

# 9. Mostrar en pantalla (opcional)
plt.show()