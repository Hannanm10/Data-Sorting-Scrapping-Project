# coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets


class SortingForm(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(SortingForm, self).__init__(parent)
        self.setupUi()

    def setupUi(self):
        self.setObjectName("SortingForm")
        self.resize(800, 600)
        self.setWindowTitle("Sorting Algorithms")

        # Set widget background color
        self.setStyleSheet("background-color: lightblue;")  # Light blue background
        
        # Main vertical layout
        self.verticalLayout = QtWidgets.QVBoxLayout(self)

        # Welcome label
        self.label = QtWidgets.QLabel("Welcome to the Sorting Algorithms Page", self)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.label.setFont(font)
        self.verticalLayout.addWidget(self.label)

        # Sorting algorithm buttons (grid layout)
        self.gridLayout = QtWidgets.QGridLayout()
        self.sortingButtons = {}
        algorithms = ['Bubble', 'Selection', 'Insertion', 'Merge', 'Quick', 'Counting', 'Radix', 'Bucket', 'Tim', 'Heap']
        
        for i, algo in enumerate(algorithms):
            self.sortingButtons[algo] = QtWidgets.QPushButton(f"{algo} Sort")
            self.sortingButtons[algo].setStyleSheet("background-color: darkblue; color: white;")  # Dark blue buttons with white text
            self.sortingButtons[algo].clicked.connect(lambda _, a=algo: self.on_sort_button_clicked(a))
            self.gridLayout.addWidget(self.sortingButtons[algo], i // 5, i % 5)
        
        self.verticalLayout.addLayout(self.gridLayout)

        # Add a small label at the bottom of the screen
        self.footerLabel = QtWidgets.QLabel("This is the footer", self)
        self.footerLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.footerLabel.setStyleSheet("color: gray;")
        self.verticalLayout.addWidget(self.footerLabel)

        # Set the layout
        self.setLayout(self.verticalLayout)

    # Sorting button onclick function placeholder
    def on_sort_button_clicked(self, algo):
        print(f"{algo} sort button clicked") 


class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setupUi()

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(1200, 800)
        self.setWindowTitle("GoSort")

        # Set main window background color
        self.setStyleSheet("background-color: lightblue;")  # Light blue background

        # Central widget
        self.centralwidget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.centralwidget)

        # Create vertical layout for central widget
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(50, 20, 50, 50)  # Reduced bottom margin
        self.verticalLayout.setSpacing(20)

        # Title Label
        self.label = QtWidgets.QLabel("Welcome to GoSort", self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(False)  # Set to False to avoid bold effect
        font.setWeight(25)   # Further reduced thickness (less than 30)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setFixedHeight(60)  # Adjust the height
        self.verticalLayout.addWidget(self.label)

        # First Button (Go to Sorting)
        self.pushButton = QtWidgets.QPushButton("Go to Sorting", self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setFixedHeight(40)
        self.pushButton.setFixedWidth(300)  # Adjust button width
        self.pushButton.clicked.connect(self.open_sorting_form)  # Connect button click to open the sorting form
        self.verticalLayout.addWidget(self.pushButton, alignment=QtCore.Qt.AlignCenter)  # Center the button

        # Second Button (Add URL)
        self.pushButton_2 = QtWidgets.QPushButton("Add URL", self.centralwidget)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setFixedHeight(40)
        self.pushButton_2.setFixedWidth(300)  # Adjust button width
        self.verticalLayout.addWidget(self.pushButton_2, alignment=QtCore.Qt.AlignCenter)  # Center the button

        # Set window layout
        self.setLayout(self.verticalLayout)

    def open_sorting_form(self):
        # Create and show the SortingForm when the button is clicked
        self.sorting_form = SortingForm()  # Create SortingForm
        self.sorting_form.show()  # Show the SortingForm
        self.close()  # Close the current window


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_window = Ui_MainWindow()  # Create instance of main window
    main_window.show()  # Show the main window
    sys.exit(app.exec_())