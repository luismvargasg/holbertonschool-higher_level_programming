#!/bin/bash
# Script that takes in a URL and displays all HTTP methods the server will accept
curl -sX GET "$1" -H "X-HolbertonSchool-User-Id: 98"
