import csv
import os
import subprocess
import shutil
import stat
import pandas as pd
import logging


def remove_readonly(func, path, _):
    """Torna arquivos somente leitura editáveis para remoção."""
    os.chmod(path, stat.S_IWRITE)
    func(path)


def setup_logging():
    """Configura o logging para o processo."""
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
    return logging.getLogger(__name__)


def check_dependencies():
    """Verifica se as dependências necessárias estão presentes (Java e ck.jar)."""
    try:
        subprocess.run(["java", "-version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError:
        logging.error("Erro: Java não está instalado ou não está no PATH. Instale o JDK e tente novamente.")
        return False

    ck_jar_path = "ck.jar"
    if not os.path.exists(ck_jar_path):
        logging.error(f"Erro: {ck_jar_path} não encontrado! Certifique-se de que ele está no diretório correto.")
        return False

    return True


def clone_repository(repo_url, repo_name):
    repo_name = repo_name.replace("/", "_")
    repo_path = f"../data/repos/{repo_name}"

    if os.path.exists(repo_path):
        logging.info(f"Removendo repositório existente: {repo_path}")
        try:
            shutil.rmtree(repo_path, onerror=remove_readonly)
        except Exception as e:
            logging.error(f"Erro ao remover repositório existente: {e}")
            return False

    try:
        subprocess.run(["git", "clone", "--depth", "1", repo_url, repo_path], check=True)
        logging.info(f"Clonagem concluída para {repo_name}!")
        return True
    except subprocess.CalledProcessError as e:
        logging.error(f"Erro ao clonar repositório {repo_name}: {e}")
        return False


def run_ck(repo_name):
    repo_name = repo_name.replace("/", "_")
    repo_path = f"../data/repos/{repo_name}"
    output_dir = f"../data/metrics/{repo_name}"
    os.makedirs(output_dir, exist_ok=True)

    try:
        result = subprocess.run(
            ["java", "-jar", "ck.jar", repo_path, "false", "0", "false", output_dir],
            check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )
        logging.info(f"CK executado para {repo_name}:\n{result.stdout}")
        logging.error(f"Erros (se houver): {result.stderr}")

        metric_file = os.path.join(output_dir, "class.csv")
        if not os.path.exists(metric_file) or os.path.getsize(metric_file) == 0:
            logging.error(f"Erro: Nenhuma métrica válida gerada para {repo_name}!")
            return False

        df = pd.read_csv(metric_file)
        df_filtered = df[["cbo", "dit", "lcom"]].copy()
        df_filtered.insert(0, "repo_name", repo_name)
        df_filtered.to_csv("../data/metrics/metrics_final.csv", mode="a", index=False,
                           header=not os.path.exists("../data/metrics/metrics_final.csv"))

        # Remover repositório após processar métricas
        try:
            shutil.rmtree(repo_path, onerror=remove_readonly)
            logging.info(f"Repositório {repo_name} removido com sucesso!")
        except Exception as e:
            logging.error(f"Erro ao remover repositório {repo_name}: {e}")

        return True
    except subprocess.CalledProcessError as e:
        logging.error(f"Erro ao executar CK para {repo_name}: {e}")
        return False


def main():
    logger = setup_logging()

    if not check_dependencies():
        return

    processed_repos = []
    os.makedirs("../data/repos", exist_ok=True)
    os.makedirs("../data/metrics", exist_ok=True)

    with open("../data/top_1000_repos.csv", "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        header = next(reader)  # Pular cabeçalho

        for row in reader:
            repo_name = row[0]  # "Repo Name"
            repo_url = row[1]  # "URL"
            logging.info(f"Processando: {repo_name}")

            if clone_repository(repo_url, repo_name):
                if run_ck(repo_name):
                    processed_repos.append(repo_name)

    logging.info(f"Processo concluído! {len(processed_repos)} repositórios processados com sucesso.")


if __name__ == "__main__":
    main()
