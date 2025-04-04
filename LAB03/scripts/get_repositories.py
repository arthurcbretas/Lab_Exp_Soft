import requests
import csv
import os
import time
from utils import GITHUB_GRAPHQL_URL, HEADERS

QUERY_REPOS = """
query ($cursor: String) {
  search(query: "stars:>10000", type: REPOSITORY, first: 50, after: $cursor) {
    edges {
      node {
        ... on Repository {
          nameWithOwner
          url
          stargazerCount
        }
      }
    }
    pageInfo {
      endCursor
      hasNextPage
    }
  }
}
"""

QUERY_PRS = """
query ($owner: String!, $name: String!) {
  repository(owner: $owner, name: $name) {
    pullRequests(states: [MERGED, CLOSED]) {
      totalCount
    }
  }
}
"""

def fetch_repositories():
    repositories = []
    cursor = None

    while len(repositories) < 200:
        response = requests.post(GITHUB_GRAPHQL_URL, json={'query': QUERY_REPOS, 'variables': {'cursor': cursor}}, headers=HEADERS)
        data = response.json()

        if "errors" in data:
            print("❌ Erro na query GraphQL:", data["errors"])
            break

        if "data" not in data or "search" not in data["data"]:
            print("❌ Resposta inesperada da API:", data)
            break

        search_results = data["data"]["search"]
        for repo in search_results["edges"]:
            repo_info = repo["node"]
            owner, name = repo_info["nameWithOwner"].split("/")
            repositories.append({
                "owner": owner,
                "name": name,
                "url": repo_info["url"],
                "stargazerCount": repo_info["stargazerCount"],
                "total_pull_requests": 0
            })

            if len(repositories) >= 200:
                break

        if not search_results["pageInfo"]["hasNextPage"]:
            break

        cursor = search_results["pageInfo"]["endCursor"]
        time.sleep(1)

    print(f"✅ {len(repositories)} repositórios coletados!")
    return repositories[:200]

def fetch_pull_requests_count(repositories):
    for repo in repositories:
        attempts = 0
        success = False
        while attempts < 5 and not success:
            response = requests.post(
                GITHUB_GRAPHQL_URL,
                json={'query': QUERY_PRS, 'variables': {'owner': repo["owner"], 'name': repo["name"]}},
                headers=HEADERS
            )
            data = response.json()

            if "errors" in data:
                print(f"⚠️ Erro na query GraphQL (tentativa {attempts + 1}/5):", data["errors"])
                attempts += 1
                time.sleep(2)
            else:
                if "data" in data and "repository" in data["data"] and "pullRequests" in data["data"]["repository"]:
                    repo["total_pull_requests"] = data["data"]["repository"]["pullRequests"]["totalCount"]
                success = True

        if not success:
            print(f"❌ Falha após várias tentativas ao buscar PRs para {repo['owner']}/{repo['name']}.")

        time.sleep(1)

    return repositories

def save_repositories_to_csv(repositories):
    os.makedirs("../data", exist_ok=True)
    with open("../data/repositories.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["owner", "name", "url", "stars", "total_pull_requests"])
        writer.writerows(
            [[r["owner"], r["name"], r["url"], r["stargazerCount"], r["total_pull_requests"]]
             for r in repositories[:200]]
        )

if __name__ == "__main__":
    repos = fetch_repositories()
    repos = fetch_pull_requests_count(repos)
    save_repositories_to_csv(repos)
    print(f"✅ {len(repos[:200])} repositórios salvos em data/repositories.csv")
