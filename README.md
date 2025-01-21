# Password Generator Application

This repository contains a Python-based application for generating secure passwords with customizable options. The graphical user interface (GUI) is built using the `tkinter` and `customtkinter` libraries.

## Features

- **Customizable Password Length:** Specify the desired length of the password.
- **Character Options:** Choose to include or exclude:
  - Numbers
  - Letters (lowercase only)
  - Special symbols
  - Spaces
- **Randomization:** Ensures the password is highly randomized and secure.
- **Simple GUI:** User-friendly interface for easy interaction.

## Prerequisites

Ensure you have the following Python libraries installed:

- `tkinter` (standard library in Python)
- `customtkinter` (install via pip: `pip install customtkinter`)
- `matplotlib` (install via pip: `pip install matplotlib`)

## How to Run

1. Clone the repository or copy the script to your local machine.
2. Ensure all dependencies are installed.
3. Run the script using Python:
   ```bash
   python <script_name>.py
   ```
4. Use the application interface to generate your password.

## GUI Components

- **Main Entry Field:** Displays the generated password.
- **Length Entry Field:** Input for the desired password length.
- **Generate Button:** Triggers the password generation process.
- **Option Toggles:** Switches for selecting password components (numbers, characters, symbols, spaces).

## Code Breakdown

### Libraries Used

- `tkinter`: For GUI components.
- `customtkinter`: For enhanced and customizable GUI elements.
- `random`: For generating random selections.
- `matplotlib`: Included to avoid conflicts when using `customtkinter`.

### Functions

- **`generate_password_func()`:**
  - Reads user input for password length and selected options.
  - Generates a randomized password based on the chosen criteria.
  - Displays the password in the main entry field.

### Variables

- **`list_of_numbers`:** Contains numeric characters ('0'-'9').
- **`list_of_chars`:** Contains lowercase alphabetical characters.
- **`list_of_symbols`:** Contains special characters.
- **`str_`:** Represents a space character.
- **`var_char`, `var_num`, `var_sym`, `var_spa`:** `IntVar` objects used for toggling character options.

## Sample Usage

1. Enter the desired password length in the second entry field.
2. Select the components to include using the toggles (e.g., numbers, symbols).
3. Click the **Generate** button.
4. Copy the generated password from the main entry field.

## Notes

- If no options are selected, the generator defaults to numbers.
- The application alerts the user if the password length field is left empty.

## Customization

Feel free to modify the script to:

- Add more character sets.
- Change the GUI appearance.
- Add additional functionality, such as saving generated passwords.

## License

This project is open-source and available for modification and distribution under the Apache License 2.0.

---

## Developer
***Youssef khaled***

Enjoy secure and customizable password generation with this Python application!

