import re

def invalid_input_message(max_val=None):
    if max_val is not None:
        print(f"\nInvalid choice. Please choose a number between 1 and {max_val}.")
    else:
        print("\nInvalid input. Please enter a number.")

# Function to sanitise filename to lowercase and replace spaces with hyphens
def sanitise_filename(filename):
    filename = filename.lower()  # Convert to lowercase
    filename = filename.replace(" ", "-")  # Replace spaces with hyphens
    return filename

# Function to check if the input contains only allowed characters
def is_valid_input(input_string):
    # Regular expression to match only alphanumeric characters and hyphen
    pattern = r'^[a-zA-Z0-9\-]+$'
    return bool(re.match(pattern, input_string))