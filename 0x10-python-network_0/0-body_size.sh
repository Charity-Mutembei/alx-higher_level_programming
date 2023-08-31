#!/bin/bash
#this is a script that takes in the url,
#sends a request to that url, 
#and displays the size of the body response in bytes
# Check if an argument (URL) is provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi
# Use curl to send a request and pipe the response to wc -c to count bytes
byte_size=$(curl -s "$1" | wc -c)
# Display the byte size of the HTTP response
echo "$byte_size"
exit 0
