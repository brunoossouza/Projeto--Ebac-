import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("ecommerce_estatistica.csv")

col_preco = "Preço"
col_vendas = "Qtd_Vendidos"
col_categoria = "Temporada"

#  Grafico de Histograma (Preço)

plt.figure(figsize=(10, 6))
plt.hist(df[col_preco].dropna(), bins=20)
plt.title("Histograma do Preço")
plt.xlabel("Preço")
plt.ylabel("Frequência")
plt.savefig("graficos/01_histograma.png", dpi=200, bbox_inches="tight")
plt.show()


#  Grafico Dispersã0 (Preço x Qtd_Vendidos)

plt.figure(figsize=(10, 6))
plt.scatter(df[col_preco], df[col_vendas], alpha=0.7)
plt.title("Dispersão: Preço vs Quantidade Vendida")
plt.xlabel("Preço")
plt.ylabel("Qtd_Vendidos")
plt.savefig("graficos/02_dispersao.png", dpi=200, bbox_inches="tight")
plt.show()



# MAPA DE CALOR (correlação)
plt.figure(figsize=(12, 8))
corr = df.select_dtypes("number").corr()
sns.heatmap(corr, annot=False, cmap="coolwarm")
plt.title("Mapa de calor: Correlação entre variáveis numéricas")
plt.savefig("graficos/03_mapa_de_calor.png", dpi=200, bbox_inches="tight")
plt.show()


# Grficos de barras
top = df[col_categoria].value_counts().head(10)

plt.figure(figsize=(10, 6))
plt.bar(top.index.astype(str), top.values)
plt.title(f"Top 10 - {col_categoria}")
plt.xlabel(col_categoria)
plt.ylabel("Quantidade")
plt.xticks(rotation=45, ha="right")
plt.savefig("graficos/04_barra.png", dpi=200, bbox_inches="tight")
plt.show()


# Grfico de pizza

top_pizza = df[col_categoria].value_counts().head(6)

plt.figure(figsize=(8, 8))
plt.pie(top_pizza.values, labels=top_pizza.index.astype(str), autopct="%1.1f%%", startangle=90)
plt.title(f"Distribuição - {col_categoria}")
plt.savefig("graficos/05_pizza.png", dpi=200, bbox_inches="tight")
plt.show()


# Grafico de Densisdade (Preço)

plt.figure(figsize=(10, 6))
sns.kdeplot(df[col_preco].dropna(), fill=True)
plt.title("Densidade do Preço")
plt.xlabel("Preço")
plt.ylabel("Densidade")
plt.savefig("graficos/06_densidade.png", dpi=200, bbox_inches="tight")
plt.show()



#  Grfico de  Regressao (Preço x Qtd_Vendidos)

plt.figure(figsize=(10, 6))
sns.regplot(x=df[col_preco], y=df[col_vendas], scatter_kws={"alpha": 0.5})
plt.title("Regressão: Qtd_Vendidos em função do Preço")
plt.xlabel("Preço")
plt.ylabel("Qtd_Vendidos")
plt.savefig("graficos/07_regressao.png", dpi=200, bbox_inches="tight")
plt.show()
