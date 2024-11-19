class Menu:
    def __init__(self, linked_list):
        self.linked_list = linked_list  # Assign the linked list instance

        #User enters a choice and handle_choice manages the different inputs.
    def handle_choice(self, choice):
        #Choice 1 display_method dispays inventory
        if choice == "1":
            print("\nViewing Inventory...")
            self.linked_list.display_items()
        #Choice 2 add_item method you user adds iems or even a different category to the inventory list.
        elif choice == "2":
            key = input("Enter category (e.g., FD, DR, MSC): ").strip()
            item = input("Enter item name: ").strip()
            self.linked_list.add_item(key, item)
            print(f"Added {item} to the inventory under category {key}.")
        #Choice 3 Removes an item from specific category
        elif choice == "3":
            key = input("Enter category (e.g., FD, DR,MSC): ").strip()
            item = input("Enter the item name to remove: ")
            
            if self.linked_list.remove_item(key,item):
                print(f"Removed {item} from the {key} catgoryof the inventory.")
            else:
                print(f"Item {item} not found in {key} inventory.")
        #Choice 4 allows for any file to integrate with our main inventory.txt file.
        elif choice == "4":
            truckload_file = input("Enter the name of the truckload file: ").strip()
            self.linked_list.load_truckload(truckload_file)
        else:
            print("Invalid choice. Please try again.")
