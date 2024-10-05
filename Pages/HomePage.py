# coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets


class SortingForm(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(SortingForm, self).__init__(parent)
        self.parent = parent  # Store the reference to the parent window (main window)
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

        # Add a table with 7 columns and 10 rows
        self.tableWidget = QtWidgets.QTableWidget(self)
        self.tableWidget.setRowCount(10)  # Set the number of rows
        self.tableWidget.setColumnCount(7)  # Set the number of columns
        self.tableWidget.setHorizontalHeaderLabels(['Column 1', 'Column 2', 'Column 3', 'Column 4', 'Column 5', 'Column 6', 'Column 7'])
        self.tableWidget.setStyleSheet("background-color: white; color: black;")
        self.verticalLayout.addWidget(self.tableWidget)

        # Start and Stop buttons
        self.buttonLayout = QtWidgets.QHBoxLayout()

        self.startButton = QtWidgets.QPushButton("Start", self)
        self.startButton.setStyleSheet("background-color: green; color: white;")
        self.startButton.setFixedSize(100, 40)
        self.startButton.clicked.connect(self.start_sorting)  # Start sorting functionality
        self.buttonLayout.addWidget(self.startButton)

        self.stopButton = QtWidgets.QPushButton("Stop", self)
        self.stopButton.setStyleSheet("background-color: darkred; color: white;")
        self.stopButton.setFixedSize(100, 40)
        self.stopButton.clicked.connect(self.stop_sorting)  # Stop sorting functionality
        self.buttonLayout.addWidget(self.stopButton)

        self.verticalLayout.addLayout(self.buttonLayout)

        # Time display label and text box
        self.timeLabel = QtWidgets.QLabel("Time taken (ms):", self)
        self.verticalLayout.addWidget(self.timeLabel)

        self.timeDisplay = QtWidgets.QLineEdit(self)
        self.timeDisplay.setReadOnly(True)  # Make it read-only to just display the time
        self.timeDisplay.setStyleSheet("background-color: white; color: black;")
        self.verticalLayout.addWidget(self.timeDisplay)

        # Go Back button
        self.backButton = QtWidgets.QPushButton("Go Back", self)
        self.backButton.setStyleSheet("background-color: red; color: white;")
        self.backButton.setFixedSize(100, 40)
        self.backButton.clicked.connect(self.go_back)
        self.verticalLayout.addWidget(self.backButton, alignment=QtCore.Qt.AlignCenter)

        # Add a small label at the bottom of the screen
        self.footerLabel = QtWidgets.QLabel("This is the footer", self)
        self.footerLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.footerLabel.setStyleSheet("color: gray;")
        self.verticalLayout.addWidget(self.footerLabel)

        # Set the layout
        self.setLayout(self.verticalLayout)

    # Placeholder function for sorting
    def on_sort_button_clicked(self, algo):
        print(f"{algo} sort button clicked")
        # Placeholder for sorting functionality

    # Start sorting functionality (to be implemented)
    def start_sorting(self):
        print("Sorting started")
        # Placeholder for starting sorting and measuring time

    # Stop sorting functionality (to be implemented)
    def stop_sorting(self):
        print("Sorting stopped")
        # Placeholder for stopping sorting

    # Go Back button function to return to the main window
    def go_back(self):
        self.close()
        self.mainform = Ui_MainWindow()  # Instantiate the Ui_Mainform class
        self.mainform.show()










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

        # Exit Button
        self.exitButton = QtWidgets.QPushButton("Exit", self.centralwidget)
        self.exitButton.setFont(font)
        self.exitButton.setFixedHeight(40)
        self.exitButton.setFixedWidth(300)  # Adjust button width
        self.exitButton.setStyleSheet("background-color: darkred; color: white;")  # Styling for the exit button
        self.exitButton.clicked.connect(self.close)  # Connect to close function
        self.verticalLayout.addWidget(self.exitButton, alignment=QtCore.Qt.AlignCenter)  # Center the button

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
