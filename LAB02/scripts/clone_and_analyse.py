import csv
import os
import subprocess

def clone_repository(repo_url, repo_name):
    repo_name = repo_name.replace("/", "_")
    repo_path = f"repos/{repo_name}"

    if os.path.exists(repo_path):
        print(f"Removendo repositório existente: {repo_path}")
        try:
            os.system(f"rmdir /s /q \"{repo_path}\"" if os.name == "nt" else f"rm -rf \"{repo_path}\"")
        except Exception as e:
            print(f"Erro ao remover repositório existente: {e}")
            return

    try:
        os.system(f"git clone --depth 1 --filter=blob:none {repo_url} {repo_path}")
    except Exception as e:
        print(f"Erro ao clonar repositório: {e}")

def run_ck(repo_name):
    repo_name = repo_name.replace("/", "_")
    output_dir = f"metrics/{repo_name}"
    os.makedirs(output_dir, exist_ok=True)

    # Verifica se o Java está instalado
    try:
        subprocess.run(["java", "-version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError:
        print("Erro: Java não está instalado ou não está no PATH. Instale o JDK e tente novamente.")
        return

    # Verifica se o ck.jar está no local correto
    ck_jar_path = "ck.jar"  # Caminho para o ck.jar
    if not os.path.exists(ck_jar_path):
        print(f"Erro: {ck_jar_path} não encontrado! Certifique-se de que ele está no diretório correto.")
        return

    # Executa o CK
    try:
        result = subprocess.run(
            ["java", "-jar", ck_jar_path, f"repos/{repo_name}", "false", "0", "false", output_dir],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        print("CK executado com sucesso!")
        print("Saída do CK:", result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar CK: {e}")
        print("Erro detalhado:", e.stderr)

def main():
    # Exemplo: Clonar e analisar o primeiro repositório da lista
    with open("top_1000_repos.csv", "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)  # Pula o cabeçalho
        repo_name, repo_url, _ = next(reader)  # Pega o primeiro repositório

    clone_repository(repo_url, repo_name)
    run_ck(repo_name)

if __name__ == "__main__":
    main()