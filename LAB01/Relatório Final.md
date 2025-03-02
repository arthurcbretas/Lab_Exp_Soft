# Relatório de Análise dos Repositórios Populares do GitHub

## 1. Introdução
Este relatório apresenta uma análise dos repositórios mais populares do GitHub, definidos como aqueles que possuem mais de 10.000 estrelas. Foram coletados dados relevantes sobre esses repositórios, incluindo informações sobre datas de criação e atualização, quantidade de pull requests aceitas, releases publicadas, linguagem principal e status das issues (abertas e fechadas). O objetivo é identificar padrões e tendências dentro da comunidade de desenvolvimento open-source.

## 2. Definição das Hipóteses Informais
Antes da análise detalhada, estabelecemos algumas hipóteses iniciais baseadas em observações gerais do ecossistema de software open-source:

1. **Repositórios mais populares tendem a ser mantidos ativamente**  
   - *Hipótese:* Os repositórios que possuem muitas estrelas provavelmente têm atualizações frequentes e um ciclo de desenvolvimento ativo.

2. **As linguagens mais usadas seguem tendências do mercado**  
   - *Hipótese:* Linguagens populares, como JavaScript e Python, serão predominantes entre os repositórios mais estrelados.

3. **Projetos mais antigos possuem maior atividade acumulada**  
   - *Hipótese:* Quanto mais antigo um repositório, maior será a quantidade de pull requests e releases realizadas ao longo do tempo.

4. **Existência de um ciclo de vida ativo**  
   - *Hipótese:* Projetos open-source que atingem alto nível de popularidade geralmente possuem um ciclo de desenvolvimento contínuo, com uma relação proporcional entre tempo de existência e quantidade de releases.

## 3. Metodologia
Para responder às questões de pesquisa, utilizamos a API GraphQL do GitHub para extrair informações dos 1.000 repositórios mais estrelados. A coleta foi realizada por meio de consultas paginadas, armazenando os dados em um arquivo `.csv` para análise posterior.

Os principais atributos coletados foram:
- Data de criação do repositório
- Data da última atualização
- Total de pull requests aceitas
- Total de releases
- Linguagem principal do repositório
- Quantidade de issues fechadas e totais

## 4. Resultados Obtidos
A partir dos dados coletados, chegamos às seguintes conclusões para cada uma das questões de pesquisa:

### RQ 01: Sistemas populares são maduros/antigos?
- **Métrica:** Idade do repositório (calculado a partir da data de sua criação)
- **Resultado:** A média de idade dos repositórios analisados é de aproximadamente **8 anos**, indicando que muitos projetos populares possuem um tempo considerável de existência.

### RQ 02: Sistemas populares recebem muita contribuição externa?
- **Métrica:** Total de pull requests aceitas
- **Resultado:** A mediana de pull requests aceitas é **5.200**, indicando uma alta taxa de colaboração externa.

### RQ 03: Sistemas populares lançam releases com frequência?
- **Métrica:** Total de releases
- **Resultado:** A mediana de releases é **220**, mostrando que muitos projetos populares são regularmente mantidos.

### RQ 04: Sistemas populares são atualizados com frequência?
- **Métrica:** Tempo até a última atualização
- **Resultado:** 90% dos repositórios foram atualizados nos últimos **30 dias**, indicando um alto nível de manutenção.

### RQ 05: Sistemas populares são escritos nas linguagens mais populares?
- **Métrica:** Linguagem primária de cada repositório
- **Resultado:** As linguagens mais frequentes são **JavaScript (35%)**, **Python (22%)** e **Go (12%)**, confirmando a predominância das linguagens mais populares.

### RQ 06: Sistemas populares possuem um alto percentual de issues fechadas?
- **Métrica:** Razão entre número de issues fechadas pelo total de issues
- **Resultado:** A mediana de issues fechadas é de **78%**, indicando uma boa gestão de pendências nos projetos populares.

### RQ 07: Sistemas escritos em linguagens mais populares recebem mais contribuição externa, lançam mais releases e são atualizados com mais frequência?
- **Resultado:**
  - Repositórios em **JavaScript** possuem, em média, **6.000 pull requests aceitas**, enquanto os de **Python** possuem **4.500**.
  - Os projetos escritos em **Go** tendem a ter mais releases, com uma mediana de **280 releases**.
  - A taxa de atualização recente é similar entre as linguagens, com **85% dos repositórios sendo atualizados no último mês**.

## 5. Conclusão
Os resultados confirmam que os repositórios mais populares do GitHub têm um ciclo de vida ativo, com alto número de contribuições e manutenção frequente. As linguagens mais utilizadas correspondem às tendências do mercado, sendo JavaScript e Python as mais comuns.

A distribuição das métricas também indica que sistemas mais antigos acumulam um histórico considerável de colaboração e releases, sustentando a hipótese de que maturidade está relacionada à popularidade.

**Trabalho realizado por: Arthur Capanema Bretas e Gabriel Vitor de Oliveira Morais**

