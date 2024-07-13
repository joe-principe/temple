#!/usr/bin/env python

import shutil
from pathlib import Path

# This program copies files from the templates folder to the current working
# directory using the `temple` command. If the file's name contains the word
# "Makefile", the user has the template_choice to should_rename it to just "Makefile" upon
# copying
def main():
    template_dir: str = "/home/joe/Templates"
    uri_len: int = len("file://")
    template_path: Path = Path(template_dir)

    print("Available Templates")

    # Print out all of the available templates
    paths = []
    filenames = []
    i: int = 0
    for i, child in enumerate(template_path.iterdir()):
        paths.append(child)
        filenames.append(child.as_uri()[len(template_dir) + uri_len + 1:])
        print(f"{i + 1}: {filenames[i]}")

    # Get the user's choice
    print()
    template_choice: str = ""
    while True:
        template_choice = input("Enter the number of the template to copy: ")

        try:
            int(str(template_choice))
        except ValueError:
            print("Invalid input. Please enter a valid number\n")
            continue

        if int(template_choice) < 1 or int(template_choice) > i + 1:
            print(f"Invalid input. Please input a value between 1 and {i + 1}\n")
        else:
            print(f"Selection: {filenames[int(str(template_choice)) - 1]}\n")
            break

    ind: int = int(str(template_choice)) - 1
    file_to_copy_name: str = filenames[ind]
    file_to_copy_path: Path = paths[ind]

    # Offer to rename the file to "Makefile"
    should_rename: bool = False
    if file_to_copy_name.find("Makefile") != -1 and file_to_copy_name.find("Makefile") != 0:
        rename_choice = input("This template contains \"Makefile\" in its name."
                              " Would you like to rename it to just "
                              "\"Makefile\" on copy? (Y/n): ")

        if rename_choice.lower().startswith('y') or not rename_choice:
            should_rename = True
            file_to_copy_name = "Makefile"

        print()

    # Check if a file exists and offer to overwrite it
    if Path(f"./{file_to_copy_name}").exists():
        overwrite_choice = input(f"A file with the name \"{file_to_copy_name}\""
                                 " already exists in this directory. Do you "
                                 "want to overwrite it? (Y/n): ")

        if overwrite_choice.lower().startswith('n'):
            exit()

        print()

    # Copy the template
    # result = []
    if should_rename:
        shutil.copy(file_to_copy_path, "./Makefile")
        # result = shutil.copy(file_to_copy_path, "./Makefile")
    else:
        shutil.copy(file_to_copy_path, "./")
        # result = shutil.copy(file_to_copy_path, "./")

    print("File successfully copied!")

    # Gotta be honest, I have no idea how to create an empty Path variable, so I
    # don't know if checking result actually does anything
    # if result:
    #     print("File successfully copied!")
    # else:
    #     print("File could not be copied")

if __name__ == "__main__":
    main()
