from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 800)
        MainWindow.setWindowTitle("Project1")

        # Set main window background color
        MainWindow.setStyleSheet("background-color: lightblue;")  # Light blue background
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Main vertical layout
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)

        # Title label
        self.titleLabel = QtWidgets.QLabel("Don Sorting", self.centralwidget)  # Changed to "Don Sorting"
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
            self.sortingButtons[algo] = QtWidgets.QPushButton(f"{algo} Sort")
            self.sortingButtons[algo].setStyleSheet("background-color: darkblue; color: white;")  # Dark blue buttons with white text
            self.sortingButtons[algo].clicked.connect(lambda _, a=algo: self.on_sort_button_clicked(a))
            self.gridLayout.addWidget(self.sortingButtons[algo], i // 5, i % 5)
        
        self.verticalLayout.addLayout(self.gridLayout)

        # Data grid (7 columns)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setRowCount(0)  # Start with no rows
        self.tableWidget.setColumnCount(7)  # 7 columns
        self.tableWidget.setHorizontalHeaderLabels(["Name", "Price", "Original Price", "Total Sold", "Estimated Delivery", "Rating", "Total Ratings"])
        self.verticalLayout.addWidget(self.tableWidget)

        # URL input section (label and button)
        self.urlLayout = QtWidgets.QHBoxLayout()
        self.urlLabel = QtWidgets.QLabel("Enter URL:")
        self.urlLabel.setStyleSheet("color: darkblue;")  # Dark blue text for URL label
        self.urlLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.urlButton = QtWidgets.QPushButton("Button", self.centralwidget)
        self.urlButton.setStyleSheet("background-color: darkblue; color: white;")  # Dark blue button with white text
        
        self.urlLayout.addWidget(self.urlLabel)
        self.urlLayout.addWidget(self.urlLineEdit)
        self.urlLayout.addWidget(self.urlButton)
        
        self.verticalLayout.addLayout(self.urlLayout)

        # Control buttons (pause, start, resume, stop) and progress bar
        self.controlLayout = QtWidgets.QHBoxLayout()
        self.startButton = QtWidgets.QPushButton("Start", self.centralwidget)
        self.pauseButton = QtWidgets.QPushButton("Pause", self.centralwidget)
        self.resumeButton = QtWidgets.QPushButton("Resume", self.centralwidget)
        self.stopButton = QtWidgets.QPushButton("Stop", self.centralwidget)
        
        self.startButton.setStyleSheet("background-color: lightgreen;")
        self.pauseButton.setStyleSheet("background-color: lightyellow;")
        self.resumeButton.setStyleSheet("background-color: lightblue;")
        self.stopButton.setStyleSheet("background-color: lightcoral;")
        
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setValue(0)
        
        self.controlLayout.addWidget(self.startButton)
        self.controlLayout.addWidget(self.pauseButton)
        self.controlLayout.addWidget(self.resumeButton)
        self.controlLayout.addWidget(self.stopButton)
        self.controlLayout.addWidget(self.progressBar)

        self.verticalLayout.addLayout(self.controlLayout)

        # Time complexity label and uneditable textbox
        self.timeComplexityLayout = QtWidgets.QHBoxLayout()
        self.timeLabel = QtWidgets.QLabel("Time Complexity:")
        self.timeComplexityBox = QtWidgets.QLineEdit("Hello World", self.centralwidget)
        self.timeComplexityBox.setReadOnly(True)
        self.timeComplexityBox.setStyleSheet("background-color: white; color: black;")
        
        self.timeComplexityLayout.addWidget(self.timeLabel)
        self.timeComplexityLayout.addWidget(self.timeComplexityBox)

        self.verticalLayout.addLayout(self.timeComplexityLayout)

        # Add a small label at the bottom of the screen
        self.footerLabel = QtWidgets.QLabel("This is the footer", self.centralwidget)
        self.footerLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.footerLabel.setStyleSheet("color: gray;")
        self.verticalLayout.addWidget(self.footerLabel)

        # Set central widget and main window configurations
        MainWindow.setCentralWidget(self.centralwidget)

    # Sorting button onclick function placeholder
    def on_sort_button_clicked(self, algo):
        print(f"{algo} sort button clicked")  # Does nothing for now


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
