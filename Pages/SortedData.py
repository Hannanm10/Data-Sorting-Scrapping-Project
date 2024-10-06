from PyQt5 import QtWidgets
from Algorithms import merge_sort,quick_sort  # Import the merge sort function

def sort_table_by_column(table_widget, column, algo='merge'):
    items = []
    for row in range(table_widget.rowCount()):
        items.append([table_widget.item(row, col).text() for col in range(table_widget.columnCount())])
    
    if algo == 'merge':
        sorted_items = merge_sort(items, column)  # Call your merge sort
    elif algo == 'quick':
        sorted_items = quick_sort(items, column)  # Call your quick sort

    return sorted_items
