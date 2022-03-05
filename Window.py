import sys
import requests
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QLineEdit,QPushButton,QVBoxLayout,QHBoxLayout

class Windows(QWidget):
    def __init__(self):
        super().__init__()
        self.UI()
    def UI(self):
        self.first = QLineEdit("Birinci Döviz")
        self.second = QLineEdit("İkinci Döviz")
        self.amount = QLineEdit("Miktar")
        self.currency = QLabel("")
        self.btnConvert = QPushButton("Çevir")

        self.firstLbl = QLabel("Birinci Döviz")
        self.secondLbl = QLabel("İkinci Döviz")
        self.amountLbl = QLabel("Miktar")

        h_box1 = QHBoxLayout()
        h_box2 = QHBoxLayout()
        v_box1 = QVBoxLayout()
        v_box2 = QVBoxLayout()
        v_box3 = QVBoxLayout()
        v_box4 = QVBoxLayout()

        v_box1.addWidget(self.firstLbl)
        v_box1.addWidget(self.first)
        v_box2.addWidget(self.secondLbl)
        v_box2.addWidget(self.second)
        v_box3.addWidget(self.amountLbl)
        v_box3.addWidget(self.amount)
        h_box1.addLayout(v_box1)
        h_box1.addLayout(v_box2)
        h_box1.addLayout(v_box3)
        h_box2.addWidget(self.btnConvert)
        h_box2.addWidget(self.currency)
        v_box4.addLayout(h_box1)
        v_box4.addLayout(h_box2)

        self.btnConvert.clicked.connect(self.click)
        self.setLayout(v_box4)
        self.setWindowTitle("Döviz Programı")
        self.show()
    def click(self):
        try:
            url = "https://api.frankfurter.app/latest?from="
            responce = requests.get(url+self.first.text().upper())
            json_data = responce.json()
            self.currency.setText(str(json_data["rates"][self.second.text().upper()]*float(self.amount.text())))
        except:
            self.currency.setText("Para birimlerini doğru giriniz.")


app = QApplication(sys.argv)
window1 = Windows()
sys.exit(app.exec_())