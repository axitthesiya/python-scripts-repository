import os  # Imports the os module to interact with the operating system (e.g., file and directory operations)
import sys  # Imports the sys module to interact with the Python interpreter (e.g., command-line arguments)
import shutil  # Imports the shutil module to perform high-level file operations (e.g., copying and moving files)
import datetime  # Imports the datetime module to work with dates and times

# Function to create the folder structure based on the date
def create_folder_structure(base_path, date):
    # Create a folder name for the month (e.g., 'January', 'February')
    #he format code "%b" converts the date to the abbreviated month name.
    #The os.path.join function is used to concatenate the base_path with the formatted month string, 
    #creating a path to a directory named after the abbreviated month.
    month_folder = os.path.join(base_path, date.strftime("%B"))
    # Calculate the week number within the month
    # The expression week number = (date.day - 1) // 7 + 1 may give the first date of the week, with Sunday as the first day of the week.
    week_number = (date.day - 1) // 7 + 1
    # Create a folder name for the week (e.g., 'week_1', 'week_2')
    week_folder = os.path.join(month_folder, f"week_{week_number}")
    
    if not os.path.exists(week_folder):
        os.makedirs(week_folder)
    
    # Return the path to the week folder
    return week_folder

def move_files(base_path):
    for file_name in os.listdir(base_path):
        file_path = os.path.join(base_path, file_name)
        if os.path.isfile(file_path):
            creation_time = os.path.getctime(file_path)
            # Convert the creation time to a datetime object
            creation_date = datetime.datetime.fromtimestamp(creation_time)
            target_folder = create_folder_structure(base_path, creation_date)
            shutil.move(file_path, os.path.join(target_folder, file_name))

# Function to move folders into their respective folders based on their creation date
def move_folders(base_path):
    # Iterate over all files and directories in the base path
    for folder_name in os.listdir(base_path):
        # Get the full path to the file or directory
        folder_path = os.path.join(base_path, folder_name)
        # Check if the current path is a directory and does not contain certain keywords
        if os.path.isdir(folder_path) and not any(keyword in folder_name for keyword in ["files_", "folder_"]):
            creation_time = os.path.getctime(folder_path)
            # Convert the creation time to a datetime object
            creation_date = datetime.datetime.fromtimestamp(creation_time)
            target_folder = create_folder_structure(base_path, creation_date)
            # Move the directory to the target folder
            shutil.move(folder_path, os.path.join(target_folder, folder_name))

# Main function to parse command-line arguments and call the appropriate function
def main():
    # Check if the number of command-line arguments is not equal to 3
    if len(sys.argv) != 3:
        # Print usage information and return
        print("Usage: python sorter.py --sort --file|--folder")
        return

    # Get the current working directory as the base path
    base_path = os.getcwd()
    # Check if the command-line arguments specify sorting files
    if sys.argv[1] == '--sort' and sys.argv[2] == '--file':
        move_files(base_path)
    # Check if the command-line arguments specify sorting folders
    elif sys.argv[1] == '--sort' and sys.argv[2] == '--folder':
        move_folders(base_path)
    else:
        print("Invalid arguments")

if __name__ == "__main__":
    main()

# Explanation of the sys module usage:
# -------------------------------------------------
# sys.argv: A list of command-line arguments passed to the Python script.
# sys.exit(): Exits the Python script.
# sys.path: A list of directories that Python searches for modules.
# sys.stdout: The standard output stream.
# sys.stderr: The standard error stream.
