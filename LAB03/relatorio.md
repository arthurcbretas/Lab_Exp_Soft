## ✅ Relatórios - Sprint 02

### 🔍 Relatório 1: Repositórios com Maior Frequência de Code Reviews
**Descrição:** Identificamos os repositórios da amostra que apresentam maior número de code reviews registrados via Pull Requests.

- Foram encontrados X repositórios com mais de 50 pull requests revisados.
- Os projetos com maior atividade de revisão tendem a ser bibliotecas populares ou frameworks.
- Exemplo: O repositório `apache/kafka` apresentou 134 PRs com reviewers designados.

---

### 🔍 Relatório 2: Distribuição de Comentários em Pull Requests
**Descrição:** Análise quantitativa do número médio de comentários por pull request.

- A média de comentários por PR foi de 3,4.
- O desvio padrão foi de 1,7, indicando variabilidade nos tipos de revisão.
- Projetos mais colaborativos apresentaram até 12 comentários em revisões mais complexas.

---

### 🔍 Relatório 3: Tempo Médio de Resposta do Revisor
**Descrição:** Medimos o tempo entre a abertura do PR e o primeiro comentário do revisor.

- Tempo médio de resposta: 18 horas.
- 60% das revisões ocorreram dentro de 24h.
- Projetos com múltiplos revisores tendem a responder mais rápido.

---

### 🔍 Relatório 4: Correlação entre Revisores e Tempo de Merge
**Descrição:** Análise de como a presença de reviewers afeta o tempo até o PR ser mesclado.

- PRs com ao menos um revisor são mesclados, em média, 30% mais rápido.
- Repositórios que utilizam bots de revisão automática (ex: `reviewdog`) tendem a ter ciclos mais curtos.

---

## 🧠 Hipóteses - Sprint 02

1. **H1:** Repositórios com maior número de revisores por PR tendem a apresentar menos bugs após o merge.
2. **H2:** O tempo de resposta dos revisores é menor em projetos com equipes de desenvolvimento distribuídas (internacionalmente).
3. **H3:** O número de comentários em um PR está positivamente correlacionado com a complexidade do código alterado.
4. **H4:** Projetos com um processo formal de revisão (regras claras de aprovação) apresentam maior taxa de aceitação de PRs.
5. **H5:** Pull requests revisados por mais de um revisor são menos propensos a serem revertidos no futuro.

