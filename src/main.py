import csv, re, os

# Function to print welcome message
def display_welcome_message():
    print("Welcome to the Random Restaurant Generator!")
    print("This tool will help you find a restaurant based on your preferences.")
    print("Let's get started!")

# Call the function to display the welcome message
display_welcome_message()

# Function to display the menu options
def display_menu():
    print("\nMenu Options:")
    print("1. Create a new list")
    print("2. Select a list")
    print("3. Add or remove options")
    print("4. Exit")

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
    print("Creating a new list...")
    while True:
        # Ask the user for the name of the new list
        list_name = input("Enter the name of the new list: ")
        
        # Check if the input contains only allowed characters
        if not is_valid_input(list_name):
            print("Error: List name can only contain alphanumeric characters and hyphens (-). Please try again.")
            continue
        
        # Adjust filename
        list_name = adjust_filename(list_name)

        # Open a new CSV file with the adjusted list name
        with open(f"{list_name}.csv", mode='w', newline='') as file:
            writer = csv.writer(file)

            # Write the header row
            writer.writerow(["Restaurant Name", "Type of Food", "Price"])

            while True:
                # Ask the user for restaurant name
                restaurant_name = input("Enter the restaurant name: ")

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
                    food_types = ["Steakhouse", "Italian", "Japanese", "Cafe", "Vegetarian", "Mexican", "Chinese", "Other"]
                    food_type = food_types[int(food_choice) - 1]
                else:
                    print("Invalid choice. Please choose a number between 1 and 8.")
                    continue

                # Ask the user to choose the price range
                print("\nChoose the price range:")
                print("1. Cheap")
                print("2. Mid-range")
                print("3. Expensive")
                price_choice = input("Enter your choice: ")

                if price_choice == '1':
                    price_range = "Cheap"
                elif price_choice == '2':
                    price_range = "Mid-range"
                elif price_choice == '3':
                    price_range = "Expensive"
                else:
                    print("Invalid choice. Please choose a number between 1 and 3.")
                    continue

                # Write the restaurant details to the CSV file
                writer.writerow([restaurant_name, food_type, price_range])

                # Ask the user for next action
                print("\nOptions:")
                print("1. Enter another restaurant")
                print("2. Save and roll")
                print("3. Exit")
                next_action = input("Enter your choice: ")

                if next_action == '1':
                    continue
                elif next_action == '2':
                    print("List saved successfully!")
                    break
                elif next_action == '3':
                    print("List saved successfully! Returning to main menu.")
                    return True  # Signal to return to the main menu
                else:
                    print("Invalid choice. Exiting without saving.")
                    return False  # Signal to exit the program

# Function to select a list
def select_list():
    print("Selecting a list...")

# Function to add or remove options
def add_or_remove_options():
    print("Adding or removing options...")
    # Your code for adding or removing options goes here

# Main function to run the program
def main():
    while True:
        display_menu()
        choice = input("Please enter the number of your choice (1-4): ")

        if choice == '1':
            should_return_to_menu = create_new_list()
            if not should_return_to_menu:
                print("Exiting the program. Goodbye!")
                break
        elif choice == '2':
            select_list()
        elif choice == '3':
            add_or_remove_options()
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

# Run the main function
if __name__ == "__main__":
    main()