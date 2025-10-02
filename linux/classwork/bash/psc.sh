#! /bin/bash

echo -n "Password: "

read -s pswd

pswd_len=${#pswd}

if [[ $pswd_len -ge 8 ]] && [[ "$pswd" =~ [a-zA-Z] ]] && [[ "$pswd" =~ [0-9] ]]; then
	echo "strong password"
elif [[ $pswd_len -ge 6 ]] && [[ $pswd_len -lt 8 ]]; then
	echo "moderate password"
else
	echo "week password"
fi
