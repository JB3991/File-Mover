# Import shutil module
import shutil

# Import path module from os
from os import path
import glob

# Set the filename with path
source_path = "/Users/jonathanburnett/Documents/Test1/123.fmf"

# Check the file exist or not
if path.exists(source_path):

    # Set the directory path where the file will be moved
    destination_path = "/Users/jonathanburnett/Library/Application Support/Sports Interactive/Football Manager 2022/tactics"

    # Move the file to the new location
    new_location = shutil.move(source_path, destination_path)

    # Print the new location of the file
    print("The %s is moved to the location, %s" % (source_path, new_location))

else:

    # Print the message if the file not exists
    print("File does not exist.")
