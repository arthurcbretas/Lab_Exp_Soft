# LAB01 - Análise de Repositórios

Este projeto coleta informações sobre os **repositórios mais populares do GitHub** utilizando a **API GraphQL do GitHub** e gera um **relatório estruturado em Excel**. O objetivo das sprints é obter dados de **1000 repositórios mais populares**, analisá-los e apresentá-los em um relatório final estruturado.

## 📌 Funcionalidades por Sprint

### 🏁 Sprint 1: Coleta de Dados
✔ **Coleta de repositórios mais populares** com base no número de estrelas  
✔ **Uso da API GraphQL do GitHub** para buscar os dados  
✔ **Armazenamento dos dados em CSV**  
✔ **Geração de uma planilha Excel formatada**  

### 📊 Sprint 2: Expansão da Coleta e Organização
✔ **Paginação para coletar 1000 repositórios**  
✔ **Armazenamento estruturado dos dados**  
✔ **Primeira versão do relatório com hipóteses iniciais**  
✔ **Análise preliminar dos dados coletados**  

### 📈 Sprint 3: Análise e Relatório Final
✔ **Cálculo de métricas como idade do repositório, releases e contribuições**  
✔ **Identificação das linguagens mais utilizadas**  
✔ **Discussão sobre os padrões identificados nos repositórios**  
✔ **Geração do relatório final em Markdown**  

## 🛠 Tecnologias Utilizadas
- **Python** 🐍  
- **GraphQL** (API do GitHub)  
- **Pandas** (Manipulação de dados)  
- **OpenPyXL** (Criação de planilhas Excel)  

## ⚙️ Como Configurar o Ambiente

1️⃣ **Crie um ambiente virtual**
```bash
python3 -m venv .venv
```

2️⃣ **Ative o ambiente virtual**  
- **Mac/Linux:**  
```bash
source .venv/bin/activate
```
- **Windows:**  
```bash
.venv\Scripts\activate
```

3️⃣ **Instale as dependências**
```bash
pip install requests pandas openpyxl
```

## 🚀 Como Executar

1️⃣ **Executar a coleta de dados (gera o CSV)**  
```bash
python scripts/coletar_dados.py
```

2️⃣ **Formatar os dados e gerar a planilha**  
```bash
python scripts/formatar_excel.py
```

✅ A planilha gerada estará disponível em `data/repositorios_formatado.xlsx`.  


📄 O relatório final está disponível no formato Markdown, pronto para análise e apresentação em `LAB01/Relatório Final.md`

