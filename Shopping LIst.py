shopping_list = []

def display_menu():
        print("\nShopping List Menu: ")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. View Shopping List")
        print("4. Exit")
    
while True:
    display_menu()
    choice = input("Choose an option (1-4): ")

    if choice == "1":
          item = input("Enter an item to add: ")
          shopping_list.append(item)
          print(f"'{item}' added to the list.")

    elif choice == '2':
        item = input("Enter an item to remove: ")
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"{item} was removed from the list" )
        else:
            print("Item not found in the list.")

    elif choice == "3":
        if shopping_list:
            print("\nShopping List: "," | ".join(shopping_list))
        else: 
            print("No item in the list")

    elif choice == '4':
        print("Existing Program. Goodbye")
        break    

    else:
        print("Invalid Choice. Please select a valid option.")
                     