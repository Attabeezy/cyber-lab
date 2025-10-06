#! /bin/bash

# Script to calculate the total size of all files in a specified directory

# Check if exactly one argument is provided
if [ $# -ne 1 ];
then
    echo "Usage: $0 [directory]"              # Print usage instructions
    echo "directory: the path of the directory you want to calculate size for"
    exit 1                                    # Exit if argument count is not equal to 1
fi

# Assign the first argument to variable 'directory'
directory=$1

# Check if the argument is a valid directory
if [ ! -d "$directory" ];
then
    echo "$directory is not a valid directory" # Print error if not a directory
    exit 1                                     # Exit if condition fails
fi

# Calculate the total size of the directory using 'du' command
total_size=$(du -sh "$directory" | cut -f1)

# Print the result
echo "The total size of all files in $directory is: $total_size"
