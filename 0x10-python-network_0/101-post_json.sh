#!/bin/bash
#sends json post request to a url passed as first argument and displays body
curl -s -X POST "$1" -d "@$2" -H "Content-Type: application/json"
