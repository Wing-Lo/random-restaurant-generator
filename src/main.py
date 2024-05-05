import csv, random, os, re

food_types = ["Steakhouse", "Italian", "Japanese", "Cafe", "Vegetarian", "Mexican", "Chinese", "Other"]
price_ranges = ["Cheap", "Mid-range", "Expensive"]


# Class for filtering by food type
class FoodTypeFilter:
    def __init__(self, choice):
        self.choice = choice

    def filter(self, restaurant):
        return restaurant[1].lower() == self.choice.lower()

# Class for filtering by price range
class PriceRangeFilter:
    def __init__(self, choice):
        self.choice = choice

    def filter(self, restaurant):
        return restaurant[2].lower() == self.choice.lower() 

# Function to print welcome message
def display_welcome_message():
    print("Welcome to the Random Restaurant Generator!")
    print("This tool will help you find a restaurant based on your preferences.")
    print("Let's get started!\n")

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

                if price_choice in ['1', '2', '3']:
                    price_range = price_ranges[int(price_choice) - 1]
                else:
                    print("Invalid choice. Please choose a number between 1 and 3.")
                    continue

                # Write the restaurant details to the CSV file
                writer.writerow([restaurant_name, food_type, price_range])

                # Ask the user for next action
                print("\nOptions:")
                print("1. Enter another restaurant")
                print("2. Save")
                print("3. Exit")
                next_action = input("Enter your choice: ")

                if next_action == '1':
                    continue
                elif next_action == '2':
                    print("List saved successfully!")
                    return True  # Signal to return to the menu options
                elif next_action == '3':
                    print("List saved successfully! Exiting the program.")
                    return True  # Signal to exit the program
                else:
                    print("Invalid choice. Exiting without saving.")
                    return False  # Signal to exit the program

# Function to select a list
def select_list():
    print("Selecting a list...")
    # Get a list of all CSV files in the current directory
    csv_files = [file[:-4] for file in os.listdir() if file.endswith('.csv')]
    
    if not csv_files:
        print("No lists found. Please create a list first.")
        return
    
    # Display the available lists
    print("Available lists:")
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
                    food_type_choice = input("Choose the type of food (1-9): ")
                    
                    if food_type_choice in ['1', '2', '3', '4', '5', '6', '7', '8']:
                        selected_food_type = food_types[int(food_type_choice) - 1]
                        break
                    else:
                        print("Invalid choice. Please choose a number between 1 and 8.")

                while True:
                    price_range_choice = input("Choose the price range (1-4): ")
                    
                    if price_range_choice in ['1', '2', '3']:
                        selected_price_range_choice = price_ranges[int(price_range_choice) - 1]
                        break
                    else:
                        print("Invalid choice. Please choose a number between 1 and 3.")
            
                # Filter restaurant options based on user's choices
                options = filter_restaurant_options(selected_list, selected_food_type, selected_price_range_choice)

                if options:
                    # Perform a random roll and select a restaurant
                    selected_restaurant = random.choice(options)
                    print(f"\nLet's go for {selected_restaurant[0]}")
                else:
                    print("No restaurants match your criteria. Please try again.")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and {}.".format(len(csv_files)))
        else:
            print("Invalid input. Please enter a number.")

def filter_restaurant_options(list_name, food_type, price_range):
    print(food_type, price_range)
    # Open the CSV file
    with open(f"{list_name}.csv", mode='r', newline='') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row

        # Filter restaurant options based on user's choices
        filtered_options = []

        for row in reader:
            if len(row) >= 3:  # Check if the row contains at least three values
                restaurant_name = row
                food_filter = FoodTypeFilter(food_type)
                price_filter = PriceRangeFilter(price_range)
                if food_filter.filter(row) and price_filter.filter(row):
                    filtered_options.append(restaurant_name)

        return filtered_options

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
