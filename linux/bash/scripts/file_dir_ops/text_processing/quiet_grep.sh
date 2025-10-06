#! /bin/bash

## this script checks a file for some string and then quietly searches

if [ $# -ne 2 ];
then
	echo "Usage: $0 [string] [filename]"
	echo "string: The string to search for"
	echo "filename: filename to search through"
	exit 1
fi

grep -q -i "$1" "$2"

if [ $? -ne 0 ];
then
	echo "Grep didn't find anything"
else
	echo "Grep found some instance of $1"
fi
