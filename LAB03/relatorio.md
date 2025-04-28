## 📚 Relatório Final - Lab 03

### 📥 Coleta de Dados

Foram coletados 200 repositórios populares do GitHub, cada um com mais de 10.000 estrelas. A seguir, extraímos informações detalhadas sobre os Pull Requests (PRs) desses repositórios, filtrando apenas aqueles que:

- Foram **merged** ou **closed**;
- Tiveram ao menos **1 revisão** registrada;
- Possuíram tempo de análise de **pelo menos 1 hora** entre abertura e fechamento.

Total de Pull Requests analisados: **1137**

### 📈 Análise Quantitativa

#### 🔎 Repositórios com Maior Frequência de Code Reviews

- Dos 200 repositórios, vários apresentaram alto volume de code reviews.
- Exemplos de repositórios mais ativos:
  - `open-webui/open-webui`: **17 revisões** em média.
  - `microsoft/terminal`: **7,26 revisões** em média.
  - `louislam/uptime-kuma`: **6,6 revisões** em média.
- Em média, tivemos **2,79 reviews por PR**.

#### 💬 Distribuição de Comentários em Pull Requests

- Média de **2,72 comentários** por PR.
- Desvio padrão de **5,36**, indicando grande variação.
- Alguns PRs chegaram a acumular **114 comentários** (valor máximo).

#### ⏳ Tempo de Revisão (Tempo entre criação e merge/close)

- Tempo médio de revisão: **1026,92 horas** (~42 dias).
- Mediana (50% dos casos) foi de apenas **24,16 horas** (~1 dia).
- Mínimo: **1 hora**.
- Máximo: **116.725 horas** (~13 anos) - um outlier claro.

A maior parte dos PRs foi revisada dentro de **6,27 horas** (percentil 25%) a **135,34 horas** (percentil 75%).

---

### 🧠 Avaliação das Hipóteses

**H1: Repositórios com mais revisores tendem a ter menos bugs após o merge.**
- **Avaliação:** Não foi possível confirmar, pois não coletamos métricas de bugs.

**H2: O tempo de resposta dos revisores é menor em projetos com equipes distribuídas internacionalmente.**
- **Avaliação:** Dados não suficientes para avaliar distribuição geográfica dos times.

**H3: O número de comentários em um PR está positivamente correlacionado com a complexidade (medida por alterações de código).**
- **Avaliação:** Sim, observou-se que PRs com mais "additions" e "deletions" tendem a ter mais comentários.
  - Correlação positiva entre número de linhas alteradas e comentários.

**H4: PRs com mais participantes tendem a ter mais comentários.**
- **Avaliação:** Sim, média de **3,4 participantes** por PR e forte correlação com quantidade de comentários.

**H5: PRs com mais revisores tendem a ter tempos de revisão maiores.**
- **Avaliação:** Parcialmente verdadeiro. PRs com muitos participantes apresentaram tanto revisões rápidas quanto demoradas, mas PRs com poucos participantes geralmente foram resolvidos mais rapidamente.

---

### ✅ Conclusões

- A média de **2,79 revisores por PR** mostra uma prática comum de revisão colaborativa.
- **3,4 participantes** por PR em média.
- **Tempo médio** de revisão elevado (42 dias) é influenciado por outliers; mediana de 24 horas é mais representativa.
- PRs com mais alterações (additions/deletions) realmente tendem a receber mais comentários.
- A maioria dos repositórios apresenta práticas básicas de revisão, com poucos reviewers por PR.

**Principais números:**
- `max(review_count) = 50`;
- `mean(comments) = 2,72`;
- `mean(participants) = 3,4`;
- `median(review_time) = 24,16 horas`.

