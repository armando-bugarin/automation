from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table
import os
import re
import shutil

console = Console()

def create_folder(folder_name):
    try:
        os.mkdir(folder_name)
        console.print(f"Folder '{folder_name}' created successfully.", style="green")
    except FileExistsError:
        console.print(f"Folder '{folder_name}' already exists.", style="yellow")

def move_documents(user_folder, temp_folder):
    try:
        os.mkdir(temp_folder)
    except FileExistsError:
        console.print(f"Temporary folder '{temp_folder}' already exists.", style="yellow")

    user_files = glob.glob(os.path.join(user_folder, '*.txt'))
    for file_path in user_files:
        shutil.move(file_path, temp_folder)
    console.print(f"Moved documents from '{user_folder}' to '{temp_folder}'.", style="green")

def sort_documents(source_folder, destination_folder):
    file_types = {'document': ['.txt'], 'email': ['.mail'], 'log': ['.log.txt']}
    for doc_type, extensions in file_types.items():
        for ext in extensions:
            files = glob.glob(os.path.join(source_folder, '*' + ext))
            if files:
                doc_folder = os.path.join(destination_folder, doc_type)
                os.makedirs(doc_folder, exist_ok=True)
                for file_path in files:
                    shutil.move(file_path, doc_folder)
                console.print(f"Moved {doc_type} files to '{doc_folder}'.", style="green")

def parse_log_file(log_file, target_folder):
    errors = []
    warnings = []

    with open(log_file, 'r') as log:
        for line in log:
            if 'ERROR' in line:
                errors.append(line)
            elif 'WARNING' in line:
                warnings.append(line)

    with open(os.path.join(target_folder, 'errors.log'), 'w') as error_log:
        error_log.writelines(errors)
    with open(os.path.join(target_folder, 'warnings.log'), 'w') as warning_log:
        warning_log.writelines(warnings)

    console.print(f"Parsed log file '{log_file}' for errors and warnings.", style="green")

def menu():
    while True:
        console.print("\n[bold]Automation Tasks:[/bold]")
        console.print("1. Create a new folder")
        console.print("2. Move documents for a deleted user")
        console.print("3. Sort documents into appropriate folders")
        console.print("4. Parse a log file for errors and warnings")
        console.print("5. Count the number of specific file types in a directory")
        console.print("6. Rename files based on a specific pattern")
        console.print("7. Automatically back up specific folders")
        console.print("0. Exit")

        choice = Prompt.ask("Enter the task number (0-7): ")

        if choice == '1':
            folder_name = Prompt.ask("Enter the folder name: ")
            create_folder(folder_name)
        elif choice == '2':
            user_folder = Prompt.ask("Enter the path of the user folder: ")
            temp_folder = Prompt.ask("Enter the path of the temporary folder: ")
            move_documents(user_folder, temp_folder)
        elif choice == '3':
            source_folder = Prompt.ask("Enter the path of the source folder: ")
            destination_folder = Prompt.ask("Enter the path of the destination folder: ")
            sort_documents(source_folder, destination_folder)
        elif choice == '4':
            log_file = Prompt.ask("Enter the path of the log file: ")
            target_folder = Prompt.ask("Enter the path of the target folder: ")
            parse_log_file(log_file, target_folder)
        elif choice == '5':
            # Add your implementation for counting file types in a directory
            pass
        elif choice == '6':
            # Add your implementation for renaming files based on a specific pattern
            pass
        elif choice == '7':
            # Add your implementation for automatically backing up specific folders
            pass
        elif choice == '0':
            console.print("Exiting the application. Goodbye!", style="green")
            break
        else:
            console.print("Invalid choice. Please enter a valid task number (0-7).", style="yellow")

if __name__ == "__main__":
    menu()
