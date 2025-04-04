import os
from dotenv import load_dotenv

load_dotenv()

GITHUB_GRAPHQL_URL = os.getenv("GITHUB_GRAPHQL_URL")
HEADERS = {
    "Authorization": f"Bearer {os.getenv('GITHUB_TOKEN')}",
    "Accept": "application/vnd.github.v4+json"
}
