def displayMenu():
    print("Shopping List Manager")
    print("1. Add item")
    print("2. Remove item")
    print("3. View list")
    print("4. Exit")
def main():
    shopping_list = []
    while True:
        displayMenu()
        choice = input("Enter your choice: ")
        if choice == '1':
            item = input("Enter item to add: ")
            shopping_list.append(item)
        elif choice == '2':
            item = input("Enter item to remove: ")
            shopping_list.remove(item)
        elif choice == '3':
            print("Shopping List:", shopping_list)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()
            