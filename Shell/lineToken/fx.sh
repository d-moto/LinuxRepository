#!/bin/bash

FILE_PATH="/home/alma1/forecast"

python3 /home/alma1/wget/fx-cp2.py > fxlog
cat fxlog >> token-fx.log

FX=$(<fxlog)

curl -X POST -H "Authorization: Bearer dozztg39CJCVeRzU4VOGQWFk7cr4Jrya5zGTGfkHV5z" -F "message=$FX" https://notify-api.line.me/api/notify

