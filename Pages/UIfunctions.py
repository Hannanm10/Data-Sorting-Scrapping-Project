import csv,os
from PyQt5 import QtWidgets


def load_csv_data(table_widget):

    # Get the current directory where the script is located
    current_directory = os.path.dirname(os.path.abspath(__file__))
    csv_file = os.path.join(current_directory, "ScrapedDataFromEBAY.csv") 

    data = []  # Initialize an empty list to store the data
    try:
        with open(csv_file, newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            data = list(reader)  # Load CSV data into a list

            # Adjust table row count based on the data
            table_widget.setRowCount(len(data) - 1)  # -1 for header

            # Populate the table with CSV data
            for row_num, row_data in enumerate(data[1:]):  # Skip the header
                for col_num, col_data in enumerate(row_data):
                    table_widget.setItem(row_num, col_num, QtWidgets.QTableWidgetItem(col_data))

    except Exception as e:
        print(f"Error reading the CSV file: {e}")

    return data  # Return the loaded data

def on_column_selected(table_widget):

    selected_items = table_widget.selectedItems()
    if selected_items:
        selected_column = selected_items[0].column()  # Get the column of the first selected item
        print(f"Selected column: {selected_column}")
        return selected_column
    return None