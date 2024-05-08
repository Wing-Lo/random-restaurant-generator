import re, csv, os

from filter import FoodTypeFilter, PriceRangeFilter # Importing the filter classes

def read_and_display_restaurants(filename):
    print("\nRestaurants in the selected list:")
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

# Function to display the menu options
def display_menu():
    print("\nMenu:")
    print("1. Create a new restaurant list")
    print("2. Select a restaurant list to roll")
    print("3. Edit restaurant list")
    print("4. Remove restaurant list")
    print("5. Exit Program")

def get_csv_files(directory="."):
    return [file[:-4] for file in os.listdir(directory) if file.endswith('.csv')]

def display_restaurant_list_options(restaurant_lists):
    print(f"\nRestaurant lists:")
    for index, list in enumerate(restaurant_lists, start=1):
        print(f"{index}. {list}")

def filter_restaurant_options(list_name, food_type, price_range):
    filtered_options = []
    food_filter = FoodTypeFilter(food_type)
    price_filter = PriceRangeFilter(price_range)

    # Open the CSV file
    with open(f"{list_name}.csv", mode="r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row

        for row in reader:
            if len(row) < 3:  # Ensure the row has the required number of values
                continue

            # Check if both food and price filters match
            if food_filter.filter(row) and price_filter.filter(row):
                filtered_options.append(row)  # Assuming the restaurant name is in the first column (index 0)

    return filtered_options