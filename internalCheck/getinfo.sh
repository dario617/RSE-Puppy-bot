#!/bin/sh
date | awk '{printf "{\"Date\": {\"day\": %d, \"month\": \"%s\", \"time\": \"%s\", \"year\": %d, \"timezone\": %d}, ", $3, $2, $4, $6, $5}'
sensors -A | awk -F'[^0-9]*' 'NF > 3 {printf "\"Temp%d\": {\"actual\": %s, \"max\": %s}, ", NR, $3,$4}'
free -m | awk 'FNR==2 {printf "\"Memory\": {\"usage\": %d, \"disponible\": %d}, ", $3, $2}'
df -h | awk '$NF=="/"{printf "\"Disk\": {\"usage\": %d, \"disponible\": %d}, ", $3, $2}'
top -bn1 | grep load | awk -F'[^0-9]*' '{printf "\"CPU\": %s.%s }", $(NF-5), $(NF-4)}'