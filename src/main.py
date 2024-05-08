import csv
import random
import os
from constant import FOOD_TYPES, PRICE_RANGES, LIST_HEADER, CSV_LIST_NOT_FOUND_MESSAGE
from utilise import read_and_display_restaurants, display_welcome_message, display_menu, get_csv_files, display_restaurant_list_options, filter_restaurant_options
from validator import sanitise_filename, is_valid_input, invalid_input_message

# Call the function to display the welcome message
display_welcome_message()

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
        list_name = sanitise_filename(list_name)

        # Open a new CSV file with write mode   
        with open(f"{list_name}.csv", mode='w', newline='', encoding="utf-8") as file:
            writer = csv.writer(file)

            # Write the header row
            writer.writerow(LIST_HEADER)
            
        while True:
            # Ask the user for restaurant name
            restaurant_name = input("\nEnter the restaurant name that you would like to add: ")

            while True:
                # Ask the user to choose the type of food
                print("\nChoose the type of food:")

                # Print the food type options
                for index, food_type in enumerate(FOOD_TYPES, start=1):
                    print(f"{index}. {food_type}")

                food_type_choice = input("Enter your choice: ")

                # Check if the choice is valid and within range
                if food_type_choice.isdigit() and 1 <= int(food_type_choice) <= len(FOOD_TYPES):
                    food_type = FOOD_TYPES[int(food_type_choice) - 1]
                    break
                else:
                    invalid_input_message(len(FOOD_TYPES))
                    
            while True:
                # Ask the user to choose the price range
                print("\nChoose the price range:")

                # Print the price range options
                for index, food_type in enumerate(PRICE_RANGES, start=1):
                    print(f"{index}. {food_type}")

                price_choice = input("Enter your choice: ")

                # Check if the choice is valid and within range
                if price_choice.isdigit() and 1 <= int(price_choice) <= len(PRICE_RANGES):
                    price_range = PRICE_RANGES[int(price_choice) - 1]
                    break
                else:
                    invalid_input_message(len(PRICE_RANGES))

            with open(f"{list_name}.csv", mode='a', newline='', encoding="utf-8") as file:
                writer = csv.writer(file)
                
                # Write the restaurant details to the CSV file
                writer.writerow([restaurant_name, food_type, price_range])

            read_and_display_restaurants(list_name)

            while True:
                # Ask the user for next action
                print("\nNext Steps:")
                print("1. Add another restaurant")
                print("2. Save and back to menu")
                print("3. Exit program")
                next_action = input("Enter your choice: ")

                if next_action == '1':
                    break
                elif next_action == '2':
                    print("\nList saved successfully!")
                    return True  # Signal to return to the menu options
                elif next_action == '3':
                    print("\nList saved successfully! Exiting the program.")
                    exit()  # Exit the program
                else:
                    invalid_input_message(3)
                    continue

# Function to select a list
def select_list():
    print("\nSelecting a list...")
    # Get a list of all CSV files in the current directory
    csv_files = get_csv_files()
    
    if not csv_files:
        print(CSV_LIST_NOT_FOUND_MESSAGE)
        return
    
    # Ask the user to select a list
    while True:
        # Display the available lists
        display_restaurant_list_options(csv_files)
        choice = input("\nEnter the number of the list you want to select (1-{}): ".format(len(csv_files)))
        
        if choice.isdigit():
            index = int(choice) - 1
            if 0 <= index < len(csv_files):
                selected_list = csv_files[index]
                print(f"You have selected: {selected_list}")

                # Get user's choices for food type and price range
                while True:
                    print("\nChoose the type of food:")
                    for index, food_type in enumerate(FOOD_TYPES, start=1):
                        print(f"{index}. {food_type}")
                    print("9. No idea")  # Add 'No idea' option
                    food_type_choice = input("Enter your choice (1-9): ")

                    if food_type_choice.isdigit() and 1 <= int(food_type_choice) <= len(FOOD_TYPES) + 1:
                        if food_type_choice == '9':
                            selected_food_type = "No idea"
                        else:
                            selected_food_type = FOOD_TYPES[int(food_type_choice) - 1]
                        break
                    else:
                        invalid_input_message(9)

                while True:
                    print("\nChoose the price range:")
                    for index, price_range in enumerate(PRICE_RANGES, start=1):
                        print(f"{index}. {price_range}")
                    print("4. Any price")  # Add 'Any price' option
                    price_range_choice = input("Enter your choice (1-4): ")

                    if price_range_choice.isdigit() and 1 <= int(price_range_choice) <= len(PRICE_RANGES) + 1:
                        if price_range_choice == '4':
                            selected_price_range = "Any price"
                        else:
                            selected_price_range = PRICE_RANGES[int(price_range_choice) - 1]
                        break
                    else:
                        invalid_input_message(4)

                while True:
                    # Filter restaurant optkions based on user's choices
                    options = filter_restaurant_options(selected_list, selected_food_type, selected_price_range)

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
                                invalid_input_message(3)
                    else:
                        print("\nNo restaurants match your criteria. Please try again.")
                        break
            else:
                invalid_input_message(len(csv_files))
        else:
            invalid_input_message()

def edit_list():
    print("\nEditing list...")

    # Get a list of all CSV files in the current directory
    csv_files = get_csv_files()

    if not csv_files:
        print(CSV_LIST_NOT_FOUND_MESSAGE)
        return

    while True:
        # Display the available lists
        display_restaurant_list_options(csv_files)  # Remove the file extension (.csv)

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
                read_and_display_restaurants(selected_list)

                while True:
                    print("\nOptions:")
                    print("1. Add another restaurant")
                    print("2. Remove a restaurant")
                    print("3. Back to menu")
                    option = input("Enter your choice (1-3): ")

                    # Retrieve the latest list of restaurants
                    with open(f"{selected_list}.csv", mode="r", newline="", encoding="utf-8") as file:
                        reader = csv.reader(file)
                        next(reader)  # Skip the header row
                        restaurants = list(reader)

                    if option == '1':

                        # Add another restaurant
                        while True:
                            restaurant_name = input("Enter the restaurant name: ")
                            print("\nChoose the type of food:")
                            for index, food_type in enumerate(FOOD_TYPES, start=1):
                                print(f"{index}. {food_type}")
                            food_type_choice = input("Enter your choice (1-{}): ".format(len(FOOD_TYPES)))

                            if food_type_choice.isdigit() and 1 <= int(food_type_choice) <= len(FOOD_TYPES):
                                food_type = FOOD_TYPES[int(food_type_choice) - 1]
                            else:
                                invalid_input_message(8)
                                continue

                            print("\nChoose the price range:")
                            for index, price_range in enumerate(PRICE_RANGES, start=1):
                                print(f"{index}. {price_range}")
                            price_range_choice = input("Enter your choice (1-{}): ".format(len(PRICE_RANGES)))

                            if price_range_choice.isdigit() and 1 <= int(price_range_choice) <= len(PRICE_RANGES):
                                price_range = PRICE_RANGES[int(price_range_choice) - 1]

                                # Append the new restaurant to the CSV file
                                with open(f"{selected_list}.csv", mode="a", newline="", encoding="utf-8") as file:
                                    writer = csv.writer(file)
                                    writer.writerow([restaurant_name, food_type, price_range])

                                print("\nRestaurant added successfully!")

                                # Print the updated list
                                read_and_display_restaurants(selected_list)
                                break  # Exit the loop after adding the restaurant
                            else:
                                invalid_input_message(3)

                    elif option == '2':
                        # Remove a restaurant
                        print("\nRemoving a restaurant...")

                        # Print the list again
                        print(f"\nHere is your list: {selected_list}")

                        # Print the contents of the selected CSV list
                        read_and_display_restaurants(selected_list)

                        # Ask for the number of the restaurant to remove
                        while True:
                            
                            remove_choice = input("\nEnter the number of the restaurant you want to remove: ")
                            if remove_choice.isdigit() and 1 <= int(remove_choice) <= len(restaurants):
                                remove_index = int(remove_choice) - 1
                                break
                            else:
                                invalid_input_message(len(restaurants))

                        # Remove the selected restaurant
                        del restaurants[remove_index]

                        # Update the CSV file
                        with open(f"{selected_list}.csv", mode='w', newline='') as file:
                            writer = csv.writer(file)
                            writer.writerow(LIST_HEADER)  # Rewrite the header
                            writer.writerows(restaurants)

                        # Print updated list
                        print("\nRestaurant removed successfully!\n")

                        read_and_display_restaurants(selected_list)

                    elif option == '3':
                        # Save
                        return

                    else:
                        invalid_input_message(3)
            else:
                invalid_input_message(len(csv_files))
        else:
            invalid_input_message()

def remove_list():
    print("\nRemoving a list...")
    
    # Get a list of all CSV files in the current directory
    csv_files = get_csv_files()
    
    if not csv_files:
        print("No lists found.")
        return
    
    while True:
        # Display the available lists with numbers
        display_restaurant_list_options(csv_files)

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
                invalid_input_message(len(csv_files))
        else:
            invalid_input_message()

# Main function to run the program
def main():
    while True:
        display_menu()
        choice = input("\nPlease enter the number of your choice (1-5): ")

        if choice.isdigit():
            if choice == '1':
                create_new_list()
            elif choice == '2':
                select_list()
            elif choice == '3':
                edit_list()
            elif choice == '4':
                remove_list()
            elif choice == '5':
                print("\nExiting the program. Goodbye!")
                exit()
            else:
                invalid_input_message(5)
        else:
            invalid_input_message()

# Run the main function
if __name__ == "__main__":
    main()
