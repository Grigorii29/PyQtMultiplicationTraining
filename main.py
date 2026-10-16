import random
import sys
from encodings.punycode import selective_find

from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QHeaderView
from front import Ui_MainWindow
import datetime as dt
from PyQt6.QtCore import Qt


class MyApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.startTime = None
        self.cnt = 0
        self.cnt_errors = 0
        self.cnt_ex = 0
        self.a, self.b = 0, 0
        self.startBtn.clicked.connect(self.start)

    def start(self):
        self.start_time = dt.datetime.now()
        self.cnt, self.cnt_ex = self.spinBox.value(), self.spinBox.value()
        self.a = random.randint(2, 9)
        self.b = random.randint(11, 99)
        self.workLabel.setText(f"{self.a} x {self.b}")
        self.resLabel.setText("")

    def keyPressEvent(self, event):
        if event.key() == 16777220:
            if self.cnt > 0:
                self.cnt -= 1
                self.spinBox.setValue(self.cnt)
                if self.a * self.b == int(self.lineEdit.text()):
                    self.resLabel.setText("✅ Верно")
                else:
                    self.resLabel.setText(f"Ошибка {self.a} x {self.b} не равно {int(self.lineEdit.text())}")
                    self.cnt_errors += 1
                self.a = random.randint(2, 9)
                self.b = random.randint(11, 99)
                self.lineEdit.setText("")
                self.workLabel.setText(f"{self.b} x {self.a}")
            if self.cnt == 0:
                self.cnt -= 1
                m = int((dt.datetime.now() - self.start_time).total_seconds()) // 60
                sec = (dt.datetime.now() - self.start_time).seconds
                self.resLabel.setText(
                    f"Решено примеров: {self.cnt_ex}\nДопущено ошибок: {self.cnt_errors}\nВремя:\t{m}:{sec % 60}")
                self.cnt_errors = 0


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec())
