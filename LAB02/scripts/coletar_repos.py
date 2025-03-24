import requests
import csv
import time
import os
from datetime import datetime

TOKEN = 'TOKEN_HERE'  # Substitua pelo seu token do GitHub
URL = 'https://api.github.com/graphql'
HEADERS = {"Authorization": f"Bearer {TOKEN}"}


def get_query(after_cursor=None):
    after = f', after: "{after_cursor}"' if after_cursor else ''
    return f"""
    {{
      search(query: "language:java", type: REPOSITORY, first: 20{after}) {{
        edges {{
          cursor
          node {{
            ... on Repository {{
              nameWithOwner
              url
              stargazers {{ totalCount }}
              releases {{ totalCount }}
              createdAt
              defaultBranchRef {{
                target {{
                  ... on Commit {{
                    history(first: 1) {{
                      edges {{
                        node {{
                          additions
                          deletions
                        }}
                      }}
                    }}
                  }}
                }}
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


def fetch_top_repositories():
    repositories = []
    after_cursor = None

    while len(repositories) < 1000:
        query = get_query(after_cursor)
        result = run_query(query)

        if 'data' in result:
            search_data = result['data']['search']
            for edge in search_data['edges']:
                repo = edge['node']
                if 'nameWithOwner' in repo and 'url' in repo and 'stargazers' in repo:
                    name = repo['nameWithOwner']
                    url = repo['url']
                    stars = repo['stargazers']['totalCount']
                    releases = repo.get('releases', {}).get('totalCount', 0)
                    created_at = repo.get('createdAt', None)

                    # Calcular idade do repositório
                    age = round((datetime.utcnow() - datetime.strptime(created_at, "%Y-%m-%dT%H:%M:%SZ")).days / 365,
                                2) if created_at else 0

                    # Obter LOC e linhas de comentários (additions e deletions)
                    additions = \
                    repo.get('defaultBranchRef', {}).get('target', {}).get('history', {}).get('edges', [{}])[0].get(
                        'node', {}).get('additions', 0)
                    deletions = \
                    repo.get('defaultBranchRef', {}).get('target', {}).get('history', {}).get('edges', [{}])[0].get(
                        'node', {}).get('deletions', 0)
                    loc = additions - deletions  # Aproximação de LOC

                    repositories.append([name, url, stars, loc, releases, age])

            if not search_data['pageInfo']['hasNextPage']:
                break
            after_cursor = search_data['pageInfo']['endCursor']
        else:
            print("Erro na resposta da API:", result)
            break

    return repositories


def save_repositories_to_csv(repositories, filename="../data/top_1000_repos.csv"):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Repo Name", "URL", "Stars", "LOC", "Releases", "Age (Years)"])
        writer.writerows(repositories)


def main():
    repos = fetch_top_repositories()
    save_repositories_to_csv(repos)
    print(f"Lista dos top {len(repos)} repositórios Java salva em 'top_1000_repos.csv'.")


if __name__ == "__main__":
    main()
