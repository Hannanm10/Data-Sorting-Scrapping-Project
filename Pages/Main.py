# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets


class SecondWindow(QtWidgets.QWidget):
    def __init__(self, text):
        super(SecondWindow, self).__init__()
        self.setupUi()

        # Optionally use the text parameter to display in the second window
        self.titleLabel.setText(f"Don Sorting - {text}")

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(1200, 800)
        self.setWindowTitle("Project1")

        # Set main window background color
        self.setStyleSheet("background-color: lightblue;")  # Light blue background

        # Main vertical layout
        self.verticalLayout = QtWidgets.QVBoxLayout(self)

        # Title label
        self.titleLabel = QtWidgets.QLabel("Don Sorting", self)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.titleLabel.setFont(font)
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setStyleSheet("background-color: darkblue; color: white;")  # Dark blue background with white text
        self.verticalLayout.addWidget(self.titleLabel)

        # Sorting algorithm buttons (grid layout)
        self.gridLayout = QtWidgets.QGridLayout()
        self.sortingButtons = {}
        algorithms = ['Bubble', 'Selection', 'Insertion', 'Merge', 'Quick', 'Counting', 'Radix', 'Bucket', 'Tim', 'Heap']

        for i, algo in enumerate(algorithms):
            self.sortingButtons[algo] = QtWidgets.QPushButton(f"{algo} Sort", self)
            self.sortingButtons[algo].setStyleSheet("background-color: darkblue; color: white;")  # Dark blue buttons with white text
            self.sortingButtons[algo].clicked.connect(lambda _, a=algo: self.on_sort_button_clicked(a))
            self.gridLayout.addWidget(self.sortingButtons[algo], i // 5, i % 5)

        self.verticalLayout.addLayout(self.gridLayout)

        # Data grid (7 columns)
        self.tableWidget = QtWidgets.QTableWidget(self)
        self.tableWidget.setRowCount(0)  # Start with no rows
        self.tableWidget.setColumnCount(7)  # 7 columns
        self.tableWidget.setHorizontalHeaderLabels(["Name", "Price", "Original Price", "Total Sold", "Estimated Delivery", "Rating", "Total Ratings"])
        self.verticalLayout.addWidget(self.tableWidget)

        # URL input section (label and button)
        self.urlLayout = QtWidgets.QHBoxLayout()
        self.urlLabel = QtWidgets.QLabel("Enter URL:", self)
        self.urlLabel.setStyleSheet("color: darkblue;")  # Dark blue text for URL label
        self.urlLineEdit = QtWidgets.QLineEdit(self)
        self.urlButton = QtWidgets.QPushButton("Button", self)
        self.urlButton.setStyleSheet("background-color: darkblue; color: white;")  # Dark blue button with white text

        self.urlLayout.addWidget(self.urlLabel)
        self.urlLayout.addWidget(self.urlLineEdit)
        self.urlLayout.addWidget(self.urlButton)

        self.verticalLayout.addLayout(self.urlLayout)

        # Control buttons (pause, start, resume, stop) and progress bar
        self.controlLayout = QtWidgets.QHBoxLayout()
        self.startButton = QtWidgets.QPushButton("Start", self)
        self.pauseButton = QtWidgets.QPushButton("Pause", self)
        self.resumeButton = QtWidgets.QPushButton("Resume", self)
        self.stopButton = QtWidgets.QPushButton("Stop", self)

        self.startButton.setStyleSheet("background-color: lightgreen;")
        self.pauseButton.setStyleSheet("background-color: lightyellow;")
        self.resumeButton.setStyleSheet("background-color: lightblue;")
        self.stopButton.setStyleSheet("background-color: lightcoral;")

        self.progressBar = QtWidgets.QProgressBar(self)
        self.progressBar.setValue(0)

        self.controlLayout.addWidget(self.startButton)
        self.controlLayout.addWidget(self.pauseButton)
        self.controlLayout.addWidget(self.resumeButton)
        self.controlLayout.addWidget(self.stopButton)
        self.controlLayout.addWidget(self.progressBar)

        self.verticalLayout.addLayout(self.controlLayout)

        # Time complexity label and uneditable textbox
        self.timeComplexityLayout = QtWidgets.QHBoxLayout()
        self.timeLabel = QtWidgets.QLabel("Time Complexity:", self)
        self.timeComplexityBox = QtWidgets.QLineEdit("Hello World", self)
        self.timeComplexityBox.setReadOnly(True)
        self.timeComplexityBox.setStyleSheet("background-color: white; color: black;")

        self.timeComplexityLayout.addWidget(self.timeLabel)
        self.timeComplexityLayout.addWidget(self.timeComplexityBox)

        self.verticalLayout.addLayout(self.timeComplexityLayout)

        # Add a small label at the bottom of the screen
        self.footerLabel = QtWidgets.QLabel("This is the footer", self)
        self.footerLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.footerLabel.setStyleSheet("color: gray;")
        self.verticalLayout.addWidget(self.footerLabel)

    # Sorting button onclick function placeholder
    def on_sort_button_clicked(self, algo):
        print(f"{algo} sort button clicked")


class BasicPage(QtWidgets.QMainWindow):
    def __init__(self):
        super(BasicPage, self).__init__()

        self.setWindowTitle("Basic PyQt Page")
        self.setGeometry(100, 100, 400, 300)

        # Central widget
        self.central_widget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.central_widget)

        # Vertical layout
        self.layout = QtWidgets.QVBoxLayout(self.central_widget)

        # Label
        self.label = QtWidgets.QLabel("Enter some text:", self)
        self.layout.addWidget(self.label)

        # Text input field
        self.text_input = QtWidgets.QLineEdit(self)
        self.layout.addWidget(self.text_input)

        # Button
        self.submit_button = QtWidgets.QPushButton("Submit", self)
        self.submit_button.clicked.connect(self.open_second_window)
        self.layout.addWidget(self.submit_button)

    def open_second_window(self):
        # Get text from the input field
        text = self.text_input.text()

        # Open the second window with the entered text
        self.second_window = SecondWindow(text)
        self.second_window.show()

        # Close the current window
        self.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_window = BasicPage()
    main_window.show()
    sys.exit(app.exec_())
