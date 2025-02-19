import requests
import csv
import time

TOKEN = 'TOKEN HERE'
URL = 'https://api.github.com/graphql'
HEADERS = {"Authorization": f"Bearer {TOKEN}"}


def get_query(after_cursor=None):
    after = f', after: "{after_cursor}"' if after_cursor else ''
    return f"""
    {{
      search(query: "stars:>10000", type: REPOSITORY, first: 10{after}) {{
        edges {{
          cursor
          node {{
            ... on Repository {{
              name
              createdAt
              pullRequests(states: MERGED) {{ totalCount }}
              releases {{ totalCount }}
              updatedAt
              primaryLanguage {{ name }}
              issues(first: 100) {{
                totalCount
                nodes {{ state }}
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


def run_query(query, retries=3):
    for attempt in range(retries):
        response = requests.post(URL, json={'query': query}, headers=HEADERS, timeout=30)
        if response.status_code == 200:
            return response.json()
        elif attempt < retries - 1:
            time.sleep(2 ** attempt)
        else:
            raise Exception(f"Query falhou com código {response.status_code}: {response.text}")


repos = []
after_cursor = None
while len(repos) < 100:
    query = get_query(after_cursor)
    result = run_query(query)

    if 'data' in result:
        search_data = result['data']['search']
        for edge in search_data['edges']:
            repo = edge['node']
            closed_issues = sum(1 for issue in repo['issues']['nodes'] if issue['state'] == 'CLOSED')
            open_issues = sum(1 for issue in repo['issues']['nodes'] if issue['state'] == 'OPEN')
            repos.append([
                repo['name'], repo['createdAt'], repo['pullRequests']['totalCount'],
                repo['releases']['totalCount'], repo['updatedAt'],
                repo['primaryLanguage']['name'] if repo['primaryLanguage'] else 'N/A',
                closed_issues, open_issues
            ])

        if not search_data['pageInfo']['hasNextPage']:
            break
        after_cursor = search_data['pageInfo']['endCursor']
    else:
        print("Erro na resposta da API:", result)
        break

# Caminho do arquivo
csv_path = "../data/repositorios.csv"

with open(csv_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow([
        'Nome', 'Data de Criação', 'Pull Requests Aceitas', 'Total de Releases',
        'Última Atualização', 'Linguagem Primária', 'Issues Fechadas', 'Issues Abertas'
    ])
    writer.writerows(repos)

print(f"Dados coletados e salvos em '{csv_path}' ({len(repos)} repositórios)")
