import argparse  # Import the argparse module for parsing command-line arguments
import os  # Import the os module for interacting with the operating system
import zipfile

# File Manager Operations

def list_files():
    for file in os.listdir('.'): # Iterate over items in the current directory
        if os.path.isfile(file): # Check if the item is a file
            print(file)

def list_folders():
    for file in os.listdir('.'): #Iterate over items in the current directory
        if os.path.isdir(file): # Check if the item is a directory
            print(file)

# Function to sort and print all files in the current directory
def sort_files():
    files = [f for f in os.listdir('.') if os.path.isfile(f)] # Create a list of files in the current directory
    files.sort() # Sort the list of files
    for file in files:  # Iterate over the sorted list
        print(file)

def sort_folders():
    folders = [f for f in os.listdir('.') if os.path.isdir(f)] ## Create a list of directories in the current directory
    folders.sort() # Sort the list of directories
    for folder in folders: # Iterate over the sorted list
        print(folder)

 # Check if the specified file is a valid zip file
def compress_files():
    with zipfile.ZipFile('files.zip', 'w') as zipf:
        for file in os.listdir('.'):
            if os.path.isfile(file):
                zipf.write(file)

def compress_folders():
    with zipfile.ZipFile('folders.zip', 'w') as zipf:
        for folder in os.listdir('.'):
            if os.path.isdir(folder):
                for root, _, files in os.walk(folder):           # os. walk() finds each file and path in filepath and generates a 3-tuple
                     for file in files:                #(a type of 3-item list) with components we will refer to as root , dirs , and files
                            zipf.write(os.path.join(root, file) )

                       
def run_file_manager(args):         
    if args.list:
        if args.file:
            list_files()
        elif args.folder:
            list_folders()
        else:
            print("Specify --file or --folder with --list")

def run_sorter(args):
    if args.file:
        sort_files()
    elif args.folder:
        sort_folders()
    else:
        print("Specify --file or --folder with --sort")

def run_compressor(args):
    if args.file_manager:
        compress_files()
        print("print file-manager")
    elif args.sorter:
        compress_folders()
    else:
        print("Specify --file-manager or --sorter with --compressor")

def main():
    parser = argparse.ArgumentParser(description="Run File Manager, Sorter, or Compressor operations based on command-line arguments.")
    
    parser.add_argument('--run', action='store_true', help='Run the specified operation')

    subparsers = parser.add_subparsers(help='Operations', dest='operation')

    # File Manager parser
    file_manager_parser = subparsers.add_parser('file-manager', help='File Manager operations')
    file_manager_parser.add_argument('--list', action='store_true', help='List files or folders')
    file_manager_parser.add_argument('--file', action='store_true', help='List files')
    file_manager_parser.add_argument('--folder', action='store_true', help='List folders')
    file_manager_parser.set_defaults(func=run_file_manager)

    # Sorter parser
    sorter_parser = subparsers.add_parser('sort', help='Sort operations')
    sorter_parser.add_argument('--file', action='store_true', help='Sort files')
    sorter_parser.add_argument('--folder', action='store_true', help='Sort folders')
    sorter_parser.set_defaults(func=run_sorter)

    # Compressor parser
    compressor_parser = subparsers.add_parser('compressor', help='Compressor operations')
    compressor_parser.add_argument('--file-manager', action='store_true', help='Compress files')
    compressor_parser.add_argument('--sorter', action='store_true', help='Compress folders')
    compressor_parser.set_defaults(func=run_compressor)

    args = parser.parse_args()

    if args.run:
        if args.operation:
            args.func(args)
        else:
            print("Specify an operation to run")
    else:
        print("Use --run to execute the operation")

if __name__ == "__main__":
    main()


# python 8task-d.py --run file-manager --list --file
# python 8task-d.py --run file-manager --list --folder


# python 8task-d.py --run sort --file
# python 8task-d.py --run sort --folder


# python 8task-d.py --run compressor --file-manager
# python 8task-d.py --run compressor --sorter


