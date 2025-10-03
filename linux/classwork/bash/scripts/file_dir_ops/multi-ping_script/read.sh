#!/bin/bash

## this script will pin a domain 4 times, and save the logs to a file called ping_results.txt

## check for one command line argument

## ping the argument 4 times

## save the results to a file called ping_results.txt

filename = "ping_results.txt"

if [ $# -ne 1 ];
then
	echo "Usage: $0 [Domain Name]"
	exit 1
fi

ping -c4 $1 > "$filename"
echo "Done!"
