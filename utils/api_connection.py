import requests
import json
from utils.variables import HABITS_FILE

url = "https://api.jsonbin.io/v3/b/6872a3c66063391d31ac4fb9"

def sent_api():
    with open(HABITS_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    headers = {
        "Content-Type": "application/json",
        "X-Master-Key": 
        "$2a$10$nnxEq6j2XMOUQB6OddcJZOwjkSgrovniGswSG1E1DCtyqYWIMqNO2"
        }

    response = requests.put(url, headers=headers, data=json.dumps(data))


def load_api():
        headers = {
            "X-Master-Key": 
            "$2a$10$nnxEq6j2XMOUQB6OddcJZOwjkSgrovniGswSG1E1DCtyqYWIMqNO2"
        }

        response = requests.get(url, headers=headers)
        data = response.json()
        conteudo = data["record"]

        with open (HABITS_FILE, "w", encoding="utf-8") as f:
            json.dump(conteudo, f, ensure_ascii=False, indent=2)