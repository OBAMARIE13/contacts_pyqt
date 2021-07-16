import sys
import os
import re
import sqlite3
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QWidget, QMainWindow
from PyQt5.uic import loadUiType
from .mainw import Ui_MainWindow




#marie = Ui_MainWindow
FORM_CLASS,_ = loadUiType(os.path.join(os.path.dirname("__file__"), "ui/main.ui"))

class Contact(QMainWindow, FORM_CLASS):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.action()

    def action(self):
        self.submit_btn.clicked.connect(self.fonction)


    def fonction(self):
        name = self.first_name.text()
        last_name = self.last_name.text()
        email = self.email.text()
        number = self.number.text()
        message = self.message.toPlainText()
        
        if not name or not last_name or not email or not message:
            QtWidgets.QMessageBox.warning(self, "Error", "Remplissez les champs vides svp")
        else:
            regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
            if not re.match(regex, email):
                QtWidgets.QMessageBox.warning(self, "Error", "email incorrect")
            else:
                db = sqlite3.connect(os.path.join(os.path.dirname("__file__"),"database/data.db"))
                c = db.cursor()
                command = """ SELECT * FROM contact WHERE email=? AND message=? """
                resultat = c.execute(command, (email, message))
                if resultat.fetchone():
                    QtWidgets.QMessageBox.warning(self, "Error", "Message existe deja")
                else:
                    QtWidgets.QMessageBox.information(self, "Success", "Message envoyé avec succès")
                    db = sqlite3.connect(os.path.join(os.path.dirname("__file__"),"database/data.db"))
                    c = db.cursor()
                    valeur = (name, last_name, email, number, message)
                    c.execute("""INSERT INTO contact (first_name, last_name, email, number, message) VALUES (?,?,?,?,?)""", valeur)
                    db.commit()
                    self.first_name.clear()
                    self.last_name.clear()
                    self.email.clear()
                    self.number.clear()
                    self.message.clear()
                





        

