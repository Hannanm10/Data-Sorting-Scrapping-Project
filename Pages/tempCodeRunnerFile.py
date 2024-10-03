import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor, QIcon, QPixmap, QFont


class HomePage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Home Page")
        self.setGeometry(100, 100, 1200, 800)
        self.setFixedSize(1200, 800)

        # Set the window icon
        self.setWindowIcon(QIcon('Icons/mainicon.png'))

        # Set up the main layout
        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)
        
        layout = QVBoxLayout(main_widget)

        # Add space above the title (to push the title down a bit)

        title_layout = QHBoxLayout()

        # Create a QLabel for the icon
        icon_label = QLabel()
        pixmap = QPixmap('Icons/mainicon.png')  # Load the icon image
        icon_label.setPixmap(pixmap.scaled(50, 50, Qt.KeepAspectRatio))  # Resize the icon

        # Create a QLabel for the title
        title_label = QLabel("Welcome to GoSort")
        title_font = QFont("Arial", 32, QFont.Bold)  # Set font size and bold (make it bigger)
        title_label.setFont(title_font)

        # Add the icon and title to the horizontal layout
        title_layout.addWidget(icon_label)
        title_layout.addWidget(title_label)
        title_layout.addStretch(5)  # To push the title and icon to the center

        # Add the title layout to the main layout
        layout.addLayout(title_layout)

        # Add more space below the title to move it up vertically
        layout.addStretch(3)  # Add more vertical space below the title

        # Create two buttons with rounded edges and blue text
        self.button1 = QPushButton("Sorting the website")
        self.button2 = QPushButton("Sort the URL")

        # Style buttons
        self.button1.setStyleSheet(
            "background-color: green;"
            "color: blue;"
            "border-radius: 15px;"   # Rounded edges
            "padding: 10px;"
            "font-size: 16px;"
        )
        self.button2.setStyleSheet(
            "background-color: green;"
            "color: blue;"
            "border-radius: 15px;"   # Rounded edges
            "padding: 10px;"
            "font-size: 16px;"
        )

        # Center the buttons
        layout.addWidget(self.button1, alignment=Qt.AlignCenter)
        layout.addWidget(self.button2, alignment=Qt.AlignCenter)

        # Add space after buttons to center everything vertically
        layout.addStretch(2)

        # Set the background color to white
        palette = QPalette()
        palette.setColor(QPalette.Background, QColor("white"))
        self.setPalette(palette)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HomePage()
    window.show()
    sys.exit(app.exec_())
