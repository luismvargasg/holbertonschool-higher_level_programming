#!/bin/bash
# Script that takes in a URL and displays all HTTP methods the server will accept
curl -L -sX PUT -d"user_id=98" -H "Origin:HolbertonSchool" 0.0.0.0:5000/catch_me
