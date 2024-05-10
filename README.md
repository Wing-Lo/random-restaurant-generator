# Random Restaurant Generator Application

## Source Control Repository

[Link to Github](https://github.com/Wing-Lo/random-restaurant-generator)

## Code Style Guide

This code was styled according to the [PEP 8 Style Guide.](https://peps.python.org/pep-0008/)

Example of usage:

- Indentation: Use 4 spaces per indentation level.
- Imports: Imports are on separate lines.
- Inline Comments: Use inline comments sparingly.

## Purpose of the Application

The Random Restaurant Generator is a Python terminal app simplifying dining decisions. Users create personalized lists, categorize eateries, and roll random selections. Flexible editing allows for list management, ensuring evolving preferences. With streamlined decision-making, users enjoy culinary exploration effortlessly.

## List of Features

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

The implementation plan for this project is organized using Trello. The main board consists of three lists: "To Do," "Doing," and "Done," facilitating the monitoring of project progress and due dates. Additionally, checklists are created for each feature, providing clear and easy-to-follow steps. Please refer to the screenshots below.

![Trello board - main](/docs/screen-shot-trello-main.png)
![Trello board - feature 1](/docs/screen-shot-trello-f1.png)
![Trello board - feature 2](/docs/screen-shot-trello-f2.png)
![Trello board - feature 3](/docs/screen-shot-trello-f3.png)
![Trello board - feature 4](/docs/screen-shot-trello-f4.png)

## Installation Guide

Welcome to the installation guide for Random Restaurant Generator. Follow these steps to get the application up and running on your system.

### Step 1: Download the application

1. Navigate to the [GitHub](https://github.com/Wing-Lo/random-restaurant-generator) repository.
2. Click the green `< > Code` button on the page.
3. Select `Download ZIP` from the dropdown menu.

### Step 2: Extract the application

1. Locate the downloaded ZIP file on your computer.
2. Extract the contents of the ZIP file to a directory of your choice.

### Step 3: Execute the application

The application requires Python version 3.10. Follow the instructions below based on your execution preference.

#### Automatic Execution

Run the provided script to automate the execution process:

```bash
cd path/to/extracted/folder
. ./src/start.sh
```

Or, if the above doesn't work, try:

```bash
bash ./src/start.sh
```

This script will check for Python 3.10, install it if necessary, and then execute the application automatically.

#### Manual Execution

To manually execute the application:

1. Open your terminal.
2. Check your current Python version:

```bash
python --version
```

3. If you have an older version or Python is not installed, visit the [Python Download Page](https://www.python.org/downloads/) and install Python 3.10 or the latest version.
4. Once installed, verify the installation by checking the version again:

```bash
python3 --version
```

5. Navigate to the directory containing the application's files.
6. Run the application with the following command:

```bash
python3 ./src/main.py
```

### Dependencies

No external dependencies are required to operate the application. All necessary Python packages (csv, random, os, and re) are included in the [Python Standard Library](https://docs.python.org/3/library/index.html).

### System/hardware Requirements

This program recommends a modern operating system with either:

- Windows 10
- Mac OS Monterey
- Ubuntu 20.04

Ensure that your system meets these requirements for optimal performance.

## References

- Python Software Foundation (n.d.), 'csv — CSV File Reading and Writing', Python Documentation. Retrieved from [https://docs.python.org/3/library/csv.html](https://docs.python.org/3/library/csv.html).

- Python Software Foundation (n.d.), 'os — Miscellaneous operating system interfaces', Python Documentation. Retrieved from [https://docs.python.org/3/library/os.html](https://docs.python.org/3/library/os.html).

- Python Software Foundation (n.d.), 'PEP 8 -- Style Guide for Python Code', Python Enhancement Proposals. Retrieved from [https://peps.python.org/pep-0008/](https://peps.python.org/pep-0008/).

- Python Software Foundation. (n.d.). Python 3.10.2 documentation: Python Standard Library. Retrieved from [https://docs.python.org/3/library/index.html](https://docs.python.org/3/library/index.html).

- Python Software Foundation (n.d.), 'random — Generate pseudo-random numbers', Python Documentation. Retrieved from [https://docs.python.org/3/library/random.html](https://docs.python.org/3/library/random.html).

- Python Software Foundation (n.d.), 're — Regular expression operations', Python Documentation. Retrieved from [https://docs.python.org/3/library/re.html](https://docs.python.org/3/library/re.html).