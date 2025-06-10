import os
from dotenv import load_dotenv
import requests

load_dotenv()
url = os.getenv("WEBHOOK_URL")
url2 = os.getenv("WEBHOOK_URL2")

# Пример: отправка POST-запроса
response = requests.post(url, json={"test": "data"})
print("Status answer:", response.status_code)

