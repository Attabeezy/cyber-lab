#! /bin/bash

# Script to create a backup of a specified file with a timestamp

# Check if exactly one argument is provided
if [ $# -ne 1 ];
then
    echo "Usage: $0 [filename]"               # Print usage instructions
    echo "filename: the name of the file you want to backup"
    exit 1                                    # Exit if argument count is not equal to 1
fi

# Assign the first argument to variable 'file'
file=$1

# Check if the argument is a valid file
if [ ! -f "$file" ];
then
    echo "$file is not a regular file"        # Print error if not a file
    exit 1                                    # Exit if condition fails
fi

# Generate timestamp in Year-Month-Day-Hour-Minute format
timestamp=$(date +%F-%H:%M)

# Define backup file name with timestamp and .bak extension
backup_file="${file}_${timestamp}.bak"

# Copy original file to new backup file
cp "$file" "$backup_file"

# Print confirmation message
echo "Backup of $file created as $backup_file"
