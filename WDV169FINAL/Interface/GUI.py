import traceback

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QTextBrowser, \
    QListWidget, QMessageBox
from WDV169FINAL.MainCode.Classes import Item, Location, PriorityQueue

# Create a GUI class for the Priority Queue
class PriorityQueueGUI(QWidget):
    def __init__(self):
        super().__init__()

        # Initialize the Priority Queue, and a list to store added items
        self.priority_queue = PriorityQueue()
        self.added_items = []

        # Set up the initial GUI
        self.init_ui()

    def init_ui(self):
        # Configure the main window
        self.setWindowTitle('Priority Queue GUI')
        self.setGeometry(300, 300, 400, 400)

        # Create a vertical layout for the widgets
        self.layout = QVBoxLayout()

        # Widgets for input fields (item number, quantity, priority, location)
        self.item_label = QLabel('Item Number:')
        self.item_num_input = QLineEdit()
        self.layout.addWidget(self.item_label)
        self.layout.addWidget(self.item_num_input)

        self.quantity_label = QLabel('Quantity:')
        self.quantity_input = QLineEdit()
        self.layout.addWidget(self.quantity_label)
        self.layout.addWidget(self.quantity_input)

        self.priority_label = QLabel('Priority:')
        self.priority_input = QLineEdit()
        self.layout.addWidget(self.priority_label)
        self.layout.addWidget(self.priority_input)

        self.location_label = QLabel('Location:')
        self.location_input = QLineEdit()
        self.layout.addWidget(self.location_label)
        self.layout.addWidget(self.location_input)

        # Button to add an item to the Priority Queue
        self.add_button = QPushButton('Add Item to the Queue')
        self.add_button.clicked.connect(self.add_item_to_queue)
        self.layout.addWidget(self.add_button)

        # Button to sort the Priority Queue
        self.sort_button = QPushButton('Sort Priority Queue')
        self.sort_button.clicked.connect(self.sort_queue)
        self.layout.addWidget(self.sort_button)

        # Widgets to display the sorted Priority Queue and the added items
        self.result_label = QLabel('Sorted Queue:')
        self.layout.addWidget(self.result_label)

        self.result_text = QTextBrowser()
        self.layout.addWidget(self.result_text)

        self.added_items_label = QLabel('Added Items:')
        self.layout.addWidget(self.added_items_label)

        self.added_items_list = QListWidget()
        self.layout.addWidget(self.added_items_list)

        # Button to remove the selected item from the added items list
        self.remove_item_button = QPushButton('Remove Selected Item')
        self.remove_item_button.clicked.connect(self.remove_selected_item)
        self.layout.addWidget(self.remove_item_button)

        # Set the layout for the main window
        self.setLayout(self.layout)

    def remove_selected_item(self):
        # Remove the selected item from both the Priority Queue and the added items list
        selected_item_index = self.added_items_list.currentRow()
        if selected_item_index != -1:
            selected_item = self.added_items[selected_item_index]

            # Remove from Priority Queue if present
            try:
                self.priority_queue.linked_list.remove(selected_item)
            except Exception as e:
                pass  # Handle the exception if needed

            # Remove from added items list
            del self.added_items[selected_item_index]

            # Update the GUI
            self.update_added_items_list()

    def add_item_to_queue(self):
        try:
            # Add an item to the Priority Queue and the added items list
            item_num = int(self.item_num_input.text())
            quantity = int(self.quantity_input.text())
            priority = int(self.priority_input.text())
            location_name = self.location_input.text()

            item = Item(item_num, quantity, priority)
            location = Location(location_name, item)
            self.priority_queue.enqueue(location)
            self.added_items.append(item)

            # Clear input fields
            self.item_num_input.clear()
            self.quantity_input.clear()
            self.priority_input.clear()
            self.location_input.clear()

            # Update the added items list in the GUI
            self.update_added_items_list()

        except ValueError:
            # Handle the case where the input cannot be converted to integers
            # For example, if the user enters non-numeric values for quantity or priority
            QMessageBox.warning(self, 'Input Error', 'Please enter valid numeric values for Quantity and Priority.')
        except Exception as e:
            # Catch any other exceptions and print the traceback
            QMessageBox.warning(self, 'Error', 'An error occurred. Please check the console for details.')
            print(traceback.format_exc())



    def sort_queue(self):
        try:
            self.priority_queue.linked_list.bubble_sort()
            self.update_sorted_result()
        except Exception as e:
            print(f"Error sorting the queue: {e}")

    def update_sorted_result(self):
        # Update the result text widget with the sorted Priority Queue
        self.result_text.clear()
        for node in self.priority_queue.linked_list:
            self.result_text.append(str(node.data))

    def update_added_items_list(self):
        # Update the added items list widget in the GUI
        self.added_items_list.clear()
        for item in self.added_items:
            self.added_items_list.addItem(str(item))
