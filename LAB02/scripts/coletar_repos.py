import os
import csv
import requests

# Configurações da API do GitHub
github_api_url = "https://api.github.com/search/repositories"
github_query = "language:java&sort=stars&order=desc&per_page=100"
github_headers = {
    "Accept": "application/vnd.github.v3+json",
    "Authorization": "token TOKEN_GIT"  # Substitua pelo seu token do GitHub
}

def fetch_top_repositories():
    repositories = []
    for page in range(1, 11):  # 10 páginas de 100 repositórios
        try:
            response = requests.get(f"{github_api_url}?q={github_query}&page={page}", headers=github_headers)
            response.raise_for_status()  # Lança exceção para erros HTTP
            data = response.json()
            repositories.extend([(repo["full_name"], repo["html_url"], repo["stargazers_count"]) for repo in data["items"]])
        except requests.exceptions.RequestException as e:
            print(f"Erro ao buscar repositórios na página {page}: {e}")
            break
    return repositories

def save_repositories_to_csv(repositories, filename="top_1000_repos.csv"):
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Repo Name", "URL", "Stars"])
        writer.writerows(repositories)

def main():
    os.makedirs("repos", exist_ok=True)
    os.makedirs("metrics", exist_ok=True)
    repos = fetch_top_repositories()
    save_repositories_to_csv(repos)
    print("Lista dos top 1.000 repositórios Java salva em 'top_1000_repos.csv'.")

if __name__ == "__main__":
    main()