import requests
import csv
import os
import pandas as pd

# 👉 Substitua pelo seu token pessoal do GitHub
GITHUB_TOKEN = "SEU_TOKEN_AQUI"

# Configuração da API GraphQL
GITHUB_GRAPHQL_URL = "https://api.github.com/graphql"
HEADERS = {
    "Authorization": f"Bearer {GITHUB_TOKEN}"
}

# Consulta GraphQL para obter PRs
PR_QUERY = """
query($repo_owner: String!, $repo_name: String!) {
  repository(owner: $repo_owner, name: $repo_name) {
    pullRequests(first: 50, states: [MERGED, CLOSED]) {
      edges {
        node {
          number
          title
          createdAt
          mergedAt
          closedAt
          reviews {
            totalCount
          }
          additions
          deletions
          comments {
            totalCount
          }
          participants {
            totalCount
          }
          bodyText
        }
      }
    }
  }
}
"""

# Função para buscar PRs de um repositório
def fetch_pull_requests(repo_owner, repo_name):
    variables = {"repo_owner": repo_owner, "repo_name": repo_name}
    response = requests.post(GITHUB_GRAPHQL_URL, json={'query': PR_QUERY, 'variables': variables}, headers=HEADERS)
    data = response.json()

    # 🛑 Se houver erro na resposta
    if "errors" in data:
        print(f"Erro ao buscar PRs de {repo_owner}/{repo_name}:")
        print(data["errors"])
        return []

    pull_requests = []
    for pr in data["data"]["repository"]["pullRequests"]["edges"]:
        pr_info = pr["node"]

        created_at = pd.to_datetime(pr_info["createdAt"])
        closed_or_merged_at = pd.to_datetime(pr_info["mergedAt"] or pr_info["closedAt"])
        review_time = (closed_or_merged_at - created_at).total_seconds() / 3600

        # Filtra PRs com ao menos 1 revisão e duração de análise maior que 1 hora
        if pr_info["reviews"]["totalCount"] > 0 and review_time >= 1:
            pull_requests.append([
                f"{repo_owner}/{repo_name}",
                pr_info["number"],
                pr_info["title"],
                created_at,
                closed_or_merged_at,
                pr_info["reviews"]["totalCount"],
                pr_info["additions"],
                pr_info["deletions"],
                pr_info["comments"]["totalCount"],
                pr_info["participants"]["totalCount"],
                len(pr_info["bodyText"])
            ])

    return pull_requests

# Função para salvar em CSV
def save_pull_requests_to_csv(pull_requests):
    os.makedirs("../data", exist_ok=True)
    with open("../data/pull_requests.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            "repository", "pr_number", "title", "created_at", "closed_or_merged_at",
            "review_count", "additions", "deletions", "comments", "participants", "description_length"
        ])
        writer.writerows(pull_requests)

# Função principal
if __name__ == "__main__":
    df_repos = pd.read_csv("../data/repositories.csv")

    all_pull_requests = []

    for _, row in df_repos.iterrows():
        repo_owner = row["owner"]
        repo_name = row["name"]

        print(f"🔍 Buscando PRs para: {repo_owner}/{repo_name}")
        pull_requests = fetch_pull_requests(repo_owner, repo_name)
        all_pull_requests.extend(pull_requests)

    save_pull_requests_to_csv(all_pull_requests)
    print(f"\n✅ {len(all_pull_requests)} PRs salvos em ../data/pull_requests.csv")
