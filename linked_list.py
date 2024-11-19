import time

# Node class represents each individual element in the linked list
class Node:
    def __init__(self, key, item):
        self.key = key      # The category of the item
        self.item = item     # The actual item name
        self.next = None    # Pointer to the next node in the linked list

# LinkedList class to manage the inventory of items categorized by key
class LinkedList:
    def __init__(self):
        self.head = None    # Initialize the linked list with no items

    # Adds a new item to the linked list
    def add_item(self, key, item):
        new_node = Node(key, item)  # Create a new Node with the given key and item

        # If the list is empty, the new node becomes the head of the list
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            # Traverse the list to find the last node and append the new node
            while current.next:
                current = current.next
            current.next = new_node

    # Removes an item from the inventory by its key and item name
    def remove_item(self, key, item_name):
        prev = None      # To keep track of the previous node
        current = self.head        # Start from the head of the list
        while current:
            # Check if the current node matches the key and item name
            if key == current.key and current.item == item_name:
                # If it's the first node (head), update the head pointer
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return True      # Item removed successfully
            prev = current         # Move prev to the current node
            current = current.next  # Move to the next node
        return False         # If no matching item was found, return False

    # Displays all items in the inventory categorized by their key
    def display_items(self):
        # Start timing
        start_time = time.time()
        
        category_items = {} # Dictionary to hold categories
        current = self.head # Start at the head of the list

        # Traverse the linked list to categorize the items
        while current:
            key = current.key
            item = current.item
            # Add the item to the list of its corresponding category in the dictionary
            category_items.setdefault(key, []).append(item)
            current = current.next

        # Print the categorized items in sorted order of categories
        for category in sorted(category_items.keys()):
            print(f"\nCategory: {category}")
            for item in category_items[category]:
                print(f" - {item}")
        
        # End timing
        end_time = time.time()
        execution_time_ms = (end_time - start_time) * 1000
        print()
        print("Display method time:")
        print(f"Execution time: {execution_time_ms:.2f} ms")

    # Loads inventory items from a file and adds them to the linked list
    def load_inventory(self, filename):
        try:
            #open the file
            with open(filename, 'r') as file:

                # Read each line from the file
                for line in file:
                    line = line.strip()
                    
                    if '-' in line:
                        key, item = line.split('-', 1)
                        self.add_item(key, item)
                        
        except FileNotFoundError:
            print(f"File '{filename}' not found. Starting with an empty inventory.") # Error if file is not found

    # Saves the current inventory (linked list)
    def save_inventory(self, filename):
        with open(filename, 'w') as file:
            current = self.head
            
            while current:
                file.write(f"{current.key}-{current.item}\n")
                current = current.next

    # Loads a truckload of inventory items from a file and updates the inventory
    def load_truckload(self, truckload_file):
        try:
            # Open the truckload file in read mode
            with open(truckload_file, 'r') as file:

                  # Read each line from the truckload
                for line in file:
                    line = line.strip()
                    
                    if '-' in line:
                        key, item = line.split('-', 1)
                        self.add_item(key, item)    
            print(f"Truckload from '{truckload_file}' has been added to the inventory.")
            
            # Overwrite the inventory file with truck inventory
            self.save_inventory("inventory.txt")
            
            print("The inventory has been updated and saved to 'inventory.txt'.")
            
        except FileNotFoundError:
            print(f"File '{truckload_file}' not found.")  # Error if truckload file is not found
