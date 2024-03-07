#!/bin/bash
#displays all HTTP methods the server will accept
curl -s -X OPTIONS -I $1 | awk '/^Allow: / {for (i = 2; i <= NF; i++) printf "%s ", $i; printf "\n"}'
