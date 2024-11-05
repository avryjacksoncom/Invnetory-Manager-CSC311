# main.py

from menu import Menu
from linked_list import LinkedList

def main():
    # Create an instance of LinkedList    
    linked_list = LinkedList()
    linked_list.load_inventory("inventory.txt")
    menu = Menu(linked_list)  # Pass linked_list to Menu

    while True:
        print("\nPlease select a menu item below that suits your needs:")
        print("1. View Inventory")
        print("2. Add Item to Inventory")
        print("3. Remove Item from Inventory")
        print("4. Exit")

        choice = input("\nEnter your choice: ")
        if choice == "4":
            linked_list.save_inventory("inventory.txt")
            print("Exiting the program. Thank you for visiting Loker Union Book Store!")
            break
        else:
            menu.handle_choice(choice)

main()
