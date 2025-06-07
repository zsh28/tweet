import requests
from functools import lru_cache

@lru_cache(maxsize=1)
def fetch_trusted_accounts():
    print("🔄 Fetching trusted accounts from GitHub...")
    url = "https://raw.githubusercontent.com/devsyrem/turst-list/main/list"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return [
            int(line.strip())
            for line in response.text.splitlines()
            if line.strip().isdigit()
        ]
    except Exception as e:
        print(f"⚠️ Failed to fetch trusted accounts list: {e}")
        return []
