#!/bin/bash
#sends a POST request to the passed URL, and displays the body of the respons
curl -s -X POST -H "email: test@gmail.com" -H "subject: I will always be here for PLD" $1
