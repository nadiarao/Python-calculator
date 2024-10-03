# Define a dictionary to hold events and their corresponding items
event_items = {}

def add_event(event_name):
    '''Add a new event to the dictionary.'''
    if event_name not in event_items:
        event_items[event_name] = []
        print(f"Event '{event_name}' added.")
    else:
        print(f"Event '{event_name}' already exists.")

def add_item_to_event(event_name, item):
    '''Add an item to the specified event.'''            
    if event_name in event_items:
        event_items[event_name].append(item)
        print(f"Item '{item}' added to event '{event_name}'.")
    else:
        print(f"Event '{event_name}' does not exist.")

def display_items_for_event(event_name):
    '''Display items associated with a specific event.'''            
    if event_name in event_items:
        items = event_items[event_name]
        print(f"Items for '{event_name}' : {'.'.join(items) if items else 'No items added.'}")
    else:
        print(f"Event '{event_name}' does not exist.")

def main():
    while True:
        print("n\Options:")
        print("1. Add Event ")
        print("2. Add item to event")
        print("3. Display Item for Event")
        print("4. Exit")
        choice = input("Select an option (1-4): ")

        if choice == '1':
            event_name = input("Enter the event name: ") 
            add_event(event_name)
        elif choice =='2':
            event_name = input("Enter the event name: ")
            item = input("Enter the item name: ")
            add_item_to_event(event_name, item)
        elif choice =='3':
            event_name = input("Enter the event name: ") 
            display_items_for_event(event_name)
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()            
