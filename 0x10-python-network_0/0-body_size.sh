#!/bin/bash
# Check if the URL argument is provided
curl -s -I "$1" | awk '/^Content-Length:/ {print $2}'
