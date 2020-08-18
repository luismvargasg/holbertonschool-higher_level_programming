#!/bin/bash
# Script that takes in a URL and displays the size of the body of the response.
curl -is "$1" | grep Content-Length | cut -d " " -f2
