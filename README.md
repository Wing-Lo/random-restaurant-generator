# Random restaurant generator app

## Source control repository

[Link to Github](https://github.com/Wing-Lo/random-restaurant-generator)

## Code Style Guide

This code was styled according to [the PEP 8 Style Guide.](https://peps.python.org/pep-0008/)

## Purpose of the application

The Random Restaurant Generator is a Python terminal app simplifying dining decisions. Users create personalized lists, categorize eateries, and roll random selections. Flexible editing allows for list management, ensuring evolving preferences. With streamlined decision-making, users enjoy culinary exploration effortlessly.

## List of features

### 1. Create a new restaurant list

This feature allows the user to create a new restaurant list. Here's how it works:

- The user is prompted to enter the name of the new restaurant list.
- The input is validated to ensure it contains only allowed characters.
- A new CSV file is created with the sanitized filename.
- The user can then add restaurant details such as name, food type, and price range to the list.
- After adding each restaurant, the user is given the option to add another restaurant, save and return to the menu, or exit the program.

### 2. Select a restaurant list to roll

This feature allows the user to select a restaurant list and roll a random restaurant from it. Here's how it works:

- The user is prompted to select a list from the available CSV files.
- After selecting a list, the user can choose the type of food and price range they prefer.
- Based on the user's choices, the list is filtered to roll from relevant restaurants.
- A random restaurant is selected from the filtered list and displayed to the user.
- The user is then given options to either exit the program, re-roll, or go back to the menu.

### 3. Edit restaurant list

This feature allows the user to edit an existing restaurant list by adding or removing restaurants. Here's how it works:

- The user selects a list they want to edit from the available CSV files.
- They are then presented with options to add another restaurant, remove a restaurant, or go back to the menu.
- If the user chooses to add a restaurant, they can input the restaurant name, food type, and price range.
- If the user chooses to remove a restaurant, they can select a restaurant from the list to remove.
- After each action (adding or removing), the updated list is displayed to the user.

### 4. Remove restaurant list

This feature allows the user to remove an existing restaurant list. Here's how it works:

- The user is presented with a list of existing restaurant lists.
- They can select a list they want to remove.
- The user is then asked for confirmation before the selected list is deleted.
- If the user confirms, the selected list (CSV file) is removed from the directory.
- If the user enters an invalid confirmation response, the program prompts the user to enter "yes" or "no" until a valid response is provided.

## Implementation Plan

Two board have been developed in Trello. One for monitoring the whole project and one for the checklists for each feature. Please see screenshots below.

![Trello board - main](/docs/screen-shot-trello-1.png)
![Trello board - feature](/docs/screen-shot-trello-2.png)

## References

- Python Software Foundation (no date), 'csv — CSV File Reading and Writing', Python Documentation, viewed 5 May 2024, [https://docs.python.org/3/library/csv.html](https://docs.python.org/3/library/csv.html).

- Python Software Foundation (no date), 'os — Miscellaneous operating system interfaces', Python Documentation, viewed 6 May 2024, [https://docs.python.org/3/library/os.html](https://docs.python.org/3/library/os.html).

- Python Software Foundation (no date), 'PEP 8 -- Style Guide for Python Code', Python Enhancement Proposals, viewed 5 May 2024, [https://peps.python.org/pep-0008/](https://peps.python.org/pep-0008/).

- Python Software Foundation (no date), 'random — Generate pseudo-random numbers', Python Documentation, viewed 7 May 2024, [https://docs.python.org/3/library/random.html](https://docs.python.org/3/library/random.html).

- Python Software Foundation (no date), 're — Regular expression operations', Python Documentation, viewed 8 May 2024, [https://docs.python.org/3/library/re.html](https://docs.python.org/3/library/re.html).