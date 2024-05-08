"""
This module provides utility functions to validate and sanitise user inputs.

It includes functions to display invalid input messages, sanitise filenames
by converting them to a consistent format, and validate input strings against
a set of allowed characters.
"""
import re

def invalid_input_message(max_val=None):
    """Prints an invalid input message, customized based on the context provided."""
    if max_val is not None:
        print(f"\nInvalid choice. Please choose a number between 1 and {max_val}.")
    else:
        print("\nInvalid input. Please enter a number.")

def sanitise_filename(filename):
    """
    Sanitizes the provided filename by converting it to lowercase and replacing spaces with hyphens.
    
    Args:
        filename (str): The filename to sanitize.
        
    Returns:
        str: The sanitized filename.
    """
    filename = filename.lower()  # Convert to lowercase
    filename = filename.replace(" ", "-")  # Replace spaces with hyphens
    return filename

def is_valid_input(input_string):
    """
    Checks if the input string contains only allowed characters (alphanumeric and hyphens).
    
    Args:
        input_string (str): The string to validate.
        
    Returns:
        bool: True if the string is valid, False otherwise.
    """
    # Regular expression to match only alphanumeric characters and hyphen
    pattern = r'^[a-zA-Z0-9\-]+$'
    return bool(re.match(pattern, input_string))
