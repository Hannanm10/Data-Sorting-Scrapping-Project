# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Homepage.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 800)
        MainWindow.setWindowState(QtCore.Qt.WindowNoState)  # Ensure not maximized by default
        
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Icons/mainicon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color:#0D98BA;\n"
                                 "background-color:lightblue;")
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        # Create vertical layout for central widget
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(50, 20, 50, 20)
        self.verticalLayout.setSpacing(20)
        
        # Title Label
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(False)  # Set to False to avoid bold effect
        font.setWeight(25)   # Further reduced thickness (less than 30)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("background-color: #0A74A6; color: white;")  # Dark blue with white text
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setText("Welcome to GoSort")
        self.label.setFixedHeight(60)  # Adjust the height
        self.label.setMaximumWidth(800)  # Limit the width to shorten the label
        
        # Add label to the layout
        self.verticalLayout.addWidget(self.label)
    
        # Icon Label
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setPixmap(QtGui.QPixmap("../Icons/mainicon.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setFixedSize(64, 64)  # Adjust icon size
        self.verticalLayout.addWidget(self.label_2)
        
        # First Button (Go to Sorting)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color:#0D98BA;\n"
                                      "border-radius: 10px;")
        self.pushButton.setText("Go to Sorting")
        self.pushButton.setFixedHeight(40)
        self.pushButton.setFixedWidth(300)  # Adjust button width
        
        # Add button to the layout
        self.verticalLayout.addWidget(self.pushButton, alignment=QtCore.Qt.AlignCenter)  # Center the button
        
        # Second Button (Add URL)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color:#0D98BA;\n"
                                        "border-radius: 10px;")
        self.pushButton_2.setText("Add URL")
        self.pushButton_2.setFixedHeight(40)
        self.pushButton_2.setFixedWidth(300)  # Adjust button width
        
        # Add button to the layout
        self.verticalLayout.addWidget(self.pushButton_2, alignment=QtCore.Qt.AlignCenter)  # Center the button
        
        MainWindow.setCentralWidget(self.centralwidget)
        
        # Menu bar and status bar
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 20))  # Adjusted to match window size
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "GoSort"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
