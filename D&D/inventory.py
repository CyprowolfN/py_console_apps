import json
import os
# The dictionary that holds onto our items
inventory = {}

# debug_path = "./D&D/inventory.json"
file_path = "./D&D/inventory.json"
json_size = os.path.getsize(file_path)
    
def add_item(item, quantity):
    # Load in the JSON
    with open(file_path, 'r') as file:
        existing_data = json.load(file)

        if quantity < 0:
            print("negitive values are not allowed!")
            quit()
        if item in existing_data:
            existing_data[item] += quantity
            inventory.update(existing_data)
            with open(file_path, 'w') as file:
                json.dump(inventory, file, indent=2)
                print(f'Added -> {quantity} {item} to inventory: {file_path}')
                print(f'Total {item}\'s in inventory {existing_data[item]}: {file_path}')

        else:
            existing_data[item] = quantity
            inventory.update(existing_data)
            print(inventory)
            with open(file_path, 'w') as file:
                json.dump(inventory, file, indent=2)
                print(f'(New item) {quantity} {item} has been added to inventory: {file_path}')


def remove_item(item, quantity):
    with open(file_path, 'r') as file:
    # Load data into existing_data from inventory.json
        existing_data = json.load(file)
        found = False

    # Loop over the keys in the existing_data
    for key in existing_data:
        if item == key:
            found = True
            print(f"{item} is equal to {key}")

            # modifying the quantity ( incase users decide to use negitive values )
            if quantity < 0:
                print("negitive values are not allowed!")
                quit()
            if existing_data[key] >= quantity:
                existing_data[key] -= quantity
                # Update the inventory with JSON changes
                inventory.update(existing_data)
                # If the quantity is equal to zero, remove it from the inventory
                if existing_data[key] == 0:
                    del inventory[key]
                    with open(file_path, 'w') as file:
                        json.dump(inventory, file, indent=2)
                        print(f"{quantity} {item} was removed from inventory")
                        print(f"You have no more {item}\'s in your inventory")
                else:
                    with open(file_path, 'w') as file:
                        json.dump(inventory, file, indent=2)
                        print(f"{quantity} {item} was removed from inventory")
                        print(f'Total {item}\'s in inventory {existing_data[item]}: {file_path}')
            else:
                print(f"Not enough {item}\'s in inventory to remove.")
                print(f'Total {item}\'s in inventory {existing_data[item]}: {file_path}')
            break
    
    if not found:
        print(f"{item} not found in inventory.")

def list_items():
    print("Inventory:")
    print('')
    with open(file_path, 'r') as file:
        if json_size > 2:
            existing_data = json.load(file)
            for key, value in existing_data.items():
                print(f"{key}: {value}")
        else:
            print("Your inventory is Empty!")


while True:
    print("\033[92m")
    print('v0.05A')
    command = input("Enter a command (add/remove/list/exit)\033[94m: ")
    # Add new items into the inventory
    if command == "add":
        item = input(str("Enter item name: ")).upper()
        quantity = int(input("Enter quantity: "))
        add_item(item, quantity)

    # Remove items from the inventory
    elif command == "remove":
        item = input(str("Enter item name: ")).upper()
        quantity = int(input("Enter quantity: "))
        remove_item(item, quantity)
    
    # List items from the inventory
    elif command == "list":
        list_items()
    
    # Exit the program
    elif command == "exit":
        break
    else:
        print("Invalid command.")
