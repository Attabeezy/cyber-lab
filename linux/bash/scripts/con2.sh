#! /bin/bash
## this does a conditional check
name="Ben"
nameCheck=""
age=18
ageCheck=""

read -p "Please enter your name: " nameCheck

read -p "Please enter your age: " ageCheck

## -ne: not equal to
## -eq: equal to
## -gt: greater than
## -lt: less than
## <, >, <=, >=. != for strings


if [ $age -gt 18 ] && [ "$nameCheck" == $name ];
then
	echo "Welcome $name, you can proceed to register"
else
	echo "You have to be above 18 to register"
fi
