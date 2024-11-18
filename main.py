from menu import Menu
from linked_list import LinkedList

menuPrompt = """
Please select a menu item below that suits your needs:
1. View Inventory
2. Add Item to Inventory
3. Remove Item from Inventory
4. Load Truckload into Inventory
5. Exit
"""

exitPrompt = "Exiting the program. Thank you for visiting Loker Union Book Store!"


def main():
    # Create an instance of LinkedList    
    linked_list = LinkedList()
    linked_list.load_inventory("inventory.txt")
    menu = Menu(linked_list)  # Pass linked_list to Menu

    while True:
        print(menuPrompt)
        choice = input("\nEnter your choice: ")
        #remove option doesnt work
        if choice == "5":
            print(exitPrompt)
            break
        else:
            menu.handle_choice(choice)

main()
