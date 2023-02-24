# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'examen.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import platform
import sys
import segona
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QMenu, QMenuBar, QSizePolicy, QStatusBar,
    QTextEdit, QVBoxLayout, QWidget, QFileDialog)
from PySide6.QtPrintSupport import(QPrinter, QPrintDialog)

class MainWindow(QMainWindow):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.Nou = QAction(MainWindow)
        self.Nou.setObjectName(u"Nou")
        self.Obrir = QAction(MainWindow)
        self.Obrir.setObjectName(u"Obrir")
        self.Obrir = obrir_arxiu(self)
        self.Guardar = QAction(MainWindow)
        self.Guardar.setObjectName(u"Guardar")
        self.Guardar = guardar_arxiu(self)
        self.Guardar_com = QAction(MainWindow)
        self.Guardar_com.setObjectName(u"Guardar_com")
        self.Imprimir = QAction(MainWindow)
        self.Imprimir.setObjectName(u"Imprimir")
        self.Imprimir = imprimir_arxiu(self)
        self.Tancar = QAction(MainWindow)
        self.Tancar.setObjectName(u"Tancar")
        self.Eixir = QAction(MainWindow)
        self.Eixir.setObjectName(u"Eixir")
        self.actionQuant_a_l_editor = QAction(MainWindow)
        self.actionQuant_a_l_editor.setObjectName(u"actionQuant_a_l_editor")
        #self.actionQuant_a_l_editor = obrir_segona(self)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")

        self.verticalLayout.addWidget(self.textEdit)


        self.horizontalLayout.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menuArxiu = QMenu(self.menubar)
        self.menuArxiu.setObjectName(u"menuArxiu")
        self.menuAjuda = QMenu(self.menubar)
        self.menuAjuda.setObjectName(u"menuAjuda")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArxiu.menuAction())
        self.menubar.addAction(self.menuAjuda.menuAction())
        self.menuArxiu.addAction(self.Nou)
        self.menuArxiu.addAction(self.Obrir)
        self.menuArxiu.addAction(self.Guardar)
        self.menuArxiu.addAction(self.Guardar_com)
        self.menuArxiu.addAction(self.Imprimir)
        self.menuArxiu.addAction(self.Tancar)
        self.menuArxiu.addAction(self.Eixir)
        self.menuAjuda.addAction(self.actionQuant_a_l_editor)

        barra_estado = self.statusBar()
        barra_estado.addPermanentWidget


        self.retranslateUi(MainWindow)
        self.Nou.triggered.connect(self.textEdit.clear)
        self.Eixir.triggered.connect(MainWindow.close)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Nou.setText(QCoreApplication.translate("MainWindow", u"Nou", None))
#if QT_CONFIG(shortcut)
        self.Nou.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
        self.Obrir.setText(QCoreApplication.translate("MainWindow", u"Obrir", None))
#if QT_CONFIG(shortcut)
        self.Obrir.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.Guardar.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
#if QT_CONFIG(shortcut)
        self.Guardar.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.Guardar_com.setText(QCoreApplication.translate("MainWindow", u"Guardar com", None))
#if QT_CONFIG(shortcut)
        self.Guardar_com.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+S", None))
#endif // QT_CONFIG(shortcut)
        self.Imprimir.setText(QCoreApplication.translate("MainWindow", u"Imprimir", None))
#if QT_CONFIG(shortcut)
        self.Imprimir.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+P", None))
#endif // QT_CONFIG(shortcut)
        self.Tancar.setText(QCoreApplication.translate("MainWindow", u"Tancar", None))
#if QT_CONFIG(shortcut)
        self.Tancar.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+W", None))
#endif // QT_CONFIG(shortcut)
        self.Eixir.setText(QCoreApplication.translate("MainWindow", u"Eixir", None))
#if QT_CONFIG(shortcut)
        self.Eixir.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.actionQuant_a_l_editor.setText(QCoreApplication.translate("MainWindow", u"Quant a l'editor", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Editor de textos", None))
        self.menuArxiu.setTitle(QCoreApplication.translate("MainWindow", u"Arxiu", None))
        self.menuAjuda.setTitle(QCoreApplication.translate("MainWindow", u"Ajuda", None))
    # retranslateUi

def obrir_arxiu(self):
    obrir = QFileDialog.getOpenFileName(
        self, caption = "Obrir fitxer...", dir = "."
    )

    fitxer = obrir[0]

def guardar_arxiu(self):
     guardar = QFileDialog.getSaveFileName(
          self, caption = "Guarda fitxer...", dir = "."
     )
     fitxer = guardar
     print(fitxer)

def imprimir_arxiu(self):
     imprimir = QPrintDialog(self)

#def obrir_segona(self):
#     self.ventana = QtWidgets.QMainWindow()
#     self.ui = Ui_Segona()
#     self.ui.setupUi(self.ventana)
#     self.ventana.show()
     

if __name__ == "__main__":

        window = MainWindow()
        window.show()
        window.exec()