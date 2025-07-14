from menu_item import MenuItem
from menu_manager import MenuManager


def show_user_menu():
    print("\n===== Restaurant Menu Manager =====")
    print("[V] View an Item")
    print("[A] Add an Item")
    print("[D] Delete an Item")
    print("[U] Update an Item")
    print("[S] Show the Menu")
    print("[Q] Quit")
    return input("\nChoose an option: ").strip().upper()


def add_item_to_menu():
    name = input("Enter item name: ").strip()
    price = int(input("Enter item price: ").strip())
    item = MenuItem(name, price)
    item.save()
    print("Item was added successfully.")


def remove_item_from_menu():
    name = input("Enter the name of the item to delete: ").strip()
    item = MenuItem(name, 0)
    try:
        item.delete()
        print("Item was deleted successfully.")
    except:
        print("There was an error deleting the item.")


def update_item_from_menu():
    name = input("Enter current item name: ").strip()
    old_item = MenuManager.get_by_name(name)
    if old_item:
        new_name = input("Enter new item name: ").strip()
        new_price = int(input("Enter new price: ").strip())
        old_item.update(new_name, new_price)
        print("Item was updated successfully.")
    else:
        print("Item not found.")


def show_restaurant_menu():
    MenuItem.show_menu()


def main():
    while True:
        choice = show_user_menu()
        if choice == "V":
            name = input("Enter item name to view: ").strip()
            item = MenuManager.get_by_name(name)
            print(item.item_name, item.item_price if item else "Item not found.")
        elif choice == "A":
            add_item_to_menu()
        elif choice == "D":
            remove_item_from_menu()
        elif choice == "U":
            update_item_from_menu()
        elif choice == "S":
            show_restaurant_menu()
        elif choice == "Q":
            print("\nExiting... Here's the final menu:")
            show_restaurant_menu()
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()