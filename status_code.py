import os
from dotenv import load_dotenv
import requests

load_dotenv()
url = os.getenv("WEBHOOK_URL")
url2 = os.getenv("WEBHOOK_URL2")

if not url:
    print("Error: URL do not find в .env")
else:
    print("URL download:", url)

# Пример: отправка POST-запроса
response = requests.post(url, json={"test": "data"})
print("Status answer:", response.status_code)

