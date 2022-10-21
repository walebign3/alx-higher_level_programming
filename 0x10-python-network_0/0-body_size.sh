#!/bin/bash
#Bash script that takes in a URL
curl -s "$1" | grep "Content-Length" | cut -d' ' -f 2
