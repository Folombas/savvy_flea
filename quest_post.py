import requests
from dotenv import load_dotenv
import os

# Загружаем URL из .env
load_dotenv()
url = os.getenv("WEBHOOK_URL")

# Секретное сообщение
data = {
    "agent": "007",
    "mission": "Open to Server webhook.site",
    "time": "12:00"
}

# Отправляем POST-запрос
response = requests.post(url, data=data, json=data)

# Проверяем, что сообщение дошло
if response.status_code == 200:
    print("✅ Message sent successfully!")
else:
    print("❌ Error. Code:", response.status_code)