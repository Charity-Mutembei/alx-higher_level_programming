#!/bin/bash
#Bash script that makes a request to 0.0.0.0:5000/catch_me
grep -o 'You got me!' <<< "$(curl -s "$1")"
