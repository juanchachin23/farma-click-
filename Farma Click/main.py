import sys
import pyodbc
from PyQt5 import uic, QtCore
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QMessageBox, QLabel, QVBoxLayout
import mysql.connector
import numpy
from PyQt5.QtCore import QDate, QDateTime, pyqtSlot
import datetime
from datetime import  timedelta
from PyQt5 import QtGui
from PyQt5.QtGui import QIcon



class MainWindow(QMainWindow):
    
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("1.ui", self)
        
        self.current_path = None
        # Establece el título de la ventana
        self.setWindowTitle("Farma Click")

        # Establece el icono de la ventana
        
        icon_path = "logo.jpg"
        self.setWindowIcon(QIcon(icon_path))

        
        
        self.pushButton_2.clicked.connect(self.registrarentradanueva)
        self.pushButton.clicked.connect(self.vacio)
        self.pushButton_3.clicked.connect(self.registrarentradanueva)

        
        
    
    def registrarentradanueva(self):
        if self.validar_datos():
            cantidad = float(self.doubleSpinBox.value())
            p = cantidad * 0.20
            total = cantidad + p

            floatTotal = str(total)
            

            self.label_3.clear()
            self.label_3.setText(floatTotal)
            
        


        
    
    def vacio(self):
        total = 0
        print (total)

    def validar_datos(self):
        band = True
        alert = ""
        if (self.doubleSpinBox.value()) == 0.00:
            alert = alert + "Por favor indique un numero\n"
            band = False


        if not band:
            
            dialog = QMessageBox()
            dialog.setText(alert)
            dialog.setWindowTitle('Aviso')
            dialog.setIcon(QMessageBox.Warning)
            dialog.setDetailedText(
                'Para poder sacar un porcentaje es necesario que coloque un numero')
            dialog.setStandardButtons(QMessageBox.Retry)
            dialog.exec_()

        else:
            self.registrarentradanueva

        return band
        

        

if __name__=='__main__':
    app = QApplication(sys.argv)
    ui = MainWindow()

    ui.show()
    app.exec_()