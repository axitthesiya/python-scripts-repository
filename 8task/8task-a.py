import os
import shutil
import argparse #The argparse module makes it easy to write user-friendly command-line interfaces

def list_files(directory):
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    print("Files:")
    for file in files:
        print(file)

def list_folders(directory):
    # read directory 
    folders = [f for f in os.listdir(directory) if os.path.isdir(os.path.join(directory, f))]
    print("Folders:")
    for folder in folders:
        print(folder)

def list_all(directory):
    print("Files and Folders:")
    for item in os.listdir(directory):
        print(item)

def move_file(source, destination):
    shutil.move(source, destination)
    print(f"Moved '{source}' to '{destination}'")

def move_folder(source, destination):
    shutil.move(source, destination)
    print(f"Moved folder '{source}' to '{destination}'")

def copy_file(source, destination):
    shutil.copy2(source, destination)
    print(f"Copied '{source}' to '{destination}'")

def copy_folder(source, destination):
    shutil.copytree(source, destination)
    print(f"Copied folder '{source}' to '{destination}'")

def delete_file(file_path):
    os.remove(file_path)
    print(f"Deleted file '{file_path}'")

def delete_folder(folder_path):
    print("Cannot delete a folder using this command")

def main():
    parser = argparse.ArgumentParser(description="File Manager")
    parser.add_argument("--list", action="store_true", help="List files or folders")
    parser.add_argument("--file", action="store_true", help="List files")
    parser.add_argument("--folder", action="store_true", help="List folders")
    parser.add_argument("--move", action="store_true", help="Move file or folder")
    parser.add_argument("--copy", action="store_true", help="Copy file or folder")
    parser.add_argument("--delete", help="Delete file or folder")
    parser.add_argument("--destination", help="Destination path")
    parser.add_argument("path", help="Path of file or folder")

    args = parser.parse_args()

    if args.list:
        list_all(args.path)
    elif args.file:
        list_files(args.path)
    elif args.folder:
        list_folders(args.path)
    elif args.move:
        if os.path.isfile(args.path):
            move_file(args.path, args.destination)
        elif os.path.isdir(args.path):
            move_folder(args.path, args.destination)
    elif args.copy:
        if os.path.isfile(args.path):
            copy_file(args.path, args.destination)
        elif os.path.isdir(args.path):
            copy_folder(args.path, args.destination)
    elif args.delete:
        if os.path.isfile(args.path):
            delete_file(args.path)
        elif os.path.isdir(args.path):
            delete_folder(args.path)
    else:
        print("Invalid command")

if __name__ == "__main__":
    main()
