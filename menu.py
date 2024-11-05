# menu.py

class Menu:
    def __init__(self, linked_list):
        self.linked_list = linked_list  # Assign the linked list instance

    def handle_choice(self, choice):
        if choice == "1":
            print("\nViewing Inventory...")
            self.linked_list.display_items()
        elif choice == "2":
            
            print(f"Added to the inventory.")
        elif choice == "3":
            item = input("Enter the item name to remove: ")
        else:
            print("Invalid choice. Please try again.")
