#!/bin/bash
#this is a script that takes in the url,
if [ $# -eq 0 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi
byte_size=$(curl -s "$1" | wc -c)
echo "$byte_size"
exit 0
