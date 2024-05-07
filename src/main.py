import csv, random, os, re
from filter import FoodTypeFilter, PriceRangeFilter # Importing the filter classes

food_types = ["Steakhouse", "Italian", "Japanese", "Cafe", "Vegetarian", "Mexican", "Chinese", "Other"]
price_ranges = ["Cheap", "Mid-range", "Expensive"]

def read_and_display_restaurants(filename):
    print("Restaurants in the selected list:")
    try:
        with open(filename + '.csv', 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
            for index, row in enumerate(reader, start=1):
                print(f"{index}. {', '.join(row)}")
    except FileNotFoundError:
        print("File not found. Please make sure the file exists.")

# Function to print welcome message
def display_welcome_message():
    print("\nWelcome to the Random Restaurant Generator!")
    print("This tool will help you find a restaurant based on your preferences.")
    print("Let's get started!")

# Call the function to display the welcome message
display_welcome_message()

# Function to display the menu options
def display_menu():
    print("\nMenu:")
    print("1. Create a new restaurant list")
    print("2. Select a restaurant to roll")
    print("3. Edit restaurant list")
    print("4. Remove restaurant list")
    print("5. Exit Program")

# Function to adjust filename to lowercase and replace spaces with hyphens
def adjust_filename(filename):
    filename = filename.lower()  # Convert to lowercase
    filename = filename.replace(" ", "-")  # Replace spaces with hyphens
    return filename

# Function to check if the input contains only allowed characters
def is_valid_input(input_string):
    # Regular expression to match only alphanumeric characters and hyphen
    pattern = r'^[a-zA-Z0-9\-]+$'
    return bool(re.match(pattern, input_string))

# Function to create a new list
def create_new_list():
    print("\nCreating a new list...")
    while True:
        # Ask the user for the name of the new list
        list_name = input("\nEnter the name of the new restaurant list: ")
        
        # Check if the input contains only allowed characters
        if not is_valid_input(list_name):
            print("\nError: List name can only contain alphanumeric characters and hyphens (-). Please try again.")
            continue
        
        # Adjust filename
        list_name = adjust_filename(list_name)

        # Open a new CSV file with the adjusted list name
        with open(f"{list_name}.csv", mode='w', newline='', encoding="utf-8") as file:
            writer = csv.writer(file)

            # Write the header row
            writer.writerow(["Restaurant Name", "Type of Food", "Price"])
            

        while True:
            # Ask the user for restaurant name
            restaurant_name = input("Enter the restaurant name that you would like to add: ")

            while True:
                # Ask the user to choose the type of food
                print("\nChoose the type of food:")
                print("1. Steakhouse")
                print("2. Italian")
                print("3. Japanese")
                print("4. Cafe")
                print("5. Vegetarian")
                print("6. Mexican")
                print("7. Chinese")
                print("8. Other")
                food_choice = input("Enter your choice: ")

                if food_choice in ['1', '2', '3', '4', '5', '6', '7', '8']:
                    food_type = food_types[int(food_choice) - 1]
                    break
                else:
                    print("\nInvalid choice. Please choose a number between 1 and 8.")
                    
            while True:
                # Ask the user to choose the price range
                print("\nChoose the price range:")
                print("1. Cheap")
                print("2. Mid-range")
                print("3. Expensive")
                price_choice = input("Enter your choice: ")

                if price_choice in ['1', '2', '3']:
                    price_range = price_ranges[int(price_choice) - 1]
                    break
                else:
                    print("\nInvalid choice. Please choose a number between 1 and 3.")

            with open(f"{list_name}.csv", mode='a', newline='', encoding="utf-8") as file:
                writer = csv.writer(file)
                
                # Write the restaurant details to the CSV file
                writer.writerow([restaurant_name, food_type, price_range])

            read_and_display_restaurants(list_name)

            # Ask the user for next action
            print("\nNext Steps:")
            print("1. Enter another restaurant")
            print("2. Save and back to menu")
            print("3. Exit program")
            next_action = input("Enter your choice: ")

            if next_action == '1':
                continue
            elif next_action == '2':
                print("\nList saved successfully!")
                return True  # Signal to return to the menu options
            elif next_action == '3':
                print("\nList saved successfully! Exiting the program.")
                return False  # Signal to exit the program
            else:
                print("\nInvalid choice. Please choose from options 1-3.")
                continue


# Function to select a list
def select_list():
    print("\nSelecting a list...")
    # Get a list of all CSV files in the current directory
    csv_files = [file[:-4] for file in os.listdir() if file.endswith('.csv')]
    
    if not csv_files:
        print("No lists found. Please create a list first.")
        return
    
    # Display the available lists
    print("\nRestaurant lists:")
    for index, file in enumerate(csv_files, start=1):
        print(f"{index}. {file}")  # Remove the file extension (.csv)
    
    # Ask the user to select a list
    while True:
        choice = input("Enter the number of the list you want to select (1-{}): ".format(len(csv_files)))
        
        if choice.isdigit():
            index = int(choice) - 1
            if 0 <= index < len(csv_files):
                selected_list = csv_files[index]
                print(f"You have selected: {selected_list}")

                # Get user's choices for food type and price range
                while True:
                    print("\nChoose the type of food:")
                    for index, food_type in enumerate(food_types, start=1):
                        print(f"{index}. {food_type}")
                    print("9. No idea")  # Add 'No idea' option
                    food_type_choice = input("Enter your choice (1-9): ")

                    if food_type_choice in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                        if food_type_choice == '9':
                            selected_food_type = "No idea"
                        else:
                            selected_food_type = food_types[int(food_type_choice) - 1]
                        break
                    else:
                        print("Invalid choice. Please choose a number between 1 and 9.")

                while True:
                    print("\nChoose the price range:")
                    for index, price_range in enumerate(price_ranges, start=1):
                        print(f"{index}. {price_range}")
                    print("4. Any price")  # Add 'Any price' option
                    price_range_choice = input("Enter your choice (1-4): ")

                    if price_range_choice in ['1', '2', '3', '4']:
                        if price_range_choice == '4':
                            selected_price_range_choice = "Any price"
                        else:
                            selected_price_range_choice = price_ranges[int(price_range_choice) - 1]
                        break
                    else:
                        print("Invalid choice. Please choose a number between 1 and 4.")

                while True:
                    # Filter restaurant options based on user's choices
                    options = filter_restaurant_options(selected_list, selected_food_type, selected_price_range_choice)

                    if options:
                        # Perform a random roll and select a restaurant
                        selected_restaurant = random.choice(options)
                        print(f"\nLet's go for {selected_restaurant[0]}")
                        
                        # Offer options after rolling the result
                        print("\nNext Steps:")
                        print("1. Done and exit program")
                        print("2. Roll it again")
                        print("3. Back to menu")
                        
                        while True:
                            option_choice = input("Enter your choice (1-3): ")
                            if option_choice == '1':
                                print("Exiting the program. Goodbye!")
                                exit()  # Exit the program
                            elif option_choice == '2':
                                break  # Break to continue to the next iteration of the loop to re-roll
                            elif option_choice == '3':
                                return  # Return to the menu options
                            else:
                                print("Invalid choice. Please enter a number between 1 and 3.")
                    else:
                        print("No restaurants match your criteria. Please try again.")
                        break
            else:
                print("Invalid choice. Please enter a number between 1 and {}.".format(len(csv_files)))
        else:
            print("Invalid input. Please enter a number.")

def filter_restaurant_options(list_name, food_type, price_range):
    # Open the CSV file
    with open(f"{list_name}.csv", mode="r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row

        # Filter restaurant options based on user's choices
        filtered_options = []

        for row in reader:
            if len(row) >= 3:  # Check if the row contains at least three values
                restaurant_name = row
                food_filter = FoodTypeFilter(food_type)
                price_filter = PriceRangeFilter(price_range)

                # Include all restaurants if "No idea" is selected for food type
                if food_type.lower() == "no idea":
                    # Apply price range filter if "Any price" is not selected
                    if price_range.lower() != "any price":
                        if price_filter.filter(row):
                            filtered_options.append(restaurant_name)
                    else:
                        filtered_options.append(restaurant_name)
                else:
                    # Apply food type filter
                    if food_filter.filter(row):
                        # Apply price range filter if "Any price" is not selected
                        if price_range.lower() != "any price":
                            if price_filter.filter(row):
                                filtered_options.append(restaurant_name)
                        else:
                            filtered_options.append(restaurant_name)

        return filtered_options

def edit_list():
    print("\nEditing list...")

    # Get a list of all CSV files in the current directory
    csv_files = [file[:-4] for file in os.listdir() if file.endswith('.csv')]

    if not csv_files:
        print("No lists found. Please create a list first.")
        return

    while True:
        # Display the available lists
        print("\nRestaurant lists:")
        for index, file in enumerate(csv_files, start=1):
            print(f"{index}. {file}")  # Remove the file extension (.csv)

        # Ask the user to select a list to edit
        choice = input("Enter the number of the list you want to edit (1-{}), or 0 to go back: ".format(len(csv_files)))

        if choice == '0':
            return

        if choice.isdigit():
            index = int(choice) - 1
            if 0 <= index < len(csv_files):
                selected_list = csv_files[index]
                print(f"\nHere is your list: {selected_list}")

                # Print the contents of the selected CSV list
                print("\nRestaurants:")
                with open(f"{selected_list}.csv", mode="r", newline="") as file:
                    reader = csv.reader(file)
                    next(reader)  # Skip the header row
                    restaurants = list(reader)
                    for i, row in enumerate(restaurants, start=1):
                        print(f"{i}. {', '.join(row)}")

                while True:
                    print("\nOptions:")
                    print("1. Add another restaurant")
                    print("2. Remove a restaurant")
                    print("3. Back to menu")
                    option = input("Enter your choice (1-3): ")

                    if option == '1':

                        # Retrieve the latest list of restaurants
                        with open(f"{selected_list}.csv", mode="r", newline="", encoding="utf-8") as file:
                            reader = csv.reader(file)
                            next(reader)  # Skip the header row
                            restaurants = list(reader)

                        # Add another restaurant
                        while True:
                            restaurant_name = input("Enter the restaurant name: ")
                            print("\nChoose the type of food:")
                            for index, food_type in enumerate(food_types, start=1):
                                print(f"{index}. {food_type}")
                            food_type_choice = input("Enter your choice (1-8): ")

                            if food_type_choice.isdigit() and 1 <= int(food_type_choice) <= 8:
                                food_type = food_types[int(food_type_choice) - 1]
                            else:
                                print("\nInvalid food type choice. Please choose a number between 1 and 8.")
                                continue

                            print("\nChoose the price range:")
                            for index, price_range in enumerate(price_ranges, start=1):
                                print(f"{index}. {price_range}")
                            price_range_choice = input("Enter your choice (1-3): ")

                            if price_range_choice.isdigit() and 1 <= int(price_range_choice) <= 3:
                                price_range = price_ranges[int(price_range_choice) - 1]

                                # Append the new restaurant to the CSV file
                                with open(f"{selected_list}.csv", mode="a", newline="", encoding="utf-8") as file:
                                    writer = csv.writer(file)
                                    writer.writerow([restaurant_name, food_type, price_range])
                                print("\nRestaurant added successfully!")

                                # Print the updated list
                                print("\nHere is your new list:")
                                with open(f"{selected_list}.csv", mode="r", newline="", encoding="utf-8") as file:
                                    reader = csv.reader(file)
                                    next(reader)  # Skip the header row
                                    for i, row in enumerate(reader, start=1):
                                        print(f"{i}. {', '.join(row)}")
                                break  # Exit the loop after adding the restaurant
                            else:
                                print("Invalid price range choice. Please choose a number between 1 and 3.")

                    elif option == '2':
                        # Remove a restaurant
                        print("\nRemoving a restaurant...")

                        # Print the list again
                        print(f"\nHere is your list: {selected_list}")

                        # Print the contents of the selected CSV list
                        print("\nRestaurants:")
                        with open(f"{selected_list}.csv", mode="r", newline="", encoding="utf-8") as file:
                            reader = csv.reader(file)
                            next(reader)  # Skip the header row
                            restaurants = list(reader)
                            for i, row in enumerate(restaurants, start=1):
                                print(f"{i}. {', '.join(row)}")

                        # Ask for the number of the restaurant to remove
                        while True:
                            remove_choice = input("\nEnter the number of the restaurant you want to remove: ")
                            if remove_choice.isdigit() and 1 <= int(remove_choice) <= len(restaurants):
                                remove_index = int(remove_choice) - 1
                                break
                            else:
                                print("\nInvalid choice. Please enter a valid number.")

                        # Remove the selected restaurant
                        del restaurants[remove_index]

                        # Update the CSV file
                        with open(f"{selected_list}.csv", mode='w', newline='') as file:
                            writer = csv.writer(file)
                            writer.writerow(["Restaurant Name", "Type of Food", "Price"])  # Rewrite the header
                            writer.writerows(restaurants)

                        # Print updated list
                        print("\nRestaurant removed successfully!\n")
                        print("Here is your new list:")
                        for i, row in enumerate(restaurants, start=1):
                            print(f"{i}. {', '.join(row)}")

                    elif option == '3':
                        # Save
                        return

                    else:
                        print("\nInvalid option. Please choose a number between 1 and 3.")
            else:
                print("\nInvalid choice. Please enter a number between 1 and {}.".format(len(csv_files)))
        else:
            print("\nInvalid input. Please enter a number.")

def remove_list():
    print("\nRemoving a list...")
    
    # Get a list of all CSV files in the current directory
    csv_files = [file[:-4] for file in os.listdir() if file.endswith('.csv')]
    
    if not csv_files:
        print("No lists found.")
        return
    
    while True:
        # Display the available lists with numbers
        print("\nRestaurant lists:")
        for index, file in enumerate(csv_files, start=1):
            print(f"{index}. {file}")

        # Ask the user to select a list to remove
        choice = input("Enter the number of the list you want to remove (1-{}), or enter 0 to exit: ".format(len(csv_files)))
        
        if choice == '0':
            return

        if choice.isdigit():
            index = int(choice) - 1
            if 0 <= index < len(csv_files):
                selected_list = csv_files[index]
                print(f"\nAre you sure to remove your list: {selected_list}?")

                # Ask for confirmation
                confirmation = input("Enter 'yes' to confirm or 'no' to cancel: ").lower()
                if confirmation == 'yes':
                    # Remove the CSV file
                    os.remove(f"{selected_list}.csv")
                    print(f"\nYour list: {selected_list} has been removed.")
                    return
                elif confirmation == 'no':
                    print("Please select another list to remove or enter 0 to exit.")
                else:
                    print("Invalid input. Please enter 'yes' or 'no'.")
            else:
                print("Invalid choice. Please enter a number between 1 and {}.".format(len(csv_files)))
        else:
            print("Invalid input. Please enter a number.")

# Main function to run the program
def main():
    while True:
        display_menu()
        choice = input("Please enter the number of your choice (1-5): ")

        if choice == '1':
            should_return_to_menu = create_new_list()
            if not should_return_to_menu:
                print("\nExiting the program. Goodbye!")
                break
        elif choice == '2':
            select_list()
        elif choice == '3':
            edit_list()
        elif choice == '4':
            remove_list()
        elif choice == '5':
            print("\nExiting the program. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please enter a number between 1 and 5.")

# Run the main function
if __name__ == "__main__":
    main()
