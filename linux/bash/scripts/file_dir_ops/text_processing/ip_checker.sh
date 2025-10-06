#! /bin/bash

## this script checks a file for hosts and then reads the file, pings the host with at least packets
## and a timeout then checks if the host is up. if host is up, save the ips to a file (up_hosts.txt)

## check for command arguments

file="$1"

if [ $# -eq 0 ] || [ $# -gt 1 ];
then
	echo "Usage: $0 [Hosts file]"
	echo "file: the file containing the number of hosts"
exit 1
fi


## check if the argument is actually a file

if [ ! -f $file ];
then
	echo "$file is not a regular file"
	exit 1
fi

## read the file

while read -r domain;
do
	echo "The domain is: $domain"
	ping -c2 -W 2 $domain

	## ping -c4 $domain | grep "from" | cut -d ':' -f 1 | awk '{print $4}'

done < $file
