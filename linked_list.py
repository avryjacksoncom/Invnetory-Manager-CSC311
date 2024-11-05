# linked_list.py

class Node:
    def __init__(self, key, item):
        self.key = key      
        self.item = item     
        self.next = None    

class LinkedList:
    def __init__(self):
        self.head = None    

    def add_item(self, key, item):
        new_node = Node(key, item)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display_items(self):
        if not self.head:
            print("Inventory is empty.")
            return

    # Collect items by category
        category_items = {}
        current = self.head
        while current:
            key = current.key
            item = current.item
            category_items.setdefault(key, []).append(item)
            current = current.next

    # Print items under each category
        for category in sorted(category_items.keys()):
            print(f"\nCategory: {category}")
            for item in category_items[category]:
                print(f" - {item}")

    # Display the items in the linked list
    # def display_items(self):
    #     if not self.head:
    #         print("Inventory is empty.")
    #         return
    #     current = self.head
    #     print("\nCurrent Inventory:")
    #     while current:
    #         print(f"{current.key}-{current.item}")
    #         current = current.next


    # Load items from the inventory file
    def load_inventory(self, filename):
        try:
            with open(filename, 'r') as file:
                for line in file:
                    line = line.strip()
                    if '-' in line:
                        key, item = line.split('-', 1)
                        self.add_item(key, item)
        except FileNotFoundError:
            print(f"File '{filename}' not found. Starting with an empty inventory.")

