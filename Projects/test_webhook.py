import os
import httpx
from dotenv import load_dotenv

load_dotenv()
secret = os.getenv("WEBHOOK_SECRET")

r = httpx.post(
    "http://127.0.0.1:8000/webhook",
    headers={"Authorization": f"Bearer {secret}"},
    json={"repo": "you/repo", "run_id": "123", "branch": "main", "logs": "test log"},
    timeout=60,
)
print(r.status_code, r.text)