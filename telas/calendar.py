from PySide6.QtWidgets import (
    QWidget, QCalendarWidget, QStackedWidget, QGridLayout)
from PySide6.QtCore import QLocale, Qt
from telas.habits import HabitsWindow


class CalendarioWidget(QWidget):
    def __init__(self, stack, parent=None):
        super().__init__(parent)
        self.v_layout = QGridLayout(self)

        # Calendário para navegação
        self.calendar = QCalendarWidget()
        self.calendar.setGridVisible(True)  # Mostra a grade do calendário
        self.calendar.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)
        self.calendar.setHorizontalHeaderFormat(
            QCalendarWidget.SingleLetterDayNames)
        self.calendar.setNavigationBarVisible(True)
        self.calendar.setDateEditEnabled(True)
        self.calendar.setSelectedDate(self.calendar.selectedDate())
        self.calendar.setStyleSheet(
            "QCalendarWidget { background-color: #f0f0f0; }")
        self.v_layout.addWidget(self.calendar, 0, 0, 1, 1)
        self.calendar.setFocusPolicy(Qt.StrongFocus)
        self.calendar.setFocus()
        self.calendar.installEventFilter(self)

        # Calendário em português
        self.calendar.setLocale(QLocale(QLocale.Portuguese, QLocale.Brazil))

        # Abrir nova tela ao clicar em um dia
        self.calendar.clicked.connect(
            lambda date: self.open_new_window(date, stack))

    def open_new_window(self, date, stack: QStackedWidget):
        habbits_widget = stack.widget(1)
        habbits_widget.set_date(date)
        stack.setCurrentIndex(1)
