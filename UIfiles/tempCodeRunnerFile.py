class SortingForm(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(SortingForm, self).__init__(parent)
        self.setObjectName("SortingForm")
        self.resize(800, 600)
        self.setWindowTitle("Sorting Algorithms")

        # Example UI elements for Sorting Form
        layout = QtWidgets.QVBoxLayout(self)
        label = QtWidgets.QLabel("Welcome to the Sorting Algorithms Page", self)
        label.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(label)

        # You can add more elements for sorting algorithms here
        self.setLayout(layout)