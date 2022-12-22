#!/bin/bash

DATE=`date`
LOG=`date +%Y%m%d`.log
FILE1=`date +%Y%m%d`.log.tmp
FILE2=`date +%Y%m%d`.log.tmp.cut

#curl wttr.in/tokyo > `date +%Y%m%d`.log
curl wttr.in/tokyo > /home/dell-user-alma/forecast/$LOG

#sed -n 1,3p $LOG > `date +%Y%m%d`.log.tmp
sed -n 1,3p /home/dell-user-alma/forecast/$LOG > /home/dell-user-alma/forecast/$FILE1

cat /home/dell-user-alma/forecast/$FILE1 | awk -F" " '{for(i=4;i<NF;i++) {printf("%s%s",$i,OFS=" ")} print $NF}' > /home/dell-user-alma/forecast/$FILE2

location=`cat /home/dell-user-alma/forecast/$FILE2 | awk 'NR==1 {print}'`
forecast=`cat /home/dell-user-alma/forecast/$FILE2 | awk 'NR==3 {print}'`

echo $location
echo $forecast

curl -X POST -H "Authorization: Bearer dozztg39CJCVeRzU4VOGQWFk7cr4Jrya5zGTGfkHV5z" -F "message=$location" https://notify-api.line.me/api/notify
curl -X POST -H "Authorization: Bearer dozztg39CJCVeRzU4VOGQWFk7cr4Jrya5zGTGfkHV5z" -F "message=$forecast" https://notify-api.line.me/api/notify
