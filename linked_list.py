import time
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
            
    def remove_item(self, key, item_name):
        prev = None
        current = self.head
        while current:
            if key == current.key and current.item == item_name:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return True
            prev = current
            current = current.next
        return False
    
    def display_items(self):
        # Start timing
        start_time = time.time()
        
        category_items = {}
        current = self.head
        
        while current:
            key = current.key
            item = current.item
            category_items.setdefault(key, []).append(item)
            current = current.next

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

    def save_inventory(self, filename):
        with open(filename, 'w') as file:
            current = self.head
            
            while current:
                file.write(f"{current.key}-{current.item}\n")
                current = current.next

    def load_truckload(self, truckload_file):
        try:
            
            with open(truckload_file, 'r') as file:
                
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
            print(f"File '{truckload_file}' not found.")
