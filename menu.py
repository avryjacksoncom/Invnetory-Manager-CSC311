class Menu:
    def __init__(self, linked_list):
        self.linked_list = linked_list  # Assign the linked list instance

    def handle_choice(self, choice):
        if choice == "1":
            print("\nViewing Inventory...")
            self.linked_list.display_items()
        elif choice == "2":
            key = input("Enter category (e.g., FD, DR): ").strip()
            item = input("Enter item name: ").strip()
            self.linked_list.add_item(key, item)
            print(f"Added {item} to the inventory under category {key}.")
        elif choice == "3":
            item = input("Enter the item name to remove: ")
            if self.linked_list.remove_item(item):
                print(f"Removed {item} from the inventory.")
            else:
                print(f"Item {item} not found in inventory.")
        elif choice == "4":
            truckload_file = input("Enter the name of the truckload file: ").strip()
            self.linked_list.load_truckload(truckload_file)
        else:
            print("Invalid choice. Please try again.")
