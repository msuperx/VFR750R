import sys
import sqlite3
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QFontDatabase
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
msxp = open("compare.txt", 'w')
msxp.close()
sp = set()
x = 0


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.minprice = QtWidgets.QLineEdit(self.centralwidget)
        self.minprice.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.minprice, 3, 1, 1, 2)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.diameter = QtWidgets.QComboBox(self.centralwidget)
        self.diameter.setObjectName("comboBox")
        self.diameter.addItems(['Все', "11", "14", "16", "17", '18', '19', '20', '22'])
        self.gridLayout.addWidget(self.diameter, 6, 2, 1, 2)
        self.maxprice = QtWidgets.QLineEdit(self.centralwidget)
        self.maxprice.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.maxprice, 3, 4, 1, 2)
        self.minpwrres = QtWidgets.QLineEdit(self.centralwidget)
        self.minpwrres.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.minpwrres, 4, 1, 1, 2)
        self.maxpwrres = QtWidgets.QLineEdit(self.centralwidget)
        self.maxpwrres.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.maxpwrres, 4, 4, 1, 2)
        self.selectbtn = QtWidgets.QPushButton(self.centralwidget)
        self.selectbtn.setObjectName("pushButton")
        self.selectbtn.setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.gridLayout.addWidget(self.selectbtn, 5, 4, 2, 1)
        self.srbtn = QtWidgets.QPushButton(self.centralwidget)
        self.srbtn.setObjectName("pushButton")
        self.srbtn.setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.gridLayout.addWidget(self.srbtn, 5, 5, 2, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.gridLayout.addWidget(self.label_6, 4, 3, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 5, 2, 1, 2)
        self.brand = QtWidgets.QComboBox(self.centralwidget)
        self.brand.setObjectName("comboBox_2")
        self.brand.addItems(['Все', "Inmotion", "Begode", "KingSong", "Leaperkim", 'Extreme Bull', 'Ninebot'])
        self.gridLayout.addWidget(self.brand, 6, 0, 1, 2)
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout.addWidget(self.listWidget, 7, 0, 1, 6)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.gridLayout.addWidget(self.label_5, 3, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 5, 0, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setFont(QtGui.QFont("Roboto", 10))
        self.label_2.adjustSize()
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 3, 1, 1)
        self.guidebtn = QtWidgets.QPushButton(self.centralwidget)
        self.guidebtn.setObjectName("pushButton")
        self.guidebtn.setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.gridLayout.addWidget(self.guidebtn, 8, 5, 2, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 754, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Моноколёса"))
        self.label_4.setText(_translate("MainWindow", "Запас хода от:"))
        self.selectbtn.setText(_translate("MainWindow", "Выбрать"))
        self.srbtn.setText(_translate("MainWindow", "Сравнить"))
        self.label_6.setText(_translate("MainWindow", "до:"))
        self.label_7.setText(_translate("MainWindow", "Диаметр"))
        self.label_5.setText(_translate("MainWindow", "до:"))
        self.label_3.setText(_translate("MainWindow", "Цена от:"))
        self.label.setText(_translate("MainWindow", "Бренд"))
        self.label_2.setText(_translate("MainWindow", "Фильтры:"))
        self.guidebtn.setText(_translate('MainWindow', 'Гайд по выбору'))


class OpenWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(657, 459)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.maxspeed = QtWidgets.QLabel(self.centralwidget)
        self.maxspeed.setAlignment(QtCore.Qt.AlignCenter)
        self.maxspeed.setObjectName("maxspeed")
        self.gridLayout_2.addWidget(self.maxspeed, 5, 2, 1, 1)
        self.diameter = QtWidgets.QLabel(self.centralwidget)
        self.diameter.setAlignment(QtCore.Qt.AlignCenter)
        self.diameter.setObjectName("diameter")
        self.gridLayout_2.addWidget(self.diameter, 4, 2, 1, 1)
        self.name = QtWidgets.QLabel(self.centralwidget)
        self.name.setAlignment(QtCore.Qt.AlignCenter)
        self.name.setFont(QtGui.QFont("Roboto", 10, QtGui.QFont.Bold))
        self.name.adjustSize()
        self.name.setObjectName("name")
        self.gridLayout_2.addWidget(self.name, 1, 2, 1, 1)
        self.weight = QtWidgets.QLabel(self.centralwidget)
        self.weight.setAlignment(QtCore.Qt.AlignCenter)
        self.weight.setObjectName("weight")
        self.gridLayout_2.addWidget(self.weight, 8, 2, 1, 1)
        self.power = QtWidgets.QLabel(self.centralwidget)
        self.power.setAlignment(QtCore.Qt.AlignCenter)
        self.power.setObjectName("power")
        self.gridLayout_2.addWidget(self.power, 6, 2, 1, 1)
        self.pwrres = QtWidgets.QLabel(self.centralwidget)
        self.pwrres.setAlignment(QtCore.Qt.AlignCenter)
        self.pwrres.setObjectName("pwrres")
        self.gridLayout_2.addWidget(self.pwrres, 3, 2, 1, 1)
        self.capacity = QtWidgets.QLabel(self.centralwidget)
        self.capacity.setAlignment(QtCore.Qt.AlignCenter)
        self.capacity.setObjectName("capacity")
        self.gridLayout_2.addWidget(self.capacity, 7, 2, 1, 1)
        self.price = QtWidgets.QLabel(self.centralwidget)
        self.price.setAlignment(QtCore.Qt.AlignCenter)
        self.price.setObjectName("price")
        self.gridLayout_2.addWidget(self.price, 2, 2, 1, 1)
        self.compare = QtWidgets.QPushButton(self.centralwidget)
        self.compare.setObjectName("pushButton")
        self.compare.setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.gridLayout_2.addWidget(self.compare, 9, 2, 1, 1)
        self.photo = QtWidgets.QLabel(self.centralwidget)
        self.photo.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.photo.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.photo.setAlignment(QtCore.Qt.AlignCenter)
        self.photo.setObjectName("photo")
        self.gridLayout_2.addWidget(self.photo, 1, 0, 9, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 657, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Товар"))
        self.maxspeed.setText(_translate("MainWindow", "TextLabel"))
        self.diameter.setText(_translate("MainWindow", "TextLabel"))
        self.name.setText(_translate("MainWindow", "TextLabel"))
        self.weight.setText(_translate("MainWindow", "TextLabel"))
        self.power.setText(_translate("MainWindow", "TextLabel"))
        self.pwrres.setText(_translate("MainWindow", "TextLabel"))
        self.capacity.setText(_translate("MainWindow", "TextLabel"))
        self.price.setText(_translate("MainWindow", "TextLabel"))
        self.compare.setText(_translate("MainWindow", "Добавить к сравнению"))
        self.photo.setText(_translate("MainWindow", "TextLabel"))


class TextWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(462, 432)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.weight_2 = QtWidgets.QLabel(self.centralwidget)
        self.weight_2.setAlignment(QtCore.Qt.AlignCenter)
        self.weight_2.setObjectName("weight_2")
        self.gridLayout.addWidget(self.weight_2, 8, 2, 1, 1)
        self.susp_1 = QtWidgets.QLabel(self.centralwidget)
        self.susp_1.setAlignment(QtCore.Qt.AlignCenter)
        self.susp_1.setObjectName("susp_1")
        self.gridLayout.addWidget(self.susp_1, 9, 0, 1, 1)
        self.pwrres_2 = QtWidgets.QLabel(self.centralwidget)
        self.pwrres_2.setAlignment(QtCore.Qt.AlignCenter)
        self.pwrres_2.setObjectName("pwrres_2")
        self.gridLayout.addWidget(self.pwrres_2, 4, 2, 1, 1)
        self.name_2 = QtWidgets.QLabel(self.centralwidget)
        self.name_2.setAlignment(QtCore.Qt.AlignCenter)
        self.name_2.setFont(QtGui.QFont("Roboto", 8, QtGui.QFont.Bold))
        self.name_2.setObjectName("name_2")
        self.name_2.adjustSize()
        self.gridLayout.addWidget(self.name_2, 1, 2, 1, 1)
        self.pwrres_1 = QtWidgets.QLabel(self.centralwidget)
        self.pwrres_1.setAlignment(QtCore.Qt.AlignCenter)
        self.pwrres_1.setObjectName("pwrres_1")
        self.gridLayout.addWidget(self.pwrres_1, 4, 0, 1, 1)
        self.maxspeed_2 = QtWidgets.QLabel(self.centralwidget)
        self.maxspeed_2.setAlignment(QtCore.Qt.AlignCenter)
        self.maxspeed_2.setObjectName("maxspeed_2")
        self.gridLayout.addWidget(self.maxspeed_2, 6, 2, 1, 1)
        self.price_1 = QtWidgets.QLabel(self.centralwidget)
        self.price_1.setAlignment(QtCore.Qt.AlignCenter)
        self.price_1.setObjectName("price_1")
        self.gridLayout.addWidget(self.price_1, 2, 0, 1, 1)
        self.susp_2 = QtWidgets.QLabel(self.centralwidget)
        self.susp_2.setAlignment(QtCore.Qt.AlignCenter)
        self.susp_2.setObjectName("susp_2")
        self.gridLayout.addWidget(self.susp_2, 9, 2, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24.setObjectName("label_24")
        self.gridLayout.addWidget(self.label_24, 4, 1, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.centralwidget)
        self.label_27.setAlignment(QtCore.Qt.AlignCenter)
        self.label_27.setObjectName("label_27")
        self.gridLayout.addWidget(self.label_27, 6, 1, 1, 1)
        self.diameter_2 = QtWidgets.QLabel(self.centralwidget)
        self.diameter_2.setAlignment(QtCore.Qt.AlignCenter)
        self.diameter_2.setObjectName("diameter_2")
        self.gridLayout.addWidget(self.diameter_2, 5, 2, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.gridLayout.addWidget(self.label_18, 9, 1, 1, 1)
        self.weight_1 = QtWidgets.QLabel(self.centralwidget)
        self.weight_1.setAlignment(QtCore.Qt.AlignCenter)
        self.weight_1.setObjectName("weight_1")
        self.gridLayout.addWidget(self.weight_1, 8, 0, 1, 1)
        self.price_2 = QtWidgets.QLabel(self.centralwidget)
        self.price_2.setAlignment(QtCore.Qt.AlignCenter)
        self.price_2.setObjectName("price_2")
        self.gridLayout.addWidget(self.price_2, 2, 2, 1, 1)
        self.power_1 = QtWidgets.QLabel(self.centralwidget)
        self.power_1.setAlignment(QtCore.Qt.AlignCenter)
        self.power_1.setObjectName("power_1")
        self.gridLayout.addWidget(self.power_1, 7, 0, 1, 1)
        self.maxspeed_1 = QtWidgets.QLabel(self.centralwidget)
        self.maxspeed_1.setAlignment(QtCore.Qt.AlignCenter)
        self.maxspeed_1.setObjectName("maxspeed_1")
        self.gridLayout.addWidget(self.maxspeed_1, 6, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 3, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setFont(QtGui.QFont("Roboto", 11))
        self.label.setObjectName("label")
        self.label.adjustSize()
        self.gridLayout.addWidget(self.label, 0, 0, 1, 3)
        self.capacity_2 = QtWidgets.QLabel(self.centralwidget)
        self.capacity_2.setAlignment(QtCore.Qt.AlignCenter)
        self.capacity_2.setObjectName("capacity_2")
        self.gridLayout.addWidget(self.capacity_2, 3, 2, 1, 1)
        self.capacity_1 = QtWidgets.QLabel(self.centralwidget)
        self.capacity_1.setAlignment(QtCore.Qt.AlignCenter)
        self.capacity_1.setObjectName("capacity_1")
        self.gridLayout.addWidget(self.capacity_1, 3, 0, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        self.label_25.setAlignment(QtCore.Qt.AlignCenter)
        self.label_25.setObjectName("label_25")
        self.gridLayout.addWidget(self.label_25, 5, 1, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 8, 1, 1, 1)
        self.diameter_1 = QtWidgets.QLabel(self.centralwidget)
        self.diameter_1.setAlignment(QtCore.Qt.AlignCenter)
        self.diameter_1.setObjectName("diameter_1")
        self.gridLayout.addWidget(self.diameter_1, 5, 0, 1, 1)
        self.power_2 = QtWidgets.QLabel(self.centralwidget)
        self.power_2.setAlignment(QtCore.Qt.AlignCenter)
        self.power_2.setObjectName("power_2")
        self.gridLayout.addWidget(self.power_2, 7, 2, 1, 1)
        self.label_28 = QtWidgets.QLabel(self.centralwidget)
        self.label_28.setAlignment(QtCore.Qt.AlignCenter)
        self.label_28.setObjectName("label_28")
        self.gridLayout.addWidget(self.label_28, 7, 1, 1, 1)
        self.name_1 = QtWidgets.QLabel(self.centralwidget)
        self.name_1.setAlignment(QtCore.Qt.AlignCenter)
        self.name_1.setFont(QtGui.QFont("Roboto", 8, QtGui.QFont.Bold))
        self.name_1.setObjectName("name_1")
        self.name_1.adjustSize()
        self.gridLayout.addWidget(self.name_1, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 462, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Сравнение"))
        self.label_24.setText(_translate("MainWindow", "Запас хода, км"))
        self.label_27.setText(_translate("MainWindow", "Макс. скорость, км/ч"))
        self.label_18.setText(_translate("MainWindow", "Наличие подвески"))
        self.label_8.setText(_translate("MainWindow", "Ёмкость аккумулятора, Втч"))
        self.label_5.setText(_translate("MainWindow", "Цена, ₽"))
        self.label.setText(_translate("MainWindow", "Сравнение"))
        self.label_25.setText(_translate("MainWindow", "Диаметр"))
        self.label_16.setText(_translate("MainWindow", "Вес, кг"))
        self.diameter_1.setText(_translate("MainWindow", "TextLabel"))
        self.label_28.setText(_translate("MainWindow", "Мощность, Вт"))


class GuideWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(595, 392)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setStyleSheet("font: 14pt \"Microsoft JhengHei UI\";")
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout_2.addWidget(self.plainTextEdit, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 595, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Гайд"))


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.selectbtn.clicked.connect(self.bpress)
        self.srbtn.clicked.connect(self.compare)
        self.guidebtn.clicked.connect(self.guide)
        self.listWidget.itemClicked.connect(self.euc)

    def keyPressEvent(self, event):
        if event.key() in (Qt.Key_Return, Qt.Key_Enter):
            self.bpress()

    def bpress(self):
        self.listWidget.clear()
        d = self.minprice.text()
        h = self.maxprice.text()
        y = self.minpwrres.text()
        j = self.maxpwrres.text()
        if d != '' and not d.isdigit() or h != '' and not h.isdigit() or \
                y != '' and not y.isdigit() or j != '' and not j.isdigit():
            mesg = QMessageBox()
            mesg.setWindowTitle("Ошибка")
            mesg.setText("Вводите числа в поля ввода.")
            mesg.setIcon(QMessageBox.Critical)
            mesg.exec_()
            self.minprice.setText('')
            self.maxprice.setText('')
            self.minpwrres.setText('')
            self.maxpwrres.setText('')
            sd = False
        else:
            sd = True
        if d != '' and d.isdigit():
            d = int(self.minprice.text())
        else:
            d = 0
        if h != '' and h.isdigit():
            h = int(self.maxprice.text())
        else:
            h = 10000000
        if y != '' and y.isdigit():
            y = int(self.minpwrres.text())
        else:
            y = 0
        if j != '' and j.isdigit():
            j = int(self.maxpwrres.text())
        else:
            j = 10000000
        if self.diameter.currentText() != 'Все':
            k = int(self.diameter.currentText())
            n = k
        else:
            k = 0
            n = 25
        if self.brand.currentText() != 'Все':
            s = self.brand.currentText()
            b = s
        else:
            s = 'Inmotion'
            b = 'Ninebot'
        if sd:
            con = sqlite3.connect("euc_copy.sqlite")
            cur = con.cursor()
            names = cur.execute(f"SELECT name FROM eucs WHERE price BETWEEN ? AND ? AND pwrres BETWEEN ? AND ? "
                                f"AND diameter BETWEEN ? AND ? AND brand_id BETWEEN (SELECT id FROM brands WHERE "
                                f"brand=?) AND (SELECT id FROM brands WHERE brand=?)",
                                (d, h, y, j, k, n, s, b)).fetchall()
            con.close()
            for item in names:
                self.listWidget.addItem(item[0])

    def euc(self, item):
        global x
        x = item.text()
        self.ec = OpenWidget()
        self.ec.show()
        self.ec.setFixedSize(700, 540)

    def compare(self):
        global mark
        gse = open('compare.txt', "r")
        nt = gse.readlines()
        gse.close()
        if len(nt) != 0:
            self.ev = TextWidget()
            self.ev.show()
            self.ev.setFixedSize(590, 350)
            sp.clear()
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Ошибка")
            msg.setText("Недостаточно товаров для сравнения")
            msg.setIcon(QMessageBox.Critical)
            msg.exec_()

    def guide(self):
        self.ecx = GuideWidget()
        self.ecx.show()


class GuideWidget(QMainWindow, GuideWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class TextWidget(QMainWindow, TextWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        gtg = open('compare.txt', 'r')
        gtd = gtg.readlines()
        gtg.close()
        gtd[0] = ''.join(gtd[0].split('\n')).split(' vs ')
        for u in range(1, len(gtd)):
            gtd[u] = ''.join(gtd[u].split('\n')).split()
        self.weight_2.setText(gtd[7][2])
        self.susp_1.setText(gtd[8][0])
        self.pwrres_2.setText(gtd[3][2])
        self.name_2.setText(gtd[0][1])
        self.pwrres_1.setText(gtd[3][0])
        self.maxspeed_2.setText(gtd[5][2])
        self.price_1.setText(gtd[1][0])
        self.susp_2.setText(gtd[8][2])
        self.diameter_2.setText(gtd[4][2])
        self.weight_1.setText(gtd[7][0])
        self.price_2.setText(gtd[1][2])
        self.power_1.setText(gtd[6][0])
        self.maxspeed_1.setText(gtd[5][0])
        self.capacity_2.setText(gtd[2][2])
        self.capacity_1.setText(gtd[2][0])
        self.diameter_1.setText(gtd[4][0])
        self.power_2.setText(gtd[6][2])
        self.name_1.setText(gtd[0][0])


class OpenWidget(QMainWindow, OpenWindow):
    def __init__(self):
        global x
        super().__init__()
        self.setupUi(self)
        con = sqlite3.connect("euc_copy.sqlite")
        cur = con.cursor()
        xcv = cur.execute("""SELECT * FROM eucs WHERE name=?""", (x,)).fetchall()
        con.close()
        self.maxspeed.setText('Макс. скорость: ' + str(xcv[0][6]) + ' км/ч')
        self.capacity.setText('Ёмкость аккумулятора: ' + str(xcv[0][7]) + ' Втч')
        self.price.setText('Цена: ' + str(xcv[0][3]) + '₽')
        self.diameter.setText('Диаметр колеса: ' + str(xcv[0][1]) + '"')
        self.weight.setText('Вес: ' + str(xcv[0][5]) + ' кг')
        self.pwrres.setText('Запас хода: ' + str(xcv[0][4]) + ' км')
        self.power.setText('Мощность: ' + str(xcv[0][2]) + ' Вт')
        self.name.setText(xcv[0][8])
        self.nn = xcv[0][8]
        self.pixmap = QPixmap(xcv[0][9])
        self.photo.setPixmap(self.pixmap.scaled(500, 500))
        self.compare.clicked.connect(self.compare_event)

    def compare_event(self):
        if len(sp) == 0:
            gse = open('compare.txt', "w")
            gse.close()
        if len(sp) < 2:
            sp.add(self.nn)
        if len(sp) == 2:
            msx = open("compare.txt", 'w')
            con = sqlite3.connect("euc_copy.sqlite")
            cur = con.cursor()
            gs = list(sp)
            gsx = list(cur.execute(f"SELECT * FROM eucs WHERE name=?", (gs[0],)).fetchall())
            gsxr = list(cur.execute(f"SELECT * FROM eucs WHERE name=?", (gs[1],)).fetchall())
            con.close()
            msx.write(gsx[0][8] + ' vs ' + gsxr[0][8] + '\n')
            msx.write(str(gsx[0][3]) + ' vs ' + str(gsxr[0][3]) + ' -Цена' + '\n')
            msx.write(str(gsx[0][7]) + ' vs ' + str(gsxr[0][7]) + ' -Ёмкость аккумулятора' + '\n')
            msx.write(str(gsx[0][4]) + ' vs ' + str(gsxr[0][4]) + ' -Запас хода' + '\n')
            msx.write(str(gsx[0][1]) + ' vs ' + str(gsxr[0][1]) + ' -Диаметр' + '\n')
            msx.write(str(gsx[0][6]) + ' vs ' + str(gsxr[0][6]) + ' -Макс. скорость' + '\n')
            msx.write(str(gsx[0][2]) + ' vs ' + str(gsxr[0][2]) + ' -Мощность' + '\n')
            msx.write(str(gsx[0][5]) + ' vs ' + str(gsxr[0][5]) + ' -Вес' + '\n')
            if gsx[0][10] == 1:
                r = 'Да'
            else:
                r = 'Нет'
            if gsxr[0][10] == 1:
                i = 'Да'
            else:
                i = 'Нет'
            msx.write(r + ' vs ' + i + ' -Наличие подвески')
            msx.close()


StyleSheet = """QMainWindow {background-color: rgb(220, 210, 150)}"""
if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('fusion')
    app.setStyleSheet(StyleSheet)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
