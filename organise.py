import os
import shutil
from pathlib import Path

EXTENSION_FOLDERS = {
    'pdf': 'PDF Files',
    'exe': 'Executable Files',
    'txt': 'Text Files',
    'jpg': 'Image Files',
    'jpeg': 'Image Files',
    'png': 'Image Files',
    'gif': 'Image Files',
    'doc': 'Word Documents',
    'docx': 'Word Documents',
    'xls': 'Excel Files',
    'xlsx': 'Excel Files',
    'ppt': 'PowerPoint Files',
    'pptx': 'PowerPoint Files',
    'mp3': 'Audio Files',
    'wav': 'Audio Files',
    'mp4': 'Video Files',
    'avi': 'Video Files',
    'mkv': 'Video Files',
    'zip': 'Compressed Files',
    'rar': 'Compressed Files',
    '7z': 'Compressed Files',
}

def get_folder_name(file_extension):
    return EXTENSION_FOLDERS.get(file_extension.lower(), f'{file_extension.upper()} Files')

def organize_files_by_type(directory, file_types):
    os.chdir(directory)
    for filename in os.listdir(directory):
        try:
            if os.path.isdir(filename):
                continue

            file_extension = Path(filename).suffix[1:].lower() if '.' in filename else 'No Extension'
            if file_extension in file_types:
                folder_name = get_folder_name(file_extension)
                if not os.path.exists(folder_name):
                    os.makedirs(folder_name)
                shutil.move(filename, os.path.join(folder_name, filename))
        except PermissionError:
            print(f"Permission denied: '{filename}'. Skipping...")
        except Exception as e:
            print(f"Error processing file '{filename}': {e}")
    print("Files organized successfully!")

def display_summary(directory):
    print("\nSummary of Organized Files:")
    for folder in sorted(os.listdir(directory)):
        folder_path = os.path.join(directory, folder)
        if os.path.isdir(folder_path):
            try:
                file_count = len(os.listdir(folder_path))
                print(f'{folder}: {file_count} file(s)')
            except PermissionError:
                print(f"Permission denied when accessing folder: '{folder}'. Skipping...")
            except Exception as e:
                print(f"Error accessing folder '{folder}': {e}")

def show_menu():
    print("File Organizer Menu")
    print("1. Organize PDF Files")
    print("2. Organize Word Documents")
    print("3. Organize Image Files")
    print("4. Organize Video Files")
    print("5. Organize Audio Files")
    print("6. Organize Text Files")
    print("7. Organize Executable Files")
    print("8. Organize Compressed Files")
    print("9. Organize All Files")
    print("0. Exit")

def get_file_types(option):
    options = {
        1: ['pdf'],
        2: ['doc', 'docx'],
        3: ['jpg', 'jpeg', 'png', 'gif'],
        4: ['mp4', 'avi', 'mkv'],
        5: ['mp3', 'wav'],
        6: ['txt'],
        7: ['exe'],
        8: ['zip', 'rar', '7z'],
        9: EXTENSION_FOLDERS.keys()
    }
    return options.get(option, [])

if __name__ == "__main__":
    target_directory = input("Enter the directory path to organize: ").strip()
    if os.path.exists(target_directory) and os.path.isdir(target_directory):
        while True:
            show_menu()
            try:
                choice = int(input("Enter your choice: "))
                if choice == 0:
                    print("Exiting the program.")
                    break
                file_types = get_file_types(choice)
                if file_types:
                    organize_files_by_type(target_directory, file_types)
                    display_summary(target_directory)
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Please enter a valid number.")
    else:
        print("Invalid directory path. Please try again.")
