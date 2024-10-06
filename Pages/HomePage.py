from PyQt5 import QtCore, QtGui, QtWidgets
from UIfunctions import load_csv_data, on_column_selected
from Algorithms import merge_sort, quick_sort, radix_sort_strings, counting_sort_strings, bucket_sort, bubble_sort, selection_sort, insertion_sort, tim_sort, heap_sort

class SortingForm(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(SortingForm, self).__init__(parent)
        self.parent = parent
        self.setupUi()

    def on_sort_button_clicked(self, algo):
        selected_items = self.tableWidget.selectedItems()
        if selected_items:
            selected_column = selected_items[0].column()
            QtCore.QTimer.singleShot(0, lambda: self.perform_sort(algo, selected_column))

    def perform_sort(self, algo, selected_column):
        raw_data = []

        # Extract the data from the table into raw_data
        for row in range(self.tableWidget.rowCount()):
            row_data = [self.tableWidget.item(row, col).text() for col in range(self.tableWidget.columnCount())]
            raw_data.append(row_data)

        # Determine if the selected column data is numeric
        is_numeric = True
        for i in range(len(raw_data)):
            try:
                raw_data[i][selected_column] = int(raw_data[i][selected_column])  # Attempt to convert to int
            except ValueError:
                is_numeric = False  # If conversion fails, it's not numeric

        # Initialize the progress bar
        self.progressBar.setValue(0)
        self.progressBar.setMaximum(100)

        # Sort the raw_data based on the selected algorithm
        if algo == 'Merge':
            sorted_data = merge_sort(raw_data, selected_column)
        elif algo == 'Quick':
            sorted_data = quick_sort(raw_data, selected_column)
        elif algo == 'Counting':
            if is_numeric:
                sorted_data = counting_sort_strings([str(row[selected_column]) for row in raw_data], position=0)
            else:
                sorted_data = counting_sort_strings([row[selected_column] for row in raw_data], position=0)
        elif algo == 'Radix':
            if is_numeric:
                sorted_data = radix_sort_strings([str(row[selected_column]) for row in raw_data])
            else:
                sorted_data = radix_sort_strings([row[selected_column] for row in raw_data])
        elif algo == 'Bucket':
            sorted_data = bucket_sort([row[selected_column] for row in raw_data])
        elif algo == 'Bubble':
            sorted_data = bubble_sort([row[selected_column] for row in raw_data])
        elif algo == 'Selection':
            sorted_data = selection_sort([row[selected_column] for row in raw_data])
        elif algo == 'Insertion':
            sorted_data = insertion_sort(raw_data)
        elif algo == 'Tim':
            sorted_data = tim_sort(raw_data)
        elif algo == 'Heap':
            sorted_data = heap_sort(raw_data)

        # Simulate progress for the sorting operation
        for i in range(101):
            QtCore.QThread.msleep(10)  # Simulate time taken for sorting
            self.progressBar.setValue(i)

        # Map the sorted strings back to their original rows
        sorted_raw_data = [raw_data[i] for i in sorted(range(len(raw_data)), key=lambda k: (str(raw_data[k][selected_column]) if not is_numeric else raw_data[k][selected_column]))]

        # Update the table with the sorted data
        self.update_table(sorted_raw_data)

        # Display a done message
        self.show_done_message()

    def show_done_message(self):
        """Display a message box when sorting is done."""
        msg_box = QtWidgets.QMessageBox(self)
        msg_box.setWindowTitle("Sorting Done")
        msg_box.setText("Sorting is complete!")
        msg_box.setIcon(QtWidgets.QMessageBox.Information)
        msg_box.addButton("OK", QtWidgets.QMessageBox.AcceptRole)

        # Show the message box
        msg_box.exec_()

        # Reset the progress bar
        self.progressBar.setValue(0)

    def update_table(self, sorted_data):
        """Updates the table with the sorted data."""
        self.tableWidget.setRowCount(len(sorted_data))  # Adjust row count to fit sorted data
        for row_index, row_data in enumerate(sorted_data):
            for col_index, item in enumerate(row_data):
                self.tableWidget.setItem(row_index, col_index, QtWidgets.QTableWidgetItem(str(item)))

    def setupUi(self):
        self.setObjectName("SortingForm")
        self.resize(1200, 800)
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

        # Load CSV button
        self.loadCsvButton = QtWidgets.QPushButton("Load CSV")
        self.loadCsvButton.setStyleSheet("background-color: green; color: white;")
        self.loadCsvButton.clicked.connect(self.load_data)
        self.verticalLayout.addWidget(self.loadCsvButton)

        # Sorting algorithm buttons (grid layout)
        self.gridLayout = QtWidgets.QGridLayout()
        self.sortingButtons = {}
        algorithms = ['Bubble', 'Selection', 'Insertion', 'Merge', 'Quick', 'Counting', 'Radix', 'Bucket', 'Tim', 'Heap']

        for i, algo in enumerate(algorithms):
            self.sortingButtons[algo] = QtWidgets.QPushButton(f"{algo} Sort")
            self.sortingButtons[algo].setStyleSheet("background-color: darkblue; color: white;")
            self.sortingButtons[algo].clicked.connect(lambda _, a=algo: self.on_sort_button_clicked(a))
            self.gridLayout.addWidget(self.sortingButtons[algo], i // 5, i % 5)

        self.verticalLayout.addLayout(self.gridLayout)

        # Add a table with 7 columns and 10 rows
        self.tableWidget = QtWidgets.QTableWidget(self)
        self.tableWidget.setRowCount(10)  # Set the number of rows
        self.tableWidget.setColumnCount(7)  # Set the number of columns
        self.tableWidget.setHorizontalHeaderLabels(['Column 1', 'Column 2', 'Column 3', 'Column 4', 'Column 5', 'Column 6', 'Column 7'])
        self.tableWidget.setStyleSheet("background-color: white; color: black;")
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectColumns)  # Enable column selection
        self.verticalLayout.addWidget(self.tableWidget)

        # Connect the selection change signal to the on_column_selected method
        self.tableWidget.itemSelectionChanged.connect(self.on_column_selected)

        # Progress Bar
        self.progressBar = QtWidgets.QProgressBar(self)
        self.progressBar.setValue(0)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout.addWidget(self.progressBar)

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

    def on_column_selected(self):
        """Handle the event when a column is selected in the QTableWidget."""
        selected_items = self.tableWidget.selectedItems()
        if selected_items:
            selected_column = selected_items[0].column()  # Get the column of the first selected item
            print(f"Selected column: {selected_column}")  # For debugging purposes

    def load_data(self):
        """Load data into the table when the button is clicked."""
        load_csv_data(self.tableWidget)  # Load CSV data into the table

    def go_back(self):
        """Go back to the previous screen."""
        self.parent.setCurrentIndex(0)  # Assuming you want to go back to the first widget in the stacked layout

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWin = QtWidgets.QStackedWidget()
    form = SortingForm(mainWin)
    mainWin.addWidget(form)
    mainWin.show()
    sys.exit(app.exec_())
