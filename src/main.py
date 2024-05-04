import csv, random

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
    print("4. View a list")
    print("5. Exit")

# Function to create a new list
def create_new_list():
    print("Creating a new list...")
    # Your code for creating a new list goes here

# Function to select a list
def select_list():
    print("Selecting a list...")
    # Your code for selecting a list goes here

# Function to add or remove options
def add_or_remove_options():
    print("Adding or removing options...")
    # Your code for adding or removing options goes here

# Function to view a list
def view_list():
    print("Viewing a list...")
    # Your code for viewing a list goes here

# Main function to run the program
def main():
    while True:
        display_menu()
        choice = input("Please enter the number of your choice (1-5): ")

        if choice == '1':
            create_new_list()
        elif choice == '2':
            select_list()
        elif choice == '3':
            add_or_remove_options()
        elif choice == '4':
            view_list()
        elif choice == '5':
            print("Exiting the program. Goodbye!")
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

# Run the main function
if __name__ == "__main__":
    main()