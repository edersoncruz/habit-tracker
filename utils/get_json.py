import os
import json
from datetime import datetime, timedelta
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

# Tenho que pegar uma lista com todos os indices do dic
# Criar uma nova lista iniciando ela pela data mais antiga da minha lista de dic que já tenho
# Crio uma variável data atual
# Faço um for e dessa data mais antiga até a data atual eu adicono um indice com a data aumentando de 1 em 1 dia.
# Para caso eu pule algum dia quando entrar no gráfico ele conte aquele dia zerado.
# Depois disso vou ter que criar a estrutura toda de habitos tudo como false

def get_json_data(delta):
    data = load_json()
    data_formatted = {}
    data = ensure_all_dates(data)
    if not data:
        raise FileNotFoundError("No data found in the JSON file.")
    for key, _list in data.items():
        count = 0
        if key == "_habits_list":
            continue
        else: 
            data_formatted[key] = count
            key_formatted = datetime.strptime(key, "%Y-%m-%d").date()
            data_hoje = datetime.now().date()
            
            if key_formatted > data_hoje or (key_formatted < (data_hoje - timedelta(days=delta))):
                data_formatted.pop(key, None)
                continue
            for value in _list.values():
                if value == True:
                    count += 1
                    data_formatted[key] = count

    ordened_data = {key: data_formatted[key] for key in sorted(data_formatted)}

    datas = list(ordened_data.keys())
    values = list(ordened_data.values())

    return datas, values


def ensure_all_dates(data):
    if not data:
        return data

    date_format = "%Y-%m-%d"
    all_dates = set()

    # Obter a data mais antiga do JSON
    min_date_str = min(key for key in data.keys() if key != "_habits_list")
    min_date = datetime.strptime(min_date_str, date_format).date()
    max_date = datetime.now().date()

    # Gerar todas as datas entre a data mais antiga e a data atual
    current_date = min_date
    while current_date <= max_date:
        all_dates.add(current_date.strftime(date_format))
        current_date += timedelta(days=1)

    # Adicionar datas faltantes ao dicionário com valores padrão
    for date_str in all_dates:
        if date_str not in data:
            data[date_str] = {habit: False for habit in data.get("_habits_list", [])}

    return data