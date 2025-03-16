import requests
import csv
import time

TOKEN = 'TOKEN_HERE'
URL = 'https://api.github.com/graphql'
HEADERS = {"Authorization": f"Bearer {TOKEN}"}

def get_query(after_cursor=None):
    after = f', after: "{after_cursor}"' if after_cursor else ''
    return f"""
    query ($cursor: String) {{
      search(query: "language:Java stars:>10000", type: REPOSITORY, first: 20, after: $cursor) {{
        edges {{
          cursor
          node {{
            ... on Repository {{
              nameWithOwner
              stargazerCount
              createdAt
              updatedAt
              releases {{
                totalCount
              }}
            }}
          }}
        }}
        pageInfo {{
          hasNextPage
          endCursor
        }}
      }}
    }}"""

def run_query(query, variables=None, retries=3):
    for attempt in range(retries):
        response = requests.post(URL, json={'query': query, 'variables': variables}, headers=HEADERS, timeout=30)
        if response.status_code == 200:
            return response.json()
        elif attempt < retries - 1:
            time.sleep(2 ** attempt)
        else:
            raise Exception(f"Query falhou com código {response.status_code}: {response.text}")

repos = []
after_cursor = None
while len(repos) < 1000:
    query = get_query(after_cursor)
    variables = {"cursor": after_cursor}
    result = run_query(query, variables)

    if 'data' in result and 'search' in result['data']:
        search_data = result['data']['search']
        for edge in search_data['edges']:
            repo = edge['node']
            repos.append([
                repo['nameWithOwner'], repo['stargazerCount'], repo['createdAt'],
                repo['updatedAt'], repo['releases']['totalCount']
            ])

        if not search_data['pageInfo']['hasNextPage']:
            break
        after_cursor = search_data['pageInfo']['endCursor']
    else:
        print("Erro na resposta da API:", result)
        break

# Caminho do arquivo
csv_path = "../data/repositorios_java.csv"

# Salvar os dados em CSV (irá criar o arquivo se não existir)
with open(csv_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Nome", "Estrelas", "Criado em", "Última Atualização", "Releases"])
    writer.writerows(repos)

print(f"Dados coletados e salvos em '{csv_path}' ({len(repos)} repositórios)")
