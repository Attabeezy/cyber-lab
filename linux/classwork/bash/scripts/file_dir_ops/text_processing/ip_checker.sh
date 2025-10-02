#! /bin/bash

## this script checks a file for hosts and then reads the file, pings the host with at least packets
## and a timeout then checks if the host is up. if host is up, save the ips to a file (up_hosts.txt)

if [ $# -eq 0 ];
then
	echo "Usage: $0 [Hosts file]"
	echo "file: the file containing the number of hosts"
exit 1
fi
