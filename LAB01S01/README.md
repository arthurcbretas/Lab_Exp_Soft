# LAB01 - Análise de repositórios

Este projeto coleta informações sobre os **repositórios mais populares do GitHub** utilizando a **API GraphQL do GitHub** e gera um **relatório estruturado em Excel**. O objetivo da **Sprint 1** é obter dados de **100 repositórios com mais de 10.000 estrelas**, armazená-los em um arquivo CSV e, posteriormente, transformá-los em uma planilha formatada.

## 📌 Funcionalidades da Sprint 1
✔ **Coleta de repositórios mais populares** com base no número de estrelas  
✔ **Uso da API GraphQL do GitHub** para buscar os dados  
✔ **Armazenamento dos dados em CSV**  
✔ **Geração de uma planilha Excel formatada**  

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
