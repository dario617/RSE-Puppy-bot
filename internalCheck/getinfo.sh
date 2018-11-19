#!/bin/sh
date | awk '{printf "{\"Date\": {\"day\": %d, \"month\": \"%s\", \"time\": \"%s\", \"year\": %d, \"timezone\": %d}, ", $3, $2, $4, $6, $5}'
sensors -A | awk -F'[^0-9]*' 'NF > 5 {printf "\"Temp%d\": {\"actual\": %d.%d, \"max\": %d.%d}, ", NR, $3,$4,$5,$6}'
free -m | awk 'FNR==2 {printf "\"Memory\": {\"usage\": %d, \"disponible\": %d}, ", $3, $2}'
df -h | awk '$NF=="/"{printf "\"Disk\": {\"usage\": %d, \"disponible\": %d}, ", $3, $2}'
top -bn1 | grep load | awk '{printf "\"CPU\": %.2f }", $(NF-2)}'