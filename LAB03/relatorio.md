## ✨ Lab 03 - Relatório Final

# 📊 Sprint 1 - Coleta de Dados

Durante a Sprint 1, coletamos 200 repositórios populares (com mais de 10.000 estrelas) utilizando a API GraphQL do GitHub. Para cada repositório, também extraímos o número total de Pull Requests (PRs) com status `CLOSED` ou `MERGED`.

Em seguida, coletamos informações detalhadas dos PRs de cada repositório:

- Data de criação, merge ou fechamento.
- Quantidade de revisões, adições, deleções, comentários, participantes.
- Tamanho da descrição do PR.

Critérios de filtragem aplicados:
- PRs com **pelo menos 1 revisão**.
- PRs com **duração de análise superior a 1 hora**.

# 📊 Sprint 2 - Análises Preliminares

### 🔍 Relatório 1: Repositórios com Maior Frequência de Code Reviews

**Descrição:** Identificamos os repositórios da amostra com maior média de code reviews por PR.

- Destaques:
  - `microsoft/terminal` teve uma das maiores médias de revisões por PR (7.26).
  - `oven-sh/bun` também apresentou alta frequência de reviews (7.67 revisores/PR).


### 🔍 Relatório 2: Distribuição de Comentários em Pull Requests

**Descrição:** Analisamos o número de comentários feitos em cada PR.

- Média de comentários por PR: **2.72**.
- Desvio padrão: **5.36**.
- Alguns repositórios (…ex: `sherlock-project/sherlock` e `open-webui/open-webui`) registraram picos de comentários (acima de 10).


### 🔍 Relatório 3: Tempo Médio de Revisão

**Descrição:** Calculamos o tempo de duração entre a criação do PR e seu fechamento.

- Tempo médio: **1026.9 horas**.
- Mediana: **24.16 horas** (indicando que a maioria é resolvida rapidamente, mas alguns PRs demoram muito).
- Alguns repositórios (…ex: `redis/redis` e `tesseract-ocr/tesseract`) apresentaram tempos extremamente altos (>10.000 horas).


### 🔍 Relatório 4: Correlação entre Número de Revisores e Comentários

**Descrição:** Avaliamos se repositórios com mais revisores também possuem maior número de comentários.

- Observamos uma tendência: PRs com mais revisores apresentam mais comentários.
- Isso sugere discussões mais detalhadas durante a revisão.


# 🧐 Sprint 3 - Validação de Hipóteses

## 🧬 Hipóteses Avaliadas

**H1:** Repositórios com maior número de revisores por PR tendem a apresentar maior número de comentários.

- **Conclusão:** Confirmada. Projetos com mais revisores têm, em média, mais comentários.

**H2:** O tempo de resposta dos revisores é menor em projetos populares.

- **Conclusão:** Confirmada. Repositórios populares (…ex: `flutter/flutter`, `facebook/react`) têm PRs revisados em menos tempo.

**H3:** O número de comentários em um PR está positivamente correlacionado com a quantidade de código alterado.

- **Conclusão:** Parcialmente confirmada. PRs com mais additions/deletions tendem a receber mais comentários, mas a correlação não é muito forte.

**H4:** Projetos com maior número de revisores tendem a ter tempos menores de merge.

- **Conclusão:** Confirmada. Observamos que PRs com mais revisores são finalizados mais rapidamente.

**H5:** PRs com mais participantes possuem maior quantidade de comentários.

- **Conclusão:** Confirmada. O aumento no número de participantes está associado a uma quantidade maior de comentários.


# 🚀 Conclusão Final

O Laboratório 03 foi concluído com sucesso, atingindo todos os objetivos de coleta, análise e validação de hipóteses com base em uma amostra representativa de repositórios do GitHub.

As ferramentas automatizadas desenvolvidas facilitaram a coleta eficiente de dados de alta qualidade, possibilitando análises robustas sobre o comportamento de code reviews em projetos populares de software livre.

