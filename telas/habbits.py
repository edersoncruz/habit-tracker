import json
import os
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QCheckBox, QPushButton, QGridLayout, QLineEdit, QHBoxLayout
from PySide6.QtCore import Qt, QLocale

locale = QLocale(QLocale.Portuguese, QLocale.Brazil)
QLocale.setDefault(locale)

HABITS_FILE = "habits.json"

class HabitsWindow(QWidget):
    DEFAULT_HABITS = [
        "Estudar Python",
        "Estudar Inglês",
        "Exercitar-se",
        "Ler um livro",
        "Lei da Atração",
        "Escrever Diário",
        "Meditar",
    ]

    def __init__(self, main_window, stack, parent=None):
        super().__init__(parent)
        self.main_window = main_window
        self.stack = stack
        self.current_date_str = None

        self.habbits = QVBoxLayout()
        self.checkboxes = {}

        # Campo para adicionar hábito
        input_layout = QHBoxLayout()
        self.input_habit = QLineEdit()
        self.input_habit.setPlaceholderText("Novo hábito")
        self.add_habit_btn = QPushButton("Adicionar hábito")
        self.add_habit_btn.clicked.connect(self.add_habit)
        input_layout.addWidget(self.input_habit)
        input_layout.addWidget(self.add_habit_btn)
        self.habbits.addLayout(input_layout)

        self.habbits.addSpacing(20)
        self.grid = QGridLayout()
        self.habbits.addLayout(self.grid)

        self.habbits.addStretch()

        # Botão para voltar ao calendário
        button = QPushButton("Voltar ao Calendário")
        button.clicked.connect(self.on_back_to_calendar)
        self.habbits.addWidget(button)
        button.setFixedHeight(30)

        self.setLayout(self.habbits)

        # Para exibir a data selecionada
        self.titulo = None

        # Carrega lista de hábitos personalizada
        self.habits_list = self.load_habits_list()
        self.create_checkboxes()

    def set_date(self, date):
        # Remove o título anterior, se existir
        if self.titulo:
            self.habbits.removeWidget(self.titulo)
            self.titulo.deleteLater()
        # Atualiza o título com a data selecionada
        data_formatada = QLocale(QLocale.Portuguese, QLocale.Brazil).toString(date, QLocale.LongFormat)
        self.titulo = QLabel(data_formatada)
        self.titulo.setAlignment(Qt.AlignCenter)
        self.habbits.insertWidget(1, self.titulo)  # Depois do campo de adicionar hábito
        self.habbits.setAlignment(Qt.AlignTop)

        # Salva a data atual em formato ISO para usar como chave no JSON
        self.current_date_str = date.toString(Qt.ISODate)
        self.load_habits_for_date()

    def create_checkboxes(self):
        # Limpa o grid antes de recriar
        for i in reversed(range(self.grid.count())):
            widget = self.grid.itemAt(i).widget()
            if widget:
                widget.setParent(None)
        self.checkboxes.clear()
        for idx, label in enumerate(self.habits_list):
            row = idx // 2
            col = idx % 2
            cb = QCheckBox(label)
            self.grid.addWidget(cb, row, col * 2)
            self.checkboxes[label] = cb
            # Botão remover
            rm_btn = QPushButton("Remover")
            rm_btn.setFixedWidth(80)
            rm_btn.clicked.connect(lambda _, l=label: self.remove_habit(l))
            self.grid.addWidget(rm_btn, row, col * 2 + 1)
        # Sempre recarrega o estado dos checkboxes para o dia atual
        self.load_habits_for_date()

    def add_habit(self):
        label = self.input_habit.text().strip()
        if label and label not in self.habits_list:
            self.habits_list.append(label)
            self.save_habits_list()
            self.create_checkboxes()
            self.input_habit.clear()

    def remove_habit(self, label):
        if label in self.habits_list:
            self.habits_list.remove(label)
            self.save_habits_list()
            self.create_checkboxes()

    def save_habits_list(self):
        # Salva a lista de hábitos personalizada
        data = self.load_all_habits()
        data["_habits_list"] = self.habits_list
        with open(HABITS_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def load_habits_list(self):
        if os.path.exists(HABITS_FILE):
            with open(HABITS_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
            return data.get("_habits_list", self.DEFAULT_HABITS.copy())
        return self.DEFAULT_HABITS.copy()

    def on_back_to_calendar(self):
        self.save_habits_for_date()
        self.stack.setCurrentIndex(0)

    def closeEvent(self, event):
        self.save_habits_for_date()
        super().closeEvent(event)

    def save_habits_for_date(self):
        if not self.current_date_str:
            return
        data = self.load_all_habits()
        data[self.current_date_str] = {label: cb.isChecked() for label, cb in self.checkboxes.items()}
        # Também salva a lista de hábitos personalizada
        data["_habits_list"] = self.habits_list
        with open(HABITS_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def load_habits_for_date(self):
        if not self.current_date_str:
            return
        data = self.load_all_habits()
        checks = data.get(self.current_date_str, {})
        for label, cb in self.checkboxes.items():
            cb.setChecked(checks.get(label, False))

    def load_all_habits(self):
        if os.path.exists(HABITS_FILE):
            with open(HABITS_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        return {}
