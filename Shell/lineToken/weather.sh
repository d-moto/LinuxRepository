#!/bin/bash

FILE_PATH="/home/alma1/forecast"

#python3 /home/alma1/wget/fx-cp2.py > fxlog
python3 /home/alma1/wget/weather.py > weatherlog

cat weatherlog >> token-weather.log

#FX=$(<fxlog)
WT=$(<weatherlog)

curl -X POST -H "Authorization: Bearer dozztg39CJCVeRzU4VOGQWFk7cr4Jrya5zGTGfkHV5z" -F "message=$WT" https://notify-api.line.me/api/notify

