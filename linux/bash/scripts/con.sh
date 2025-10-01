x#! /bin/bash
## this does a conditional check
name="Benjamin"
nameCheck=""
age = 18
ageCheck = ""

read -p "Please enter your name: " nameCheck

read -p "Please enter your age: " ageCheck

## -ne: not equal to
## -eq: equal to
## -gt: greater than
## -lt: less than
## <, >, <=, >=. != for strings

if [ $nameCheck != $name ];
then
	echo "You are not the expected user"
else
	echo "Welcome $nameCheck"
fi

if [ $ageCheck -lt $age] || [ $nameCheck != $name];
then
	echo "You cannot register!"
else
	echo "Welcome $name"
fi
