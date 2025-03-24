# Relatório Final da Análise de Qualidade e Características de Repositórios Java

## 1. Introdução  

Este estudo tem como objetivo analisar a relação entre a popularidade, maturidade, atividade e tamanho dos repositórios com suas respectivas métricas de qualidade, como CBO (Coupling Between Objects), DIT (Depth Inheritance Tree) e LCOM (Lack of Cohesion of Methods). A análise foi realizada utilizando repositórios populares em Java, coletados da plataforma GitHub e avaliados por meio de métricas extraídas com a ferramenta CK.

### Hipóteses Informais  

- **RQ01:** Repositórios mais populares (com maior número de estrelas) tendem a apresentar menor CBO, DIT e LCOM, indicando melhor qualidade estrutural.  
- **RQ02:** Repositórios mais antigos (maior maturidade) demonstram uma tendência de redução em DIT e CBO, mas um aumento em LCOM, sugerindo que, ao longo do tempo, os projetos podem perder coesão nos métodos.  
- **RQ03:** Repositórios com maior atividade (mais releases) apresentam uma leve tendência de redução em LCOM e CBO, indicando que a manutenção contínua pode melhorar o acoplamento e coesão do código.  
- **RQ04:** Repositórios maiores (com mais linhas de código) tendem a ter um aumento na média de LCOM, sugerindo menor coesão entre os métodos, enquanto CBO apresenta uma leve tendência de redução, indicando possível modularização do código.

## 2. Metodologia

Os dados foram coletados de repositórios Java populares no GitHub, utilizando suas APIs REST e GraphQL para extrair informações sobre:
- Popularidade: número de estrelas
- Maturidade: idade em anos
- Atividade: número de releases
- Tamanho: Linhas de Código (LOC)

As métricas de qualidade foram extraídas utilizando a ferramenta CK (Chidamber & Kemerer Java Metrics). Os resultados foram sumarizados utilizando valores de média, mediana e desvio padrão.

## 3. Resultados

Abaixo estão os principais achados da análise:

### 3.1. Popularidade e Qualidade
- A média de **DIT, LCOM e CBO reduziram** conforme o número de estrelas aumentou.
- Isso sugere que repositórios populares tendem a ter códigos mais bem estruturados, com menor acoplamento e melhor modularização.

### 3.2. Maturidade e Qualidade
- A média de **DIT e CBO diminuiu** com o aumento da idade do repositório.
- A média de **LCOM aumentou** com o tempo.
- Isso pode indicar que repositórios mais antigos têm uma arquitetura mais simples, mas a coesão entre os métodos piora ao longo do tempo.

### 3.3. Atividade e Qualidade
- A média de **LCOM e CBO diminuíram** levemente com o aumento do número de releases.
- Isso sugere que repositórios mais ativos podem estar refinando seu design ao longo do tempo, reduzindo o acoplamento e melhorando a estrutura do código.

### 3.4. Tamanho e Qualidade
- A média de **LCOM aumentou** conforme o LOC cresceu.
- A média de **CBO reduziu** conforme o LOC cresceu.
- Isso pode indicar que repositórios maiores têm códigos menos acoplados, mas a coesão entre os métodos piora.

## 4. Visualização no Power BI
Para apresentar os resultados de forma clara e intuitiva, utilizamos as seguintes visualizações no Power BI:

Gráficos de linha com tendência: Demonstram a relação entre as métricas de qualidade do código (CBO, DIT e LCOM) e os fatores analisados, como número de estrelas, idade do repositório, quantidade de releases e tamanho do código (LOC). A linha pontilhada representa a tendência dos dados.

Gráficos comparativos: Cada métrica foi analisada separadamente para diferentes variáveis, permitindo observar padrões e variações ao longo dos compartimentos categorizados.

Segmentação por compartimentos: As variáveis contínuas foram agrupadas em intervalos (bins) para facilitar a visualização e análise de tendências.
## 5. Discussão e Conclusão

Os resultados indicam que repositórios populares e mais ativos tendem a apresentar melhores práticas de desenvolvimento, reduzindo o acoplamento e aumentando a modularização. No entanto, a coesão dos métodos pode ser prejudicada conforme o repositório envelhece ou cresce em tamanho.

Essa análise pode ser aprimorada com a incorporação de outras métricas e técnicas estatísticas mais avançadas para entender melhor os fatores que impactam a qualidade dos repositórios Java no GitHub.

