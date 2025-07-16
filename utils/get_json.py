import os
import json
from datetime import datetime
from pathlib import Path

# Criar dict com JSON
JSON_PATH = Path('files') / 'habits.json'

def load_json():
    if os.path.exists(JSON_PATH):
        with open(JSON_PATH, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data
    else:
        print(f"JSON file not found at {JSON_PATH}. Please ensure the file exists.")
        return None

data = load_json()
data_formatted = {}

if not data:
    print("No data found in the JSON file.")
    exit()
for key, _list in data.items():
    count = 0
    if key == "_habits_list":
        continue
    else: 
        data_formatted[key] = count
        key_formatted = datetime.strptime(key, "%Y-%m-%d").date()
        data_hoje = datetime.now().date()
        
        if key_formatted > data_hoje:
            data_formatted.pop(key, None)
            continue
        for value in _list.values():
            if value == True:
                count += 1
                data_formatted[key] = count

ordened_data = {key: data_formatted[key] for key in sorted(data_formatted)}

datas = list(ordened_data.keys())
values = list(ordened_data.values())