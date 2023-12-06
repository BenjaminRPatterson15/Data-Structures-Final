import unittest
from WDV169FINAL.MainCode.Classes import PriorityQueue, Location, Item, Node, LinkedList


class TestPriorityQueue(unittest.TestCase):
    def test_enqueue_empty_priority_queue(self):
        # Test case for enqueueing into an empty priority queue
        priority_queue = PriorityQueue()
        item = Item(1, 5, 3)
        location = Location("A", item)

        priority_queue.enqueue(location)

        self.assertEqual(priority_queue.linked_list.head.data, location, "Head should contain the enqueued location.")

    def test_enqueue_multiple_items(self):
        # Test case for enqueueing multiple items into the priority queue
        priority_queue = PriorityQueue()
        item1 = Item(1, 5, 3)
        item2 = Item(2, 3, 1)
        item3 = Item(3, 8, 2)
        location1 = Location("A", item1)
        location2 = Location("B", item2)
        location3 = Location("C", item3)

        priority_queue.enqueue(location1)
        priority_queue.enqueue(location2)
        priority_queue.enqueue(location3)

        self.assertEqual(priority_queue.linked_list.head.data, location1, "Head should contain the first enqueued location.")
        self.assertEqual(priority_queue.linked_list.head.next.data, location2, "Second node should contain the second enqueued location.")
        self.assertEqual(priority_queue.linked_list.head.next.next.data, location3, "Third node should contain the third enqueued location.")


    def test_bubble_sort_empty_list(self):
        # Test case for sorting an empty linked list
        linked_list = LinkedList()
        linked_list.bubble_sort()

        self.assertIsNone(linked_list.head, "Sorting an empty list should not raise an error.")


    def test_bubble_sort_single_element_list(self):
        # Test case for sorting a linked list with a single element
        linked_list = LinkedList()
        item = Item(1, 5, 3)
        location = Location("A", item)
        linked_list.head = Node(location)

        linked_list.bubble_sort()

        self.assertEqual(linked_list.head.data, location, "Sorting a single-element list should not change the order.")

class TestItemAndLocation(unittest.TestCase):
    def test_valid_item_creation(self):
        # Test case for creating a valid Item object
        item = Item(1, 5, 3)
        self.assertEqual(item.itemNum, 1, "ItemNum should be 1.")
        self.assertEqual(item.quantity, 5, "Quantity should be 5.")
        self.assertEqual(item.prio, 3, "Priority should be 3.")

    def test_valid_location_creation(self):
        # Test case for creating a valid Location object
        item = Item(1, 5, 3)
        location = Location("A", item)
        self.assertEqual(location.line, "A", "Line should be 'A'.")
        self.assertEqual(location.item, item, "Item should be the provided item.")

    def test_invalid_item_creation(self):
        # Test case for trying to create an Item with invalid input types
        with self.assertRaises(ValueError):
            invalid_item = Item("invalid", 5, 3)

    def test_invalid_location_creation(self):
        # Test case for trying to create a Location with an invalid line type
        item = Item(1, 5, 3)
        with self.assertRaises(ValueError):
            invalid_location = Location(123, item)



if __name__ == '__main__':
    unittest.main()
