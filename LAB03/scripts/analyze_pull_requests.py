import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carrega o CSV de pull requests
df = pd.read_csv("../data/pull_requests.csv")

# Garante que a coluna review_count seja numérica
df["review_count"] = pd.to_numeric(df["review_count"], errors="coerce")

# 1. Boxplot com todos os dados
plt.figure(figsize=(10, 5))
sns.boxplot(x=df["review_count"])
plt.title("Distribuição de Número de Revisões por PR (Todos os dados)")
plt.xlabel("review_count")
plt.savefig("../data/plots/boxplot_all_reviews.png")
plt.close()

# 2. Boxplot removendo outliers (review_count > 10)
plt.figure(figsize=(10, 5))
filtered = df[df["review_count"] <= 10]
sns.boxplot(x=filtered["review_count"])
plt.title("Distribuição de Número de Revisões por PR (Máx 10 revisões)")
plt.xlabel("review_count")
plt.savefig("../data/plots/boxplot_reviews_max10.png")
plt.close()

# 3. Histograma (foco em PRs com até 10 revisões)
plt.figure(figsize=(10, 5))
sns.histplot(filtered["review_count"], bins=10, kde=False)
plt.title("Histograma de Revisões por PR (até 10 revisões)")
plt.xlabel("Número de Revisões")
plt.ylabel("Quantidade de PRs")
plt.savefig("../data/plots/histogram_reviews_max10.png")
plt.close()

print("✅ Gráficos gerados em ../data/")
