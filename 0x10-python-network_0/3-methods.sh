#!/bin/bash
#displays all HTTP methods the server will accept
curl -s -X OPTIONS -I $1 | awk '/^Allow:' | cut -d' ' -f2-
