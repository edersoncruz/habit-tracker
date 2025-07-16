from PySide6.QtWidgets import QWidget, QGridLayout
from PySide6.QtWidgets import QPushButton
from pathlib import Path
import json
import os
import matplotlib.pyplot as plt
from datetime import datetime


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

# Grid 

class GridWindow(QWidget):
    def __init__(self, stack, parent=None):
        super().__init__(parent)
        self.stack = stack

        # Layout em grade
        self.grid_layout = QGridLayout(self)
        self.setLayout(self.grid_layout)

        # Line Graph
        plt.figure(figsize=(7,2.5))
        plt.plot(datas, values, marker='o', linestyle='-', color='blue')
        # Linha de meta fixa (hardcoded)
        plt.axhline(y=11, color='red', linestyle='--', label='Meta (11)')
        plt.title("Hábitos ao longo do tempo")
        plt.xlabel("Data")
        plt.ylabel("Valor")
        plt.grid(True)
        plt.tight_layout()
        plt.show()
       
        # Botão para voltar ao menu inicial
        button_back = QPushButton("Voltar ao menu Inicial")
        button_back.clicked.connect(self.back_initial_menu)
        self.grid_layout.addWidget(button_back)
        button_back.setFixedHeight(30)

        self.setWindowTitle("Tela em Grade")

    def back_initial_menu(self):
        self.stack.setCurrentIndex(0)
