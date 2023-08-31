#!/bin/bash
#this is a script that takes in the url,
curl -s "$1" | wc -c
