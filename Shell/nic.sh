#!/bin/bash

ip -4 a | grep ^[0-9^] | awk '{ print $1 $2 }' | awk -F ":" '{ print $1 " " $2 }'

#for i in ${NIC_LIST[@]};
#do
#	echo ${i}
#done


