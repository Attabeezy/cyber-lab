#! /bin/bash

## this script demonstrates stdout and stderr

echo "This line is stdout, we will save it inside stdout.txt" > stdout.txt

echo "The next command will return an error and therefore we are using stderr redirection to a file called stderr.txt"


newCommand 2> stderr.txt

echo "The next command will return both stdout and stderr to a file called stdout_stderr.txt"
## echo "This is a regular stdout" &> stdout_stderr.txt newCommand &>> stdout_stderr.txt
echo "This is a regular stdout" &> stdout_stderr.txt && newCommand &>> stdout_stderr.txt
