# Node class for a linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked list class with a bubble sort method
class LinkedList:
    def __init__(self):
        self.head = None

    def bubble_sort(self):
        # Check if the linked list is empty
        if self.head is None:
            return

        # Create a copy of the linked list
        sorted_list = LinkedList()
        current = self.head
        while current is not None:
            sorted_list.insert(current.data)
            current = current.next

        # Sort the copied list
        current = sorted_list.head
        while current:
            next_node = current.next
            while next_node:
                # Compare both location and priority, swap if needed
                if (current.data.line > next_node.data.line) or (current.data.line == next_node.data.line and current.data.item.prio > next_node.data.item.prio):
                    current.data, next_node.data = next_node.data, current.data
                next_node = next_node.next
            current = current.next

        # Update the original linked list with the sorted data
        current_original = self.head
        current_sorted = sorted_list.head
        while current_original and current_sorted:
            current_original.data = current_sorted.data
            current_original = current_original.next
            current_sorted = current_sorted.next

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def insert(self, data):
        newNode = Node(data)
        # if the Link List is empty
        if self.head is None:
            self.head = newNode
        # if the data is smaller than the head
        elif self.head.data.line >= newNode.data.line:
            newNode.next = self.head
            self.head = newNode
        else:
            # Locate node before insertion
            current = self.head
            while current.next and newNode.data.line > current.next.data.line:
                current = current.next
            # Insertion
            newNode.next = current.next
            current.next = newNode

# Priority Queue class using a linked list
class PriorityQueue:
    def __init__(self):
        self.linked_list = LinkedList()

    def enqueue(self, location):
        # Add a new node to the end of the linked list
        new_node = Node(location)
        if self.linked_list.head is None:
            self.linked_list.head = new_node
        else:
            current = self.linked_list.head
            while current.next:
                current = current.next
            current.next = new_node

# Item class with input validation
class Item:
    def __init__(self, itemNum, quantity, prio):
        # Validate input types
        if not isinstance(itemNum, int) or not isinstance(quantity, int) or not isinstance(prio, int):
            raise ValueError("ItemNum, Quantity, and Prio must be integers.")

        # Initialize item attributes
        self.itemNum = itemNum
        self.quantity = quantity
        self.prio = prio

    def __str__(self):
        return f'Item: {self.itemNum}, Quantity: {self.quantity}, Priority: {self.prio}'

# Location class
class Location:
    def __init__(self, line, item=None):
        # Validate input type for line
        if not isinstance(line, str):
            raise ValueError("Line must be a string")

        # Initialize location attributes
        self.line = line
        self.item = item

    def __str__(self):
        return f'Location: {self.line}, {self.item}'
