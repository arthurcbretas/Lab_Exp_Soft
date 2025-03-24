# Análise de Repositórios Java no GitHub

## 📊 Hipóteses para Análise

### 1. Relação entre Complexidade Ciclomática (WMC) e Coesão (LCOM)
- **Hipótese:** Projetos com alta complexidade ciclomótica (WMC) tendem a ter menor coesão (LCOM).
- **Justificativa:** Quanto mais métodos interagem entre si, menor a coesão do código.
- **Métricas:** WMC (Weighted Methods per Class) vs. LCOM (Lack of Cohesion in Methods).
- **Gráfico:** Dispersão (Scatter Plot) para visualizar a correlação.

### 2. Relação entre o Número de Classes (NOC) e Acoplamento (CBO)
- **Hipótese:** Projetos com maior número de classes (NOC) tendem a ter maior acoplamento (CBO).
- **Justificativa:** Mais classes podem levar a dependências maiores entre elas.
- **Métricas:** NOC (Number of Classes) vs. CBO (Coupling Between Objects).
- **Gráfico:** Dispersão ou Boxplot (para mostrar a distribuição).

### 3. Relação entre Profundidade da Hierarquia (DIT) e Complexidade (WMC)
- **Hipótese:** Classes com maior profundidade na hierarquia (DIT) tendem a ter maior complexidade (WMC).
- **Justificativa:** Classes mais profundas podem herdar muitos métodos, aumentando a complexidade.
- **Métricas:** DIT (Depth of Inheritance Tree) vs. WMC.
- **Gráfico:** Gráfico de Dispersão ou Barras empilhadas por categoria.

### 4. Relação entre Fan-In, Fan-Out e Manutenção
- **Hipótese:** Projetos com maior fan-in (NOC alto) e fan-out (CBO alto) são mais propensos a problemas de manutenção.
- **Justificativa:** Código muito interconectado pode ser difícil de modificar sem introduzir bugs.
- **Métricas:** NOC, CBO e RFC (Response for a Class).
- **Gráfico:** Matriz de calor para mostrar dependências.

### 5. Relação entre Complexidade Média (WMC) e Linhas de Código (LOC)
- **Hipótese:** Projetos com maior complexidade média (WMC) possuem mais linhas de código (LOC).
- **Justificativa:** Mais métodos complexos geralmente significam classes maiores.
- **Métricas:** Média de WMC por projeto vs. LOC.
- **Gráfico:** Histograma ou Boxplot.

---

## ⚙️ Scripts para Coleta e Análise de Dados

### 💾 Coleta de Repositórios Java do GitHub
O script `fetch_top_repositories.py` usa a API GraphQL do GitHub para buscar os 1000 repositórios Java mais populares.

- **Autentica na API do GitHub usando um token.**
- **Faz requisições para obter repositórios com mais estrelas.**
- **Armazena os dados em um CSV (`data/top_1000_repos.csv`).**

#### ⚡ Execução:
```sh
python fetch_top_repositories.py
```

### 🔬 Clonagem e Análise de Repositórios
O script `analyze_repositories.py` clona um repositório e executa a ferramenta SonarQube para calcular métricas de qualidade.

- **Clona repositórios Java em `repos/`.**
- **Executa SonarQube para extrair métricas como WMC, DIT, CBO e LCOM.**
- **Salva os resultados na pasta `metrics/`.**

#### ⚡ Execução:
```sh
python analyze_repositories.py
```

### 🛠️ Dependências
- **Python 3+**
- **Git**
- **Java** (para executar SonarQube)
- **[SonarQube](https://www.sonarqube.org/)** (Ferramenta de análise de qualidade de código)
- **Biblioteca Requests** (para a API do GitHub)

Para instalar dependências:
```sh
pip install requests
```

### 🛁 Estrutura do Projeto
```
/
|-- fetch_top_repositories.py   # Script para buscar repositórios do GitHub
|-- analyze_repositories.py     # Script para clonar e analisar repositórios
|-- data/
|   |-- top_1000_repos.csv      # Lista dos repositórios mais populares
|-- repos/                      # Pasta onde os repositórios são clonados
|-- metrics/                    # Pasta onde os resultados são salvos
|-- sonar-project.properties     # Configuração do SonarQube
```
