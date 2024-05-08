"""
This module provides functionalities to manage and filter restaurant lists. It
allows users to create, display, edit, and remove lists of restaurants stored
in CSV format. Additionally, it offers the capability to filter these lists
based on food type and price range using imported filter classes.

The module assumes that restaurant data is stored in CSV files with a predefined
structure. It utilizes the FoodTypeFilter and PriceRangeFilter classes from the
'filter' module to apply the desired filters to restaurant data.
"""
import csv
import os
from filter import FoodTypeFilter, PriceRangeFilter # Importing the filter classes

def read_and_display_restaurants(filename):
    """Reads and displays the restaurants from the specified CSV file."""
    print("\nRestaurants in the selected list:")
    try:
        with open(f"{filename}.csv", "r", newline="", encoding="utf-8") as csv_file:
            reader = csv.reader(csv_file)
            next(reader)
            for index, row in enumerate(reader, start=1):
                print(f"{index}. {', '.join(row)}")
    except FileNotFoundError:
        print("File not found. Please make sure the file exists.")

# Function to print welcome message
def display_welcome_message():
    """Prints a welcome message to the user."""
    print("\nWelcome to the Random Restaurant Generator!")
    print("This tool will help you find a restaurant based on your preferences.")
    print("Let's get started!")

# Function to display the menu options
def display_menu():
    """Displays the main menu options to the user."""
    print("\nMenu:")
    print("1. Create a new restaurant list")
    print("2. Select a restaurant list to roll")
    print("3. Edit restaurant list")
    print("4. Remove restaurant list")
    print("5. Exit Program")

def get_csv_files(directory="."):
    """Returns a list of CSV filenames (without extension) in the specified directory."""
    return [file[:-4] for file in os.listdir(directory) if file.endswith(".csv")]

def display_restaurant_list_options(restaurant_lists):
    """Displays the available restaurant lists to the user."""
    print("\nRestaurant lists:")
    for index, list_name in enumerate(restaurant_lists, start=1):
        print(f"{index}. {list_name}")

def filter_restaurant_options(list_name, food_type, price_range):
    """
    Filters the restaurant options from the given list by food type and price range.
    
    Args:
        list_name (str): The name of the restaurant list.
        food_type (str): The desired food type to filter by.
        price_range (str): The desired price range to filter by.
    
    Returns:
        list: A list of restaurants that match the given food type and price range.
    """
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