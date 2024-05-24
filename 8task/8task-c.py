import shutil
import argparse #The argparse module makes it easy to write user-friendly command-line interfaces
import os
import zipfile

def compress_folder(folder_path, output_name):
    """Compress the given folder into a zip file."""
    # Check if the specified folder path exists
    if not os.path.isdir(folder_path):
        print(f"Error: The folder path '{folder_path}' does not exist.")
        return
    
    try:
        # Create a zip file from the specified folder
        shutil.make_archive(output_name, 'zip', folder_path)
        print(f"Folder '{folder_path}' compressed to '{output_name}.zip'")
    except Exception as e:
        # Handle any errors that occur during compression
        print(f"Error compressing folder '{folder_path}': {e}")

def decompress_file(zip_path):
    """Decompress the given zip file."""
    # Check if the specified file is a valid zip file
    if not zipfile.is_zipfile(zip_path):
        print(f"Error: '{zip_path}' is not a valid zip file.")
        return  
    
    # Determine the output folder name by removing the file extension
    output_folder = os.path.splitext(zip_path)[0]
    try:
        # Extract the contents of the zip file to the output folder
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(output_folder)
        print(f"File '{zip_path}' decompressed to '{output_folder}'")
    except Exception as e:
        # Handle any errors that occur during decompression
        print(f"Error decompressing file '{zip_path}': {e}")

def main():
    # Create an argument parser
    parser = argparse.ArgumentParser(description="Compress or decompress folders based on operations.")
    
    # Add subparsers for 'compress' and 'decompress' commands
    subparsers = parser.add_subparsers(dest='command')
    
    # Add 'compress' subparser
    parser_compress = subparsers.add_parser('compress', help='Compress a folder')
    group = parser_compress.add_mutually_exclusive_group(required=True)
    # Add mutually exclusive options for compressing different folders
    group.add_argument('--file_manager', action='store_true', help='Compress file-manager folder')
    group.add_argument('--sorter', action='store_true', help='Compress sorter folder')
    # Add argument to specify the output name for the compressed file
    parser_compress.add_argument('output_name', type=str, help='The name of the output zip file')

    # Add 'decompress' subparser
    parser_decompress = subparsers.add_parser('decompress', help='Decompress the given zip file')
    # Add an argument to specify the zip file to decompress 
    parser_decompress.add_argument('file_name', type=str, help='The zip file to decompress')
    
    # Parse the command-line arguments
    args = parser.parse_args()
    
    # Handle the 'compress' command
    if args.command == 'compress':
        if args.file_manager:
            folder_path = 'D:/projects/python'
        elif args.sorter:
            folder_path = 'D:/projects/python/6task'
        compress_folder(folder_path, args.output_name)
    
    # Handle the 'decompress' command
    elif args.command == 'decompress':
        decompress_file(args.file_name)
    
    else:
        # Print help message if no valid command is provided
        parser.print_help()

if __name__ == '__main__':
    main()



# Importing Libraries:

# argparse: To handle command-line arguments.
# os: To interact with the operating system, such as checking if a directory exists.
# shutil: To perform high-level file operations like creating a zip archive.
# zipfile: To handle zip file operations, including checking if a file is a valid zip file and extracting its contents.
# Function compress_folder:

# Parameters: folder_path (the path of the folder to compress) and output_name (the name of the output zip file).
# Logic:
# Check if the provided folder path exists.
# If it exists, create a zip archive of the folder.
# Print appropriate success or error messages based on the operation's outcome.
# Function decompress_file:

# Parameter: zip_path (the path of the zip file to decompress).
# Logic:
# Check if the provided file is a valid zip file.       
# If it is, extract the contents to a folder named after the zip file (minus the extension).
# Print appropriate success or error messages based on the operation's outcome.
# Function main:

# Argument Parsing:
# Set up a main argument parser with a description of the script.
# Add subparsers for the compress and decompress commands.
# For the compress command, add mutually exclusive options (--file-manager and --sorter) to specify which folder to compress.
# For the decompress command, add an argument to specify the zip file to decompress.
# Logic:
# Parse the provided command-line arguments.
# Based on the parsed command, call the appropriate function (compress_folder or decompress_file) with the correct parameters.
# If no valid command is provided, print the help message.
# Usage:
# To compress the file-manager folder:


# python 8task-c.py compress --file-manager
# This will compress the folder at D:/projects/python/6task into a zip file named file_manager_compressed.zip.

# To compress the sorter folder:

# python 8task-c.py compress --sorter
# This will compress the folder at D:/projects/python into a zip file named sorter_compressed.zip.

# To decompress a zip file:

# python 8task-c.py decompress akshu.zip
# This will decompress the zip file akshu.zip into a folder named akshu.

# The script allows you to easily compress specific folders into zip files or decompress zip files using command-line arguments.
# The argparse library provides a user-friendly interface for specifying the desired operation and relevant parameters, while shutil 
# and zipfile handle the actual file operations. The script includes error handling to ensure that invalid paths or files are 
# appropriately flagged.




# directory_path = 'D:\projects\python\ex'

# archive_path = 'name'

# shutil.make_archive(archive_path, 'zip', directory_path)

# print('The Python file was compressed successfully!')



