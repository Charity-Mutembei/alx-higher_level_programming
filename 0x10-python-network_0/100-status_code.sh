#!/bin/bash
#sends request to passed argument url and returns the response code
curl -s -o /dev/null -w "%{http_code}" "$1"
