#!/bin/bash
#checking the HTTP methods the server can accept nn
curl -sI "$1" | awk '/Allow:/ { gsub(/^[ \t]+|[ \t]+$/, ""); print substr($0, index($0,$2)) }'
